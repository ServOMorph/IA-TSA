# Roadmap — IA-TSA

## Phase : Sélection utilisateur + logging horodaté [FAIT]

### Objectif
À l'ouverture de l'UI, choisir un utilisateur (éducateur/admin) avant tout accès aux
autres écrans. Par défaut "admin", pas de mot de passe, possibilité de créer un nouveau
nom d'utilisateur. Une fois l'utilisateur choisi, toute action dans l'UI (navigation,
activités, retours terrain) est journalisée avec horodatage et utilisateur.
But : analyse fine des parcours pour améliorer le projet (pas de finalité de contrôle
individuel des enfants — RGPD : aucune donnée enfant/établissement dans les logs).

### 1. Modèle utilisateur
- Fichier `data/users.json` : liste `[{"name": "admin", "created": "..."}]`.
- "admin" créé par défaut si le fichier n'existe pas.
- Pas de mot de passe, pas d'email, pas de rôle — simple étiquette de session.
- Gestion complète : suppression et renommage possibles (pas seulement création).
  Route `/utilisateur/<nom>/supprimer` (POST) et `/utilisateur/<nom>/renommer` (POST).
  "admin" non supprimable (dernier utilisateur de secours).
- Renommage : le nom est la seule clé dans les logs (pas d'id stable) — un
  renommage casse le lien avec les logs passés (l'ancien nom y reste tel quel).
  Discontinuité acceptée sciemment (usage artisanal, peu d'utilisateurs), pas
  traitée comme un bug.

### 2. Sélection à l'ouverture
- `before_request` global : si `session["user"]` absent et route hors `/utilisateur*`
  et hors assets statiques → redirection vers `/utilisateur`.
- Page `/utilisateur` (GET) : liste des utilisateurs existants (boutons) + champ
  "créer un nouvel utilisateur".
- POST `/utilisateur` : valide le nom (non vide, trim, unique), l'ajoute à
  `users.json` si nouveau, stocke `session["user"] = nom`, redirige vers `/`.
- Nécessite `app.secret_key` (clé fixe en config locale, non commitée si sensible —
  ici pas de données sensibles donc clé statique acceptable).
- Bouton "changer d'utilisateur" visible dans le layout (sidebar) → vide la session.
- `PERMANENT_SESSION_LIFETIME` court (quelques heures) : sur un poste de salle
  informatique rarement fermé, une session qui ne périme jamais attribuerait les
  actions d'une séance ultérieure au dernier utilisateur choisi. Expiration force
  un re-choix à chaque séance.
- `before_request` revalide que `session["user"]` existe toujours dans
  `users.json` (cas d'un utilisateur supprimé entre-temps) → sinon vidage de
  session et redirection vers `/utilisateur`.

### 3. Logging horodaté
- Fichier `data/logs/activite_<AAAA-MM>.jsonl` (rotation mensuelle simple), une ligne
  JSON par événement, schéma unifié :
  `{"ts": "ISO8601", "user": "...", "type": "nav"|"event", "route": "...",
  "method": "...", "activite": "...", "event": "...", "detail": "..."}`
  (champs non applicables omis selon le type).
- Hook `after_request` global : log automatique de chaque requête (route + méthode +
  utilisateur) avec `type: "nav"`, sauf routes statiques/API technique et sauf
  `/api/log-event` lui-même (déjà loggé côté endpoint — éviter le double log).
  `/api/tts` : appel loggé, jamais le texte transmis.
- Retours terrain (`retour_terrain_save`) : ajouter `"user"` aux nouvelles entrées
  sauvegardées dans `retours_terrain.json`. Les entrées existantes ne sont pas
  migrées (champ absent = donnée antérieure à la fonctionnalité, pas de valeur
  par défaut ajoutée).
- Événements fins dans les activités (touche pressée, changement de réglage,
  démarrage/fin d'activité) sont loggés dès cette itération avec `type: "event"`,
  via un endpoint commun `POST /api/log-event`
  (`{"activite": "...", "event": "...", "detail": "..."}`), horodaté et associé
  à l'utilisateur en session côté serveur.
- Événement de fin/sortie d'activité : émis via `navigator.sendBeacon` (pas `fetch`)
  pour éviter la perte de l'événement si la navigation coupe la requête en vol.

### 4. Fichiers impactés
- `UI/__init__.py` : `app.secret_key`, enregistrement du hook `before_request`/`after_request`.
- `UI/routes.py` : nouvelles routes `/utilisateur` (GET/POST/supprimer/renommer),
  `/api/log-event` (POST), fonctions `_load_users`/`_save_users`, `_log_event`.
- `UI/templates/utilisateur.html` : nouveau template (sélection, création,
  suppression, renommage).
- `UI/templates/layout.html` (ou équivalent) : bouton "changer d'utilisateur" +
  affichage utilisateur courant.
- `UI/static/js/activity-core.js` : socle JS commun aux 4 activités déjà existant —
  y ajouter la fonction `logEvent()` (fetch/sendBeacon vers `/api/log-event`),
  appelée depuis chaque script d'activité (`cause-effet.js`, `choix.js`, `ecoute.js`,
  `timer.js`). Un seul point d'instrumentation, pas de duplication dans les
  4 templates.
- `data/users.json`, `data/logs/` : nouveaux, ignorés RGPD-safe (pas de données enfant).

### 5. Contraintes
- RGPD : les logs ne contiennent que route/utilisateur/horodatage/nom d'activité,
  jamais de contenu saisi par l'enfant (ex. texte tapé dans "Écris et écoute"
  exclu du log).
- RGPD — condition de validité de l'analyse : le champ "user" désigne l'éducateur,
  pas l'enfant ; les logs restent conformes tant qu'aucun enfant n'est identifiable
  ni corrélable (ex. en croisant un horodatage de log avec un retour terrain qui
  nommerait un enfant). Si un futur usage introduit une identification indirecte
  de l'enfant, revoir la conformité avant de l'activer.
- Pas d'authentification réelle (pas de mot de passe) — accepté explicitement par
  la demande, à ne pas présenter comme une sécurité.

### 6. Étapes suivantes après implémentation
- Tester le flux complet (sélection, navigation, activités, retour terrain) en séance.
- Écran de consultation des logs dans l'UI : reporté à une itération ultérieure
  (lecture directe des fichiers `data/logs/*.jsonl` suffisante pour l'instant).

---

## Phase : Jeu dyadique "Regarde où je regarde" (balayage) [EN COURS]

### Objectif
Premier jeu à deux joueurs (adulte + jeune) du projet, comblant l'angle mort identifié
le 2026-07-27 : toutes les activités existantes sont solitaires (adulte pilote/observe,
ne joue pas). Cible pédagogique nommée : attention conjointe et alternance des rôles
initiateur/suiveur — mécanique la mieux soutenue par la littérature consultée
(voir [docs/reference/jeux_video_tsa.md](docs/reference/jeux_video_tsa.md)).

Contrainte terrain déterminante (mémorisée le 2026-07-27, voir `.claude/memory.md`) :
les jeunes ne sont pas autonomes avec la souris → entrée jeune limitée à une seule
touche (accès contacteur/switch), ce qui exclut toute variante à choix multiple
côté jeune. D'où le choix du **balayage automatique** : les zones s'éclairent l'une
après l'autre en boucle, le jeune appuie sa touche unique quand le balayage atteint
la zone désignée par l'adulte.

### 1. Mécanique de jeu
- Grille de zones (2 puis 4 selon palier), une seule active visuellement à la fois.
- Rôle "désignateur" (débute par l'adulte) : marque une zone (clic ou touche adulte) —
  contour épais + son propre, marquage durable (ne s'éteint pas).
- Balayage automatique en boucle continue sur toutes les zones, vitesse réglable.
- Rôle "suiveur" (débute par le jeune) : une seule touche (Espace par défaut,
  configurable), appui valide seulement si le balayage est sur la zone marquée.
- Match : marquages fusionnent, animation + son communs (seul moment "célébré").
- Non-match : aucune pénalité, aucun compteur d'échec, le balayage continue sans
  interruption, la zone reste marquée, le jeune peut retenter au tour suivant.
- Pas de fin de boucle automatique, pas de limite de tentatives — cohérent avec le
  principe projet "pas de minuterie implicite" (docs/pedagogie/projet_pedagogique.md §3).
- Inversion des rôles (palier 5) : le jeune désigne une zone de son choix (aucune
  "bonne" zone), l'adulte doit la rejoindre au balayage.

### 2. Paliers de progression (déclenchés manuellement par l'adulte, jamais par timer)
1. 2 zones, balayage très lent
2. 2 zones, balayage plus rapide
3. 4 zones (disposition croix)
4. 4 zones, la zone marquée cesse d'être visible pendant le balayage (mémoire)
5. Inversion des rôles activée

### 3. Réglages exposés (panel_extra du socle activite_base.html)
- Vitesse de balayage (paramètre le plus déterminant à ajuster en séance)
- Nombre de zones (2 / 4)
- Pause entre deux cycles de balayage
- Anti-rebond : ignorer les appuis répétés à moins de N ms (contacteur maintenu
  ne doit pas générer de rafale d'appuis)
- Touche du jeune configurable
- Réglages socle existants réutilisés tels quels : son, intensité, taille, mode calme

### 4. Fichiers impactés
- `UI/routes.py` : nouvelle route `/activites/regarde-ou-je-regarde`
  (suivre le patron des routes `/activites/*` existantes).
- `UI/templates/activite_regarde.html` : nouveau template, étend `activite_base.html`,
  bloc `panel_extra` pour les réglages spécifiques.
- `UI/static/js/regarde.js` : nouveau script d'activité.
- `UI/static/js/activity-core.js` : évaluer si la logique de balayage/palier/tour
  est assez générique pour vivre dans un module partagé réutilisable par de futures
  activités à tour de rôle, ou si elle reste locale à `regarde.js` pour cette
  première itération (trancher en développant, ne pas sur-abstraire prématurément).
- `UI/templates/activites.html` : ajouter la tuile du nouveau jeu au catalogue.
- Logging : réutiliser `ActivityCore.logEvent()` pour les événements clés (désignation,
  match, changement de palier, inversion de rôle) — aucun contenu enfant, RGPD inchangé.

### 5. Contraintes héritées du projet
- Prévisibilité stricte : mapping zone/touche fixe, aucun aléatoire visible.
- Pas d'échec punitif : jamais de croix rouge, buzzer, ou décompte de tentatives ratées.
- Mode calme et réglages persistés en localStorage, comme les 4 activités existantes.
- RGPD : aucune donnée enfant dans le code, les logs, ou les commits.

### 6. Tests avant [FAIT]
- Test fonctionnel de la mécanique (désignation, balayage, match, non-match,
  inversion) sur les 5 paliers.
- Test en séance réelle avec un jeune : le palier 1 (2 zones, balayage très lent)
  peut être un plafond durable pour certains profils et non une simple introduction
  (réserve notée le 2026-07-27) — noter l'observation dans l'onglet Terrain plutôt
  que de forcer la progression.
- Vérifier l'anti-rebond avec un appui maintenu (simulation contacteur).

### 7. Limite assumée
Cette conception s'appuie sur une synthèse de littérature ponctuelle et non revue par
les pairs (docs/reference/jeux_video_tsa.md). Le jeu est un support d'interaction pour
l'accompagnant, pas une intervention validée cliniquement — à ne jamais présenter comme telle.

**⏸ Checkpoint** — Demander à l'utilisateur de faire `/compact` avant de continuer.
Attendre sa réponse écrite. Ne pas commencer la phase suivante sans confirmation.

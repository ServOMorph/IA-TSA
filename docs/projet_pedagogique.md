# Projet pédagogique — IA-TSA

> Document de présentation du projet IA-TSA à destination de toute personne souhaitant comprendre l'intention, le contenu et la démarche. Ne contient aucune donnée personnelle (conformité RGPD).

---

## 1. Contexte et objectif

Le projet **IA-TSA** explore comment des outils numériques codés sur mesure peuvent soutenir l'accompagnement individuel de personnes présentant un trouble du spectre de l'autisme (TSA), dans un contexte d'accès à une salle informatique.

L'objectif n'est pas de remplacer l'accompagnant, mais de lui fournir des **outils adaptés, contrôlables et ajustables en séance**, en s'appuyant sur les données de la recherche (HAS 2026, arXiv, NCBI) et sur les retours terrain directs.

Le projet est en **recherche-action** : chaque activité est testée, observée, ajustée.

---

## 2. Ancrage dans les recommandations

Les recommandations HAS (2026) rappellent trois principes fondateurs qui orientent toutes les décisions de conception :

1. **Interventions développementales et comportementales en priorité** — le numérique est un support, pas une fin.
2. **Prévisibilité et structure** — rendre visible ce qui va se passer ; réduire les surprises.
3. **Calibration de l'intensité** — éviter autant la sous-stimulation que la surcharge sensorielle.

Le numérique convient au TSA pour des raisons structurelles : prévisibilité de la machine (pas de charge sociale), support visuel natif, absence de jugement, réaction constante et immédiate.

---

## 3. Principes de conception des activités

Chaque activité produite dans ce projet respecte un socle commun :

| Principe | Mise en œuvre concrète |
|----------|------------------------|
| **Cause-effet immédiat** | Toute action produit une réaction visible et audible dans les 100 ms |
| **Écran calme** | Rien ne bouge sans action de l'utilisateur ; pas d'animation autonome |
| **Contraste fort** | Formes simples, couleurs saturées sur fond sombre |
| **Son optionnel** | WebAudio (première interaction obligatoire selon politique navigateur) ; peut être coupé |
| **Mode calme** | Réduit les animations et la charge visuelle (accessible via le panneau réglages) |
| **Pas de minuterie implicite** | Aucune pression temporelle cachée — sauf si c'est l'objet de l'activité |
| **Réglages persistés** | localStorage : l'accompagnant retrouve ses réglages d'une séance à l'autre |
| **RGPD** | Aucune donnée sur les enfants ni sur l'établissement dans le code ou les commits |

---

## 4. Activités disponibles

### 4.1 Touche → ça réagit (cause-effet pur)

**Objectif pédagogique** : établir ou consolider le lien de causalité « mon action produit un effet ».

**Public cible** : profils avec besoin de soutien important, motricité sévèrement limitée, en phase de découverte du contrôle sur l'environnement.

**Fonctionnement** : n'importe quelle interaction (clic, touche, tap) déclenche une réaction visuelle (forme colorée animée) et sonore (note WebAudio). L'accompagnant pilote ; l'apprenant peut indiquer un choix par n'importe quel moyen (regard, geste, vocalise). L'écran reste calme entre les actions.

**Réglages disponibles** : vitesse de l'animation, volume, mode calme.

---

### 4.2 Choix entre deux (proto-CAA)

**Objectif pédagogique** : exercer la prise de décision et la communication par le choix. Première étape vers la communication alternative et augmentée (CAA).

**Public cible** : profils progressant vers la décision intentionnelle et la communication fonctionnelle.

**Fonctionnement** : deux grandes zones (gauche / droite) affichant des formes contrastées (cercle / carré). L'apprenant indique un choix par n'importe quel moyen ; l'accompagnant valide en cliquant sur la zone choisie → animation et son spécifiques à cette zone.

**Principe CAA** : pictogrammes, formes, couleurs — substituables pour personnaliser selon le profil. La dichotomie gauche/droite peut représenter n'importe quelle paire (activité souhaitée, objet, lieu).

**Réglages disponibles** : sons distincts par zone, mode calme.

---

### 4.3 Timer visuel (structuration du temps)

**Objectif pédagogique** : matérialiser l'attente et rendre les transitions prévisibles. Réduit l'anxiété liée à « combien de temps encore ? ».

**Public cible** : profils avec difficultés de gestion du temps et des transitions, anxiété liée à l'imprévisibilité.

**Fondement** : recommandation HAS §3.5 — rendre visible ce qui va se passer avant/après une activité ; matérialiser la durée via des supports visuels.

**Fonctionnement** : timer décomptant avec 5 visuels sélectionnables, signal doux (son + animation) en fin de temps. Durée réglable de 1 à 15 minutes directement sur le stage (boutons +/− min/sec, visibles à l'arrêt, masqués en cours de décompte).

**5 visuels disponibles** :
- **Anneau** — cercle qui se referme progressivement
- **Blocs** — grille de blocs qui disparaissent un à un
- **Barre** — barre de progression horizontale
- **Soleil** — rayons qui disparaissent progressivement
- **Couleur** — dégradé qui évolue du vert vers le rouge

Le visuel est sélectionné dans le panneau réglages (boutons custom, pas de `<select>` natif). Choix persisté en localStorage.

---

## 5. Infrastructure technique

| Composant | Détail |
|-----------|--------|
| **Stack** | Flask 3.0 (Blueprint, app factory, Jinja2), port 4110 |
| **Frontend** | JS vanilla + CSS charte SéréniaTech (dark mode, reduced motion) |
| **Démarrage** | `python run.py` (autoreload activé) |
| **Module Python** | `from UI import create_app` — majuscules obligatoires (Windows/Python case-sensitive) |
| **Retours terrain** | `data/retours_terrain.json` — persisté localement, gitignoré (RGPD) |
| **Licence** | MIT — repo public |

**Socle JS réutilisable** (`activity-core.js`) : gestion réglages, WebAudio, mode calme, panneau extensible (`panel_extra`). Chaque nouvelle activité étend `activite_base.html` et surcharge uniquement ce qui la différencie.

---

## 6. Onglet Retour terrain

L'onglet **Terrain** de la sidebar permet à l'accompagnant de noter, après chaque séance :

- l'activité utilisée
- le niveau d'engagement observé (engagé / neutre / retrait)
- les réglages utilisés
- une note libre

Les données sont stockées localement (`data/retours_terrain.json`, gitignoré) et ne transitent par aucun service externe. Elles servent uniquement à ajuster les activités et les paramètres par défaut.

---

## 7. Roadmap pédagogique

Les activités sont priorisées selon les besoins identifiés dans la recherche et les retours terrain.

**Réalisé :**
- Cause-effet pur
- Choix entre deux (proto-CAA)
- Timer visuel (5 visuels)
- Onglet retour terrain

**En attente de retours terrain :**
- Ajustement des paramètres par défaut (visuel timer retenu, durées, réglages)

**Prochaines activités envisagées :**
- **Pictogrammes CAA** — communication par pictogrammes, expression de besoins/émotions
- **Séquence avant/après** — structuration d'une routine en étapes visuelles

---

## 8. Cadre éthique et RGPD

- **Aucune donnée sur les enfants** ne figure dans le code, les fichiers, les commits ou tout artefact du projet.
- **Aucune donnée sur l'établissement** n'est présente.
- Les retours terrain sont stockés localement et exclus du dépôt (`.gitignore`).
- Le projet est open source (MIT) : le code est lisible, auditable, réutilisable.
- Tout outil numérique est au service de l'accompagnant, pas autonome. L'accompagnant reste décisionnaire en séance.

---

*Document créé le 19 juin 2026 — projet IA-TSA. À mettre à jour au fil des retours terrain et de l'évolution des activités.*

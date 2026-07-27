# Changelog

## v1.2 — 2026-07-27

### Ajouté
- 5e activité "Regarde où je regarde" : premier jeu dyadique du projet (route `/activites/regarde-ou-je-regarde`, template, `regarde.js`, styles). Balayage automatique, 5 paliers, mode mémoire, inversion des rôles, anti-rebond par touche, réglages persistés en localStorage
- Bouton "Règles du jeu" dans la barre d'icônes des 5 activités : modale explicative destinée à l'accompagnant (bloc Jinja `regles` dans `activite_base.html`, câblage dans `activity-core.js`, fermeture par Échap ou clic hors modale)
- Bouton "Théorie" par activité dans le catalogue : modale présentant cible visée, fondements issus de `docs/`, réserve méthodologique et source (dict `THEORIE` dans `UI/routes.py`)
- docs/reference/analyses/analyse_ecran_victoire.md : analyse concluant au refus d'un écran de victoire "Gagné"

### Modifié
- Jeu "Regarde où je regarde" rendu entièrement clavier : `Entrée` pour l'adulte (désigne), `Espace` pour le jeune (valide). Désignation à la souris et touche configurable supprimées
- Marquage de la zone désignée renforcé : bordure épaissie, halo lumineux et pulsation douce (désactivée en mode mémoire et en mouvements réduits)
- Catalogue des activités : carte restructurée avec boutons "Théorie" et "Ouvrir" distincts

### Corrigé
- Les touches du jeu ne répondaient plus dès l'ouverture du panneau de réglages (blocage `panelOpen()` hérité de `choix.js`), rendant le jeu injouable dans son cas d'usage normal
- Aucune zone n'était éclairée pendant le premier cycle de balayage (appel initial à `render()` manquant)

## v1.1 — 2026-07-27

### Ajouté
- docs/reference/jeux_video_tsa.md : synthèse de littérature sur les jeux numériques et le TSA (mécaniques, coopération vs compétition, réserves méthodologiques)
- roadmap.md : phase "Jeu dyadique Regarde où je regarde" (balayage + touche unique) spécifiée, [EN COURS]
- .claude/memory.md : contrainte projet mémorisée — jeunes non autonomes à la souris, entrée limitée à une touche
- CHANGELOG.md : création

### Modifié
- roadmap.md : phase "Sélection utilisateur + logging horodaté" marquée [FAIT]
- README.md : section "En cours" ajoutée

## v1.0 — 2026-07-16

### Ajouté
- Sélection utilisateur à l'ouverture (`/utilisateur`, admin par défaut, création/renommage/suppression)
- Logging horodaté unifié (`data/logs/activite_AAAA-MM.jsonl`) : navigation automatique + événements fins via `/api/log-event`
- Association des retours terrain à un utilisateur

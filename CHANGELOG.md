# Changelog

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

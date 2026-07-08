# IA-TSA

Recherche appliquée sur l'usage de l'IA comme outil d'aide pour les personnes atteintes de troubles du spectre autistique (TSA).

## Objectif

Explorer comment des outils basés sur l'intelligence artificielle peuvent soutenir l'accompagnement individuel de personnes avec TSA, dans un contexte éducatif avec accès à une salle informatique.

## Contraintes

- **RGPD stricte** : aucune donnée personnelle, comportementale ou de santé ne figure dans ce dépôt
- Projet open source — licence MIT

## Stack

- **Web UI** : Flask 3.0 — lancer avec `python run.py` (port 4110, autoreload)
- **Frontend** : Jinja2 + JS vanilla + CSS charte SéréniaTech (dark mode, reduced motion)
- **Docs** : `docs/` (pedagogie/, reference/, web/) — explorateur arborescent dans l'UI (onglet Recherches), rendu Markdown
- **Activités** : activités codées maison (onglet Activités) — cause-effet pur, choix entre deux
- **Retours terrain** : onglet Terrain dans la sidebar — notes d'observation persistées localement (`data/`, gitignoré RGPD)

## Licence

[MIT](LICENSE)

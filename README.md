# IA-TSA

Recherche appliquée sur l'usage de l'IA comme outil d'aide pour les personnes atteintes de troubles du spectre autistique (TSA).

## Objectif

Explorer comment des outils basés sur l'intelligence artificielle peuvent soutenir l'accompagnement individuel de personnes avec TSA, dans un contexte éducatif avec accès à une salle informatique.

## Contraintes

- **RGPD stricte** : aucune donnée personnelle, comportementale ou de santé ne figure dans ce dépôt
- Projet open source — licence MIT

## Stack

- **Web UI** : Flask 3.0 — `pip install -r requirements.txt` puis `python run.py` (port 4110, autoreload)
- **Frontend** : Jinja2 + JS vanilla + CSS charte SéréniaTech (dark mode, reduced motion)
- **Docs** : `docs/` (pedagogie/, reference/, web/) — explorateur arborescent dans l'UI (onglet Recherches), rendu Markdown
- **Activités** : activités codées maison (onglet Activités) — cause-effet pur, choix entre deux, timer visuel, écris et écoute
- **Synthèse vocale** : Piper TTS (local, gratuit) pour l'activité "Écris et écoute" — modèle voix à télécharger sur chaque poste : `python -m piper.download_voices fr_FR-siwis-medium --download-dir voices` (non versionné, gitignoré)
- **Retours terrain** : onglet Terrain dans la sidebar — notes d'observation persistées localement (`data/`, gitignoré RGPD)
- **Session utilisateur** : sélection d'un utilisateur (éducateur) à l'ouverture (`/utilisateur`, admin par défaut) + logging horodaté des parcours (navigation et événements d'activité), sans donnée sur l'enfant (`data/`, gitignoré RGPD)

## Licence

[MIT](LICENSE)

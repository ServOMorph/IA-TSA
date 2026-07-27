# IA-TSA : Recherche appliquée et activités d'accompagnement par l'IA pour l'autisme (TSA)

Projet de recherche appliquée explorant l'usage de l'intelligence artificielle comme outil de soutien et d'accompagnement individuel pour les personnes avec troubles du spectre autistique (TSA) en contexte éducatif.

Ce dépôt implémente une interface web locale et sécurisée développée en **Python** avec **Flask**, conçue pour fonctionner de manière complètement autonome sans connexion Internet requise, dans le respect strict du RGPD.

## Objectif

Explorer et concevoir des activités numériques adaptées (cause-effet, choix, structuration du temps, association mot-son avec synthèse vocale locale, jeu coopératif à deux) pour soutenir le développement cognitif et la communication d'apprenants avec TSA en salle informatique.

Contrainte de conception déterminante : les apprenants n'étant pas autonomes avec la souris, **toute activité est pilotable intégralement au clavier** (ou par contacteur mappé sur une touche) côté apprenant. La souris reste réservée à l'accompagnant.

## Fonctionnalités & Activités

Le projet propose une suite d'applications et de ressources accessibles via une barre latérale :
1. **Recherches (Explorateur de documents)** : Permet de consulter localement les travaux de recherche, documentations pédagogiques et techniques stockés en Markdown dans `docs/`.
2. **Activités personnalisées** :
   - **Touche → ça réagit** : Activité cause-effet pure (découverte du lien causal, attention conjointe). Toute touche ou clic déclenche une réaction visuelle et sonore douce.
   - **Choix entre deux** : Aide à la décision et à la communication (Proto-CAA). L'apprenant sélectionne une option et l'accompagnant valide pour lancer l'animation.
   - **Timer visuel** : Sablier circulaire dynamique matérialisant l'attente et facilitant les transitions pour réduire l'anxiété.
   - **Écris et écoute** : Synthèse vocale locale via **Piper TTS**. L'apprenant tape un mot ou une suite de lettres pour l'écouter.
   - **Regarde où je regarde** : Premier jeu **dyadique** (adulte + jeune) du projet. Les zones s'éclairent en boucle (balayage automatique) ; l'adulte désigne une zone avec `Entrée`, le jeune la valide avec `Espace` au bon moment. 5 paliers de difficulté déclenchés manuellement, sans échec ni score. Cible : attention conjointe et alternance des rôles.
3. **Retours terrain** : Interface d'observation permettant à l'accompagnant de consigner l'engagement (engagé, neutre, retrait), les réglages utilisés et ses notes après chaque séance.
4. **Session utilisateur & Traçabilité** : Identification simple de l'éducateur à l'ouverture avec journalisation locale de l'utilisation (navigation et événements fins) à des fins d'analyse.
5. **Documentation intégrée** : Chaque activité expose un bouton **Règles du jeu** expliquant son fonctionnement à l'accompagnant, et le catalogue propose pour chacune une fiche **Théorie** résumant la cible visée, les fondements issus de `docs/` et les réserves méthodologiques.

## En cours

Le jeu dyadique "Regarde où je regarde" est **codé et validé par tests navigateur automatisés**. Restent à faire : l'essai en séance réelle et la vérification de l'anti-rebond sur contacteur physique. Détails dans `roadmap.md` et `docs/reference/jeux_video_tsa.md`.

Aucune activité n'a encore été éprouvée en séance réelle — c'est la priorité du projet.

## Architecture & Concepts clés

- **Respect strict du RGPD** : Aucune donnée personnelle, comportementale, nominative ou de santé concernant les enfants n'est collectée ou transmise. Les retours terrain et les logs de parcours de l'éducateur sont stockés localement dans le dossier `data/` (exclu du suivi de version Git).
- **Synthèse vocale locale (Offline)** : Utilisation de **Piper TTS** pour générer les voix de manière locale. Aucune requête n'est envoyée à un service cloud pour lire le texte écrit par l'enfant.
- **Conception UI accessible** :
  - Palette colorée harmonieuse SéréniaTech (mode sombre reposant).
  - Réduction des animations et des stimuli (conforme aux préférences de mouvements réduits).
  - Ergonomie simplifiée adaptée aux troubles moteurs et attentionnels.

## Stack technique

- **Backend** : Python 3.11+, Flask 3.0, Piper TTS, Markdown
- **Frontend** : HTML5 (Jinja2), CSS3 Vanilla (Design System SéréniaTech, adaptatif), JavaScript Vanilla

## Prérequis et Installation

### 1. Installation des dépendances
Cloner le projet et installer les dépendances Python requises :
```bash
pip install -r requirements.txt
```

### 2. Téléchargement des voix locales
Pour l'activité de synthèse vocale, téléchargez le modèle de voix en français siwis-medium (le script le placera dans le dossier `voices/` exclu de Git) :
```bash
python -m piper.download_voices fr_FR-siwis-medium --download-dir voices
```

### 3. Démarrage de l'application
Lancez le serveur Flask de développement :
```bash
python run.py
```
L'application sera accessible localement à l'adresse suivante : [http://localhost:4110](http://localhost:4110).

## Licence

Ce projet est sous licence open source **MIT**. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.

Copyright (c) 2026 ServOMorph

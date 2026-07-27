# Analyse — Faut-il un écran "Gagné" dans le jeu dyadique ?

**Date** : 2026-07-27
**Objet** : évaluer la pertinence d'ajouter un écran de victoire plein écran (pictogramme + mot "Gagné" + menu de décision pour l'adulte : refaire une partie / changer les paramètres) au jeu "Regarde où je regarde".
**Statut** : proposition **non retenue** à ce stade.

## Demande initiale

À chaque réussite du jeune (match entre la zone désignée et la validation), afficher un écran dédié :
- un visuel de type pictogramme signalant la réussite
- le mot "Gagné"
- deux choix pour l'adulte : refaire une partie, ou changer les paramètres
- une fois les paramètres modifiés et validés, la partie reprend

## Ce que dit la littérature

### Le feedback intrinsèque prime sur le feedback symbolique

Les mécanismes de récompense identifiés comme efficaces dans les jeux sérieux pour enfants TSA restent **intégrés au flux du jeu** : effets visuels courts (scintillement, animation de la cible), effets sonores, retours immédiats. Aucune des interventions recensées ne repose sur une interstitielle de victoire bloquante (Reward Feedback Mechanism in Virtual Reality Serious Games, JMIR Serious Games 2025 — https://games.jmir.org/2025/1/e67338/).

Un point est explicitement documenté : certains enfants autistes, en particulier les profils avec besoin de soutien important, **ne valorisent pas les résultats quantitatifs ou symboliques** (scores, mentions de victoire) autant que les éléments intrinsèquement intéressants — effets audio et visuels (Designing computer-based rewards with and for children with Autism Spectrum Disorder and/or Intellectual Disability, ScienceDirect — https://www.sciencedirect.com/science/article/abs/pii/S0747563217303515).

Or le public visé par ce jeu est précisément celui-là : jeunes non autonomes à la souris, accès par contacteur une touche.

### L'encouragement de l'adulte fait le travail que l'écran prétend faire

Dans les protocoles combinant récompense symbolique (jetons) et encouragement verbal de l'accompagnant, **c'est l'encouragement verbal qui domine l'effet** et produit l'amélioration durable (LUDIFICATION ET AUTISME, FIRAH — https://www.firah.org/upload/activites-et-publications/progammes-thematiques/autisme-nouvelles-technologies/autisme-et-jeux/fr-gamification-in-autism.pdf).

Dans un jeu explicitement dyadique, la célébration de la réussite est donc mieux portée par l'adulte présent que par un écran. Un écran qui interrompt le jeu déplace l'attention du partenaire humain vers la machine — à rebours de la cible pédagogique annoncée (attention conjointe).

### La récompense visuelle courte est déjà présente

Les jeux somatosensoriels efficaces utilisent des effets de victoire de type "scintillement d'étoiles" — brefs, non bloquants, enchaînés dans le flux (Research on the design of somatosensory interactive games for autistic children based on art therapy, Frontiers in Psychiatry — https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2023.1207023/full).

C'est exactement ce que fait déjà l'animation `match` du jeu (pulsation de la zone + son commun). Le besoin de feedback de réussite est donc **déjà couvert**.

## Ce que dit le projet lui-même

L'écran demandé entre en conflit direct avec quatre décisions déjà actées :

| Principe déjà retenu | Source | Conflit |
|---|---|---|
| "Écran calme : rien ne bouge sans action de l'utilisateur, pas d'animation autonome" | [projet_pedagogique.md §3](../../pedagogie/projet_pedagogique.md) | Un écran plein surgissant seul est une animation autonome imposée |
| "Pas de fin de boucle automatique, pas de limite de tentatives" | [roadmap.md phase 2 §1](../../../roadmap.md) | Un écran de victoire crée une fin de partie là où il n'y en a pas |
| "Prévisibilité : mapping action → effet fixe, pas d'aléatoire visible" | [jeux_video_tsa.md §3](../jeux_video_tsa.md) | Une rupture plein écran est une transition non annoncée |
| "Feedback immédiat et distinct, sans connotation d'échec" | [jeux_video_tsa.md §3](../jeux_video_tsa.md) | Déjà satisfait par l'animation `match` existante |

Le projet consacre par ailleurs une activité entière (Timer visuel) à rendre les transitions prévisibles. Introduire une transition brutale non anticipée dans un autre outil du même projet serait incohérent.

## Problème de conception non résolu par la demande

Le jeu n'a **aucune notion de "partie"** : c'est une boucle de balayage continue produisant des matchs successifs. Un écran "Gagné" oblige à définir un seuil de déclenchement qui n'existe dans aucune décision prise :

- à chaque match ? → le jeu devient une suite de rounds hachés par des écrans, l'exigence attentionnelle du balayage continu disparaît
- après N matchs consécutifs ? → introduit un compteur de performance, donc une mesure quantitative, précisément ce que la littérature signale comme peu valorisé par ce public

Aucune des deux options n'est neutre sur la conception.

## Le besoin réel est déjà couvert

Le besoin fonctionnel derrière la demande — *permettre à l'adulte de changer les réglages puis de reprendre* — est déjà satisfait :

- le panneau de réglages (⚙️) est accessible à tout moment sans interrompre le balayage
- les touches Entrée (adulte) et Espace (jeune) restent actives panneau ouvert (vérifié par test navigateur le 2026-07-27)
- les réglages s'appliquent immédiatement, sans validation ni reprise à gérer

## Conclusion

**Recommandation : ne pas implémenter l'écran "Gagné".** Le feedback de réussite existe déjà sous une forme mieux soutenue par la littérature (animation + son, non bloquants), le besoin de réglage à la volée est déjà couvert, et l'écran contredirait quatre principes de conception actés du projet.

**Alternative si le besoin de marquer une fin réapparaît en séance** : une fin de session déclenchée **volontairement par l'adulte** (et non par un seuil automatique de performance), qui resterait cohérente avec le principe "progression déclenchée manuellement, jamais par timer". À n'implémenter que si un retour terrain fait apparaître ce besoin.

## Limite de cette analyse

Recherche web ponctuelle (juillet 2026), non exhaustive, non revue par les pairs, dans la continuité de la réserve méthodologique posée dans [jeux_video_tsa.md §2](../jeux_video_tsa.md). Aucun retour terrain n'est encore disponible sur ce jeu — cette analyse oriente une décision de conception, elle ne la valide pas empiriquement. Si l'observation en séance contredit ces conclusions, elle prime.

## Sources

- Reward Feedback Mechanism in Virtual Reality Serious Games in Interventions for Children With Attention Deficits, JMIR Serious Games (2025) — https://games.jmir.org/2025/1/e67338/
- Designing computer-based rewards with and for children with Autism Spectrum Disorder and/or Intellectual Disability, Computers in Human Behavior (ScienceDirect) — https://www.sciencedirect.com/science/article/abs/pii/S0747563217303515
- Research on the design of somatosensory interactive games for autistic children based on art therapy, Frontiers in Psychiatry (2023) — https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2023.1207023/full
- LUDIFICATION ET AUTISME — Revue de la littérature sur l'usage des jeux, FIRAH — https://www.firah.org/upload/activites-et-publications/progammes-thematiques/autisme-nouvelles-technologies/autisme-et-jeux/fr-gamification-in-autism.pdf
- Can AI-driven games enhance social skills for autistic children? A three-level meta-analysis, Frontiers in Psychology (2026) — https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1847426/full

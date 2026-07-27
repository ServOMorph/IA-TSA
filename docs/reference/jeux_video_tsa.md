# Jeux numériques et TSA — synthèse de la littérature

**Date** : 2026-07-27
**Objet** : rassembler ce que dit la recherche sur les jeux informatiques destinés aux enfants TSA, en vue de concevoir un jeu jouable à deux (adulte + jeune) à difficulté progressive.
**Périmètre** : recherche web ponctuelle (juillet 2026), non exhaustive, non revue par les pairs. Ne remplace pas une revue systématique.

## 1. Ce qui est établi

### Les jeux sérieux produisent des effets mesurés, sur des cibles étroites
Une revue systématique de 9 interventions (Emo Game, Zirkus Empathico, Mind Reading, JeStiMuLe, Secret Agent Society, SAGA, FaceSay, Play Emotion Detectives, IVRS) rapporte que 100 % des études observent une amélioration significative sur au moins un construit lié aux compétences sociales, et 85 % sur des compétences sociales larges. Domaines touchés : reconnaissance et encodage des émotions, régulation émotionnelle, direction du regard, attention conjointe, comportements sociaux.

### Mécaniques retrouvées dans les jeux efficaces
- Indices visuels explicites et personnages à état lisible
- Niveaux de difficulté progressifs
- Feedback interactif immédiat (succès / erreur signalés distinctement)
- Participation de l'accompagnant prévue dans le dispositif, pas subie
- Scénarios sociaux incarnés (avatar)
- Éléments multisensoriels en environnement immersif

### Coopération > compétition
Les formats collaboratifs sont plus efficaces que les formats compétitifs. Imposer la collaboration augmente la négociation et la coordination chez les personnes TSA. Les jeux à tour de rôle enseignent la réciprocité ; les jeux multijoueurs construisent naturellement l'attention conjointe, les joueurs imitant les comportements de jeu du partenaire.

### Rôle de l'adulte
Un étayage initial est déterminant : modelage du comportement attendu, incitation (prompting), renforcement, démonstration. Mais la conception doit prévoir la réduction progressive de la dépendance à l'adulte.

### Personnalisation
Profils hétérogènes : l'adaptation au rythme et au profil de chaque enfant n'est pas un confort, c'est une condition d'efficacité. Les intérêts restreints sont un levier — les jeux qui reflètent l'intérêt spécifique de l'enfant obtiennent un meilleur engagement (principe des Power Cards).

### Sensorialité
Réglages obligatoires : luminosité, palette de couleurs, volume, présence ou absence de musique de fond. La surcharge sensorielle dégrade l'engagement avant même que le contenu pédagogique n'entre en jeu.

## 2. Ce qui est fragile — à ne pas surestimer

La revue critique de Walsh, Linehan & Ryan (2025, *Autism*) tempère fortement l'optimisme des revues précédentes :

- **Définition floue des cibles** : absence de spécificité dans la définition et la justification des compétences choisies ; beaucoup d'études ne motivent pas leur choix d'intervention.
- **Mesures hétérogènes** : discordance de rigueur dans la mesure des résultats ; mesures pré/post souvent faibles, ce qui compromet l'attribution causale.
- **Transfert non démontré** : rien n'établit clairement que ce qui est acquis dans le jeu se transfère à la vie réelle.
- **Biais méthodologique élevé** : petits échantillons (10 à 42 participants), durées d'intervention très variables (4 à 40 semaines), suivis rares, tranches d'âge < 5 ans et > 12 ans peu couvertes.
- **Question de fond (neurodiversité)** : ces interventions servent-elles l'intérêt des personnes autistes ou imposent-elles des normes neurotypiques ? Les auteurs recommandent d'inclure les voix autistes plus tôt et plus centralement dans la conception.

**Conséquence pour ce projet** : un jeu maison ne doit pas être présenté comme une intervention validée. Il est un support d'interaction pour l'accompagnant. La cible comportementale doit être nommée explicitement avant de coder, et le retour terrain reste la seule mesure disponible ici.

## 3. Implications de conception retenues pour IA-TSA

| Principe issu de la littérature | Traduction concrète |
|---|---|
| Coopération plutôt que compétition | Objectif commun adulte + jeune, aucun score opposé, aucune défaite |
| Tour de rôle explicite | Le tour courant est visible en permanence à l'écran, jamais implicite |
| Attention conjointe | Le jeu impose un point de regard partagé (une seule zone active à la fois) |
| Difficulté progressive | Palier suivant déclenché manuellement par l'adulte, ou automatiquement sur un seuil de réussite, jamais par un timer |
| Feedback immédiat et distinct | Réaction < 100 ms, succès et non-succès visuellement différenciés sans connotation d'échec |
| Pas d'échec punitif | Erreur = absence d'effet ou reprise neutre, jamais buzzer / croix rouge / perte |
| Prévisibilité | Mapping action → effet fixe, pas d'aléatoire visible, pas d'animation autonome |
| Réglages sensoriels | Reprendre le socle existant : son, intensité, taille, mode calme |
| Cible nommée | Chaque jeu documente la compétence visée et pourquoi elle a été choisie |

Ces principes sont compatibles avec les décisions déjà prises dans [analyse_activite_cause_effet.md](analyses/analyse_activite_cause_effet.md) : prévisibilité, mapping fixe, vocabulaire d'interaction restreint.

## 4. Angle mort identifié

Aucune des activités actuelles du projet (cause-effet, choix à deux, timer, écris et écoute) n'est **dyadique** : elles sont toutes conçues pour un usage solitaire piloté par l'adulte. Or c'est précisément le tour de rôle et l'attention conjointe qui concentrent le soutien empirique le plus cohérent. Un jeu à deux joueurs sur le même clavier comble ce manque sans changer de stack.

## Sources

- Serious Games for Developing Social Skills in Children and Adolescents with Autism Spectrum Disorder: A Systematic Review, PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC10931397/
- Walsh O., Linehan C., Ryan C. (2025), Is there evidence that playing games promotes social skills training for autistic children and youth?, *Autism* — https://journals.sagepub.com/doi/10.1177/13623613241277309
- The Use of Analog and Digital Games for Autism Interventions, Frontiers in Psychology — https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.669734/full
- Design and Iterative Development of Serious Exergames for Children With Autism Spectrum Disorder, JMIR Serious Games (2026) — https://games.jmir.org/2026/1/e77727
- Cortical activation during cooperative joint actions and competition in children with and without an autism spectrum condition: an fNIRS study, PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC8956636/
- GOLIAH: A Gaming Platform for Home-Based Intervention in Autism – Principles and Design, PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC4848303/
- Pictogram room augmented reality technology games improve body knowledge, imitation, and joint attention skills in autistic children with intellectual disability, Scientific Reports (2025) — https://www.nature.com/articles/s41598-025-19085-5
- Impact of a serious games-based adaptive learning environment on developing communication skills and motivation among autistic children, Education and Information Technologies (2025) — https://link.springer.com/article/10.1007/s10639-025-13728-w
- The effect of game-based interventions on children and adolescents with autism spectrum disorder: A systematic review and meta-analysis, PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC12006128/
- Ludification et autisme — revue de la littérature sur l'usage des jeux, FIRAH — https://www.firah.org/upload/activites-et-publications/progammes-thematiques/autisme-nouvelles-technologies/autisme-et-jeux/fr-gamification-in-autism.pdf

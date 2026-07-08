# Analyse — Pistes d'amélioration de l'activité cause-effet à la lumière de la littérature

**Date** : 2026-07-08
**Objet** : évaluer, à partir de la littérature scientifique sur l'autisme, trois pistes d'amélioration proposées pour l'activité "Touche → ça réagit" (cause-effet), suite au premier retour terrain enregistré.

## Contexte

L'activité cause-effet ([UI/static/js/cause-effet.js](../../UI/static/js/cause-effet.js)) associe toute action de l'utilisateur (clic, appui clavier) à une réaction visuelle et sonore unique et constante. Le premier retour terrain (2026-07-08) rapporte un engagement qualifié de "neutre" : environ 2 minutes d'appuis continus sur la barre espace, une pause, puis 2 minutes de reprise. L'éducateur suggère trois pistes :

1. Faire évoluer la forme/couleur/taille au fur et à mesure des appuis (progression).
2. Différencier l'effet selon la touche pressée (espace vs Entrée vs Ctrl).
3. Mesurer objectivement la fréquence d'appui plutôt que de se limiter à une évaluation qualitative ("neutre").

Chaque piste a été confrontée à la littérature disponible sur l'habituation sensorielle, la conception logicielle pour enfants TSA, et la mesure des comportements répétitifs.

## Piste 1 — Variation progressive du stimulus après appuis répétés

**Hypothèse sous-jacente** : le désengagement observé (pause après 2 minutes) traduirait une lassitude par habituation au stimulus répété, qu'une variation progressive (formes, couleurs) permettrait de contrer.

**Ce que dit la littérature** : cette hypothèse ne correspond pas au profil d'habituation généralement documenté chez les enfants autistes. Plusieurs études en neuro-imagerie montrent que les enfants TSA présentent une habituation neuronale plus lente, voire absente, aux stimuli répétés — le cerveau ne réduit pas sa réponse comme chez les enfants neurotypiques, avec une activité qui reste élevée dans la durée (Distinct Patterns of Neural Habituation and Generalization in Youth With Autism, PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC6889004/ ; Habituation and autism — why sensory adaptation fails — https://neurodiversity.directory/habituation-autism-sensory-experience/).

Une étude sur l'attention visuelle face à des stimuli répétés versus nouveaux montre par ailleurs que les enfants TSA peuvent présenter une diminution d'attention aux deux types de stimuli (répété et nouveau) au fil du temps, contrairement aux enfants neurotypiques qui réorientent leur attention vers la nouveauté (What is the Effect of Stimulus Complexity on Attention to Repeating and Changing Information in Autism?, PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC8813872/). Cela suggère que le désengagement n'est pas nécessairement résolu par l'introduction de nouveauté.

Par ailleurs, les guides de conception logicielle pour enfants TSA recommandent des interactions prévisibles et des séquences répétées favorisant la constance et l'anticipation plutôt que la variation (Guidelines for research and design of software for children with ASD in e-health, Springer — https://link.springer.com/article/10.1007/s10209-023-01013-x).

**Conclusion** : piste faiblement soutenue par la littérature, potentiellement contre-productive si elle introduit de l'imprévisibilité. Le désengagement observé relève plus probablement d'un autre facteur (fatigue, pause sensorielle volontaire) que d'une habituation classique. **Recommandation : ne pas implémenter par défaut ; si testée, la proposer en option désactivable et évaluer son effet au cas par cas.**

## Piste 2 — Touches différenciées (Entrée, Ctrl) associées à des effets distincts

**Hypothèse sous-jacente** : des touches facilement repérables au clavier, associées chacune à un effet propre et constant, enrichiraient le vocabulaire d'interaction sans nuire à la prévisibilité.

**Ce que dit la littérature** : cette piste est la mieux alignée avec les principes de conception recommandés pour les enfants TSA. La littérature souligne l'importance d'interactions prévisibles et d'une correspondance stable entre action et réaction, réduisant l'anxiété et facilitant l'anticipation (Unlocking inclusive education: A quality assessment of software design in applications for children with autism, ScienceDirect — https://www.sciencedirect.com/science/article/pii/S0164121224002097 ; Guidelines for research and design of software for children with ASD in e-health, Springer — https://link.springer.com/article/10.1007/s10209-023-01013-x). Contrairement à la piste 1, il ne s'agit pas ici d'introduire de la variation aléatoire mais d'ajouter un mapping fixe et cohérent (touche X → effet X, toujours identique), ce qui reste conforme au principe de prévisibilité.

**Conclusion** : piste la mieux soutenue. **Recommandation : priorité haute, implémentation directe.**

## Piste 3 — Mesure objective de la fréquence d'appui (log ou seuil réglable)

**Hypothèse sous-jacente** : une mesure quantitative de la fréquence et du rythme des appuis donnerait une évaluation plus fine de l'engagement que la catégorie qualitative actuelle ("neutre").

**Ce que dit la littérature** : la persévération (comportement répétitif qui se poursuit au-delà du déclencheur initial) est un concept clinique reconnu chez les personnes TSA, mesuré classiquement par des échelles standardisées comme la Repetitive Behavior Scale-Revised (RBS-R), un questionnaire à 43 items couvrant six sous-échelles de comportements répétitifs (How to Define Perseveration in Autism Spectrum Disorder — https://www.neurodiverging.com/define-perseveration-in-autism/). La recherche montre également un lien entre variation des comportements répétitifs et contrôle inhibiteur / flexibilité cognitive (Variation in Restricted and Repetitive Behaviors and Interests Relates to Inhibitory Control and Shifting in Children with Autism Spectrum Disorder, PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC6499722/).

Aucune étude identifiée ne valide une mesure numérique de la persévération via une interface logicielle grand public — le log de fréquence d'appui serait donc un indicateur exploratoire, sans équivalence démontrée avec les échelles cliniques existantes.

**Conclusion** : piste utile comme donnée terrain complémentaire, mais à présenter comme indicateur exploratoire et non comme mesure clinique validée. **Recommandation : implémentation simple (log de fréquence dans le retour terrain), sans interprétation clinique automatisée.**

## Synthèse et priorisation

| Piste | Soutien littérature | Priorité |
|---|---|---|
| 2. Touches différenciées | Fort (prévisibilité, cohérence action-réaction) | Haute |
| 3. Log fréquence d'appui | Partiel (concept clinique existant, pas d'équivalent digital validé) | Moyenne |
| 1. Variation progressive | Faible, potentiellement contraire au profil d'habituation TSA | Basse |

## Décision

2026-07-08 : choix retenu — implémentation de la piste 2 (touches différenciées Espace / Entrée / Ctrl, chacune associée à un effet visuel et sonore distinct et constant). Pistes 1 et 3 non retenues à ce stade.

## Complément — Restriction aux 3 touches actives (Espace, Entrée, Ctrl)

**Constat** : l'implémentation initiale de la piste 2 associait un effet à Espace/Entrée/Ctrl, mais toute autre touche (hors Echap/Tab) déclenchait par défaut l'effet "Espace". Ce comportement introduit un bruit non intentionnel : l'enfant peut obtenir une réaction en pressant une touche non prévue, ce qui casse la correspondance stricte action→effet.

**Ce que dit la littérature et la documentation du projet** :
- Le document interne du projet rappelle que la prévisibilité passe par « des interfaces claires, des réactions constantes, peu de stimuli parasites » ([docs/reference/autisme_informatique.md](../autisme_informatique.md)).
- Les dispositifs d'accès alternatif (switch access) pour utilisateurs à besoins moteurs ou cognitifs recommandent de limiter le nombre d'entrées actives afin d'augmenter le contrôle et la prévisibilité de l'interaction (Alternative Access - Switches, CALL Scotland — https://www.callscotland.org.uk/information/alternative-access/switches/).
- La recherche sur le contrôle cognitif dans le TSA indique une charge cognitive et un coût attentionnel plus élevés que chez les neurotypiques pour des tâches équivalentes, ce qui plaide pour un vocabulaire d'interaction restreint et non ambigu plutôt qu'un espace de touches ouvert (Reduced Efficiency and Capacity of Cognitive Control in Autism Spectrum Disorder, PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC4713391/).
- Les ressources sur les dispositifs de communication alternative (AAC) soulignent l'intérêt de motifs moteurs cohérents et d'une charge cognitive minimisée dans la conception des interactions (What is an AAC Device and How Does it Enhance Communication?, Hopebridge — https://www.hopebridge.com/blog/what-is-an-aac-device-for-communication/).

**Décision** : 2026-07-08 — seules les touches Espace, Entrée et Ctrl déclenchent un effet ; toute autre touche est ignorée (aucune réaction produite). Le clic/tap conserve l'effet "Espace" par défaut.

## Limite de cette analyse

Cette synthèse repose sur une recherche web ponctuelle (juillet 2026), non exhaustive et non revue par les pais. Elle ne remplace pas une revue systématique. Un seul retour terrain est disponible à ce jour — les conclusions ci-dessus orientent la priorisation du développement, elles ne constituent pas une validation empirique sur le terrain de ce projet.

## Sources

- Distinct Patterns of Neural Habituation and Generalization in Youth With Autism, With and Without Sensory Over-Responsivity, PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC6889004/
- Habituation and autism — why sensory adaptation fails, Neurodiversity Directory — https://neurodiversity.directory/habituation-autism-sensory-experience/
- What is the Effect of Stimulus Complexity on Attention to Repeating and Changing Information in Autism?, PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC8813872/
- Unlocking inclusive education: A quality assessment of software design in applications for children with autism, ScienceDirect — https://www.sciencedirect.com/science/article/pii/S0164121224002097
- Guidelines for research and design of software for children with ASD in e-health, Universal Access in the Information Society (Springer) — https://link.springer.com/article/10.1007/s10209-023-01013-x
- How to Define Perseveration in Autism Spectrum Disorder, Neurodiverging — https://www.neurodiverging.com/define-perseveration-in-autism/
- Variation in Restricted and Repetitive Behaviors and Interests Relates to Inhibitory Control and Shifting in Children with Autism Spectrum Disorder, PMC — https://pmc.ncbi.nlm.nih.gov/articles/PMC6499722/

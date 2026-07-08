# Autisme (TSA) et Informatique — Document de Référence

> Document de synthèse pour le projet IA-TSA. Croise les ressources de [`docs/web/site_internet_references.md`](../web/site_internet_references.md) avec une revue d'articles web (juin 2026). Vocation : base de données de référence sur l'apport du numérique et de l'IA pour les personnes autistes en contexte éducatif.
>
> **Avertissement méthodologique** : les affirmations sont sourcées. Les distinctions fait / hypothèse / résultat préliminaire sont signalées. Les chiffres proviennent des sources citées et ne sont pas extrapolés. Aucune donnée concernant des enfants ou un établissement réel n'est présente (conformité RGPD).

---

## 1. Comprendre le TSA pour cadrer l'usage du numérique

Le **trouble du spectre de l'autisme (TSA)** est un trouble neurodéveloppemental caractérisé par des particularités dans deux domaines : la communication / interactions sociales, et les comportements / intérêts restreints et répétitifs. C'est un **spectre** : les profils vont de la personne non verbale avec besoin de soutien important à la personne autonome verbalement.

Caractéristiques fréquentes qui orientent le choix des outils :
- **Pensée visuelle** : traitement de l'information souvent plus efficace en visuel qu'en auditif.
- **Besoin de prévisibilité et de structure** : l'imprévu génère anxiété et troubles du comportement.
- **Particularités sensorielles** : hyper- ou hypo-sensibilité (son, lumière, mouvement) → risque de surcharge.
- **Difficultés de communication** : jusqu'à environ un tiers des personnes autistes sont non verbales ou peu verbales.

**Principe clé** : l'outil numérique n'est pas une fin mais un support d'intervention développementale ou comportementale. La [HAS rappelle (2026)](https://www.has-sante.fr/jcms/p_3859897/fr/autisme-les-nouvelles-recommandations-pour-le-nourrisson-l-enfant-et-l-adolescent) que la priorité va aux interventions développementales et comportementales fondées sur l'évaluation du fonctionnement de la personne.

---

## 2. Pourquoi le numérique est adapté au TSA

Plusieurs sources convergent sur les raisons structurelles de l'efficacité du numérique :

- **Prévisibilité et absence de jugement** : une machine réagit toujours de la même façon, sans la charge sociale d'un visage humain. Les enfants autistes préfèrent souvent les technologies car elles sont « sans surprise, prévisibles, structurées et exemptes de jugement » ([sites de référence du projet](../web/site_internet_references.md)).
- **Support visuel natif** : tablettes et écrans matérialisent le temps, les étapes et les choix — ce qui correspond au mode de traitement visuel.
- **Réduction de la surcharge cognitive** : les outils de planification numérique permettent de séquencer et d'alléger la charge mentale ([Réseau Canopé](https://www.reseau-canope.fr/agence-des-usages/accompagner-les-personnes-avec-autisme-via-un-agenda-numerique.html)).
- **Personnalisation** : les applications adaptatives ajustent la difficulté au rythme de l'enfant en temps réel.

> **Nuance honnête** : « préférence pour la machine » est un constat clinique fréquent, pas une règle universelle. Certains profils se désengagent face à l'écran. À évaluer cas par cas.

---

## 3. Catégories d'usage de l'IA et du numérique

### 3.1 Détection et aide au diagnostic

L'IA progresse sur le **dépistage précoce**, domaine où l'accès au diagnostic est lent.

- **Canvas Dx (Cognoa)** — premier dispositif de diagnostic d'aide basé sur l'IA **autorisé par la FDA** pour les enfants de 18 à 72 mois. Combine trois sources : questionnaire parental (5 min), deux vidéos courtes de l'enfant en jeu, et un questionnaire clinicien (10 min), agrégés par un algorithme de machine learning ([Cognoa](https://cognoa.com/clinical-research/), [Fierce Biotech](https://www.fiercebiotech.com/medtech/cognoa-s-ai-app-for-diagnosing-childhood-autism-gets-fda-green-light)). Une [analyse en conditions réelles (Nature, 2025)](https://www.nature.com/articles/s41598-025-15575-8) évalue ses performances effectives.
- **Détection par le mouvement** : des systèmes analysent les mouvements (réalité virtuelle ou capteur type Kinect) pour repérer des marqueurs du TSA, avec des taux de précision rapportés **supérieurs à 85 %** ([Univadis](https://www.univadis.fr/viewarticle/des-chercheurs-d%C3%A9veloppent-nouveau-syst%C3%A8me-2025a1000b4j)). En France, des prototypes ludiques font reproduire des mouvements de danse face à un écran ([Scolinfo](https://www.scolinfo.net/lia-est-desormait-capable-de-detecter-les-enfant-atteind-dautisme-une-premiere-en-europe/)).
- **Analyse vidéo** : l'[UNIGE / Centre Synapsy](https://www.unige.ch/medecine/synapsycentre/fr/actus/la-video-pour-une-detection-precoce-de-lautisme) travaille sur la vidéo comme support de détection précoce.

> **Statut** : la détection IA est un **outil d'aide à la décision**, pas un diagnostic autonome. Le diagnostic reste un acte clinique pluridisciplinaire.

### 3.2 Communication — CAA (Communication Alternative et Augmentée)

Pour les profils **non verbaux ou peu verbaux**, l'enjeu central est de donner accès à l'expression.

- **Principe CAA** : ensemble de moyens remplaçant le langage oral absent (alternatif) ou complétant un langage insuffisant (augmenté). Couramment utilisée avec le TSA ([Hop'Toys](https://www.bloghoptoys.fr/la-communication-alternative-augmentee), [APF Infos Handicaps](https://infos-handicaps.apf-francehandicap.org/selection-ressources-outils-facile-lire-comprendre-falc-communication-alternative-amelioree-caa)).
- **Pictogrammes** : une succession de pictogrammes associés à des mots permet de construire des phrases dans un code adapté (besoins, émotions, idées).
- **Outils tablette** : TD Snap, Pictalk, Agenda CAA, applications de PECS numérisé. Le CHU de Nantes déploie des outils CAA en milieu hospitalier ([Santé Mentale, 2026](https://www.santementale.fr/2026/03/autisme-la-communication-alternative-et-amelioree-renforcee/)).
- **Transition lettre-board → iPad** documentée dans la littérature ([NCBI, étude de cas](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11148795/)).

### 3.3 Compétences sociales — robots et IA

Les **robots sociaux** servent de médiateur d'apprentissage prévisible.

- **Kaspar** (Université du Hertfordshire, 2005) : robot humanoïde conçu pour les enfants autistes. Utilisé dans des études longitudinales auprès d'environ **170 enfants**, sur plusieurs semaines à plusieurs mois, à l'école et à domicile. Outil d'apprentissage sûr et prévisible des interactions sociales ([Cairn / ENF2](https://shs.cairn.info/article/ENF2_181_0091/pdf?lang=fr), [MBA MCI](https://mbamci.com/kaspar-le-robot-humanoide-social/)).
- **NAO** : interventions à base comportementale rapportées comme efficaces pour le langage et la communication, avec une **efficacité comparable à celle de thérapeutes humains** dans certaines études ; le design et le langage corporel favoriseraient le contact visuel ([UQAC, étude de cas](https://constellation.uqac.ca/id/eprint/9943/), [arXiv](https://arxiv.org/pdf/2407.12014)).
- **QTrobot (LuxAI)** : jeux sur tablette pour la reconnaissance et la dénomination des émotions. Modèle économique : matériel + abonnement logiciel mensuel ([référence projet](../web/site_internet_references.md)).

> **Nuance honnête** : « efficacité comparable aux thérapeutes » provient d'études de cas ou d'échantillons limités. Résultats **prometteurs mais non généralisables**. Le robot est un médiateur, pas un substitut à l'accompagnement humain.

### 3.4 Apprentissage et personnalisation

- **Apps adaptatives** : Otsimo (basé ABA), Auticiel (10 applications, 500+ activités évolutives), Curio ([QuelBonPlan](https://www.quelbonplan.fr/blogs/articles/10-applications-pour-les-enfants-autistes-asperger-ou-ted)).
- **Outils reconnus Éducation nationale** : Mathia, Lalilo, Navi, Adaptiv'Math (parcours pédagogiques sur mesure) ; MIA Seconde (chatbot simplifiant les consignes — nécessite vérification humaine).

### 3.5 Structuration du temps et de l'espace

Composante essentielle de l'intervention selon la HAS : rendre les changements prévisibles, diminuer les troubles du comportement.

- **Agendas numériques / emplois du temps visuels** : savoir ce qui se passe avant/après une activité ; matérialiser la durée via des supports visuels d'attente ([HAS](https://www.has-sante.fr/jcms/p_3859897/fr/autisme-les-nouvelles-recommandations-pour-le-nourrisson-l-enfant-et-l-adolescent)).

### 3.6 Activités cause-effet / sensorielles (profils à besoins importants)

Pour TSA non verbal avec troubles moteurs sévères — activités navigateur, gratuites, sans IA. Détail dans [`site_internet_references.md`](../web/site_internet_references.md#-activités-pratiques-en-salle-informatique-cause-effet--sensoriel) : Shiny Learning, SpecialBites, HelpKidzLearn, WonderTree, Little Miss Kim's Class.

- **Principe** : l'accompagnant pilote, l'apprenant indique un choix (regard, geste, vocalise) → action confirmée → réaction visuelle/sonore immédiate = lien causal. Donne un contrôle décisionnel même sans motricité fine.

---

## 4. Bonnes pratiques et précautions

| Principe | Mise en œuvre |
|----------|---------------|
| **Éviter la surstimulation** | Couper le son / réduire la complexité dès les premiers signes de retrait ou d'agitation. La HAS recommande de calibrer l'intensité pour éviter sous- comme sur-stimulation. |
| **Outil au service de l'objectif** | Le numérique soutient une intervention développementale/comportementale, il ne la remplace pas. |
| **Médiation humaine** | Chatbots et traductions simplifiées (MIA Seconde) **nécessitent une vérification humaine**. |
| **Prévisibilité** | Privilégier des interfaces claires, des réactions constantes, peu de stimuli parasites. |
| **Évaluation individuelle** | Tester, observer la réaction réelle, ajuster. Ce qui fonctionne pour un profil peut échouer pour un autre. |

---

## 5. Cadre réglementaire et éthique

- **HAS** : recommandations de bonne pratique actualisées (2026) — priorité aux interventions développementales et comportementales, évaluation du fonctionnement comme socle ([HAS — travaux autisme](https://www.has-sante.fr/jcms/c_2829216/fr/autisme-travaux-de-la-has)).
- **RGPD** : les outils traitant des données comportementales, vidéos ou de santé d'enfants relèvent de données sensibles. Vigilance sur l'hébergement, le consentement et la finalité. **Aucune donnée d'enfant identifiable ne doit transiter par un service non maîtrisé.**
- **IA et diagnostic** : un outil IA ne pose pas de diagnostic ; il assiste un professionnel. Risque de faux positifs/négatifs à intégrer.

---

## 6. Synthèse — quel outil pour quel besoin

| Besoin | Pistes |
|--------|--------|
| Dépistage / orientation | Canvas Dx, détection par mouvement, analyse vidéo (toujours validé par un clinicien) |
| Communication non verbale | CAA : pictogrammes, TD Snap, Pictalk, PECS numérique |
| Compétences sociales / émotions | Robots (Kaspar, NAO, QTrobot), apps de reconnaissance d'émotions |
| Apprentissages scolaires | Mathia, Lalilo, Adaptiv'Math, Otsimo, Auticiel |
| Structuration / anxiété | Agendas numériques, emplois du temps visuels, timers visuels |
| Profils moteurs sévères | Jeux cause-effet / sensoriels en navigateur, accès switch / eye-gaze |

---

## 7. Sources principales

- [HAS — Nouvelles recommandations autisme (2026)](https://www.has-sante.fr/jcms/p_3859897/fr/autisme-les-nouvelles-recommandations-pour-le-nourrisson-l-enfant-et-l-adolescent) · [Travaux HAS](https://www.has-sante.fr/jcms/c_2829216/fr/autisme-travaux-de-la-has)
- [Cognoa — recherche clinique Canvas Dx](https://cognoa.com/clinical-research/) · [Nature (2025) — performances réelles](https://www.nature.com/articles/s41598-025-15575-8) · [Fierce Biotech — FDA](https://www.fiercebiotech.com/medtech/cognoa-s-ai-app-for-diagnosing-childhood-autism-gets-fda-green-light)
- [Univadis — détection précoce IA](https://www.univadis.fr/viewarticle/des-chercheurs-d%C3%A9veloppent-nouveau-syst%C3%A8me-2025a1000b4j) · [Scolinfo](https://www.scolinfo.net/lia-est-desormait-capable-de-detecter-les-enfant-atteind-dautisme-une-premiere-en-europe/) · [UNIGE / Synapsy](https://www.unige.ch/medecine/synapsycentre/fr/actus/la-video-pour-une-detection-precoce-de-lautisme)
- [Cairn — Kaspar (ENF2)](https://shs.cairn.info/article/ENF2_181_0091/pdf?lang=fr) · [MBA MCI — Kaspar](https://mbamci.com/kaspar-le-robot-humanoide-social/) · [UQAC — NAO étude de cas](https://constellation.uqac.ca/id/eprint/9943/) · [arXiv — NAO en classe](https://arxiv.org/pdf/2407.12014)
- [Hop'Toys — CAA](https://www.bloghoptoys.fr/la-communication-alternative-augmentee) · [APF Infos Handicaps — FALC/CAA](https://infos-handicaps.apf-francehandicap.org/selection-ressources-outils-facile-lire-comprendre-falc-communication-alternative-amelioree-caa) · [Santé Mentale — CHU Nantes](https://www.santementale.fr/2026/03/autisme-la-communication-alternative-et-amelioree-renforcee/) · [NCBI — letter board vers iPad](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11148795/)
- [Réseau Canopé — agenda numérique](https://www.reseau-canope.fr/agence-des-usages/accompagner-les-personnes-avec-autisme-via-un-agenda-numerique.html) · [QuelBonPlan — apps 2025](https://www.quelbonplan.fr/blogs/articles/10-applications-pour-les-enfants-autistes-asperger-ou-ted)
- Ressources internes du projet : [`docs/web/site_internet_references.md`](../web/site_internet_references.md)

---

*Document créé le 19 juin 2026 pour le projet IA-TSA. À actualiser au fil des retours terrain et de l'évolution des outils.*

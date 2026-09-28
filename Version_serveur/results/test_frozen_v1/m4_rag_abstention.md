# Reponses du prototype Inalco + vLLM

## q002. Quelles sont les principales formations diplômantes proposées par l'Inalco ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `3575 caractères`

**Reponse :**

Les principales formations diplômantes proposées par l'Inalco incluent :

- **Licence**
- **Master**
- **Doctorat**
- **Diplôme d'établissement** (diplôme d’initiation, diplôme de langue, diplôme intensif, diplôme de civilisation, diplôme de langue et civilisation, etc.)
- **DU H2M, DU Passerelle, DIU Islamologie**
- **Dipl. initiation, intensif, de langue et/ou civilisation, DPCILO, certificats**

Pour plus de détails, vous pouvez consulter la page officielle des formations diplômantes de l'Inalco : [Formations diplômantes](https://www.inalco.fr/formations-diplomantes).

Sources :
- [Diplômes d'établissement](https://www.inalco.fr/formations/diplomes-detablissement)
- [Candidater à un cursus diplômant](https://www.inalco.fr/candidater-un-cursus-diplomant)
- [Formations diplômantes](https://www.inalco.fr/formations-diplomantes)
- [Nos formations](https://www.inalco.fr/nos-formations)

**Sources recuperees :**

- [1] Diplômes d'établissement / Diplômes d'établissement (pages=n/a-n/a, score=0.8789, semantic=0.8789, dans_contexte=oui)  https://www.inalco.fr/formations/diplomes-detablissement
- [2] Candidater à un cursus diplômant / 1. Choisir sa formation (pages=n/a-n/a, score=0.8776, semantic=0.8776, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [3] Formations diplômantes / Formations diplômantes (pages=n/a-n/a, score=0.8751, semantic=0.8751, dans_contexte=oui)  https://www.inalco.fr/formations-diplomantes
- [4] Diplômes d'établissement / Nos formations proposées en diplômes d'établissement (pages=n/a-n/a, score=0.865, semantic=0.865, dans_contexte=oui)  https://www.inalco.fr/formations/diplomes-detablissement
- [5] Nos formations / Formations diplômantes (pages=n/a-n/a, score=0.8648, semantic=0.8648, dans_contexte=oui)  https://www.inalco.fr/nos-formations

**Faits de référence (non transmis au modèle) :**

- Les principales formations diplômantes de l'Inalco comprennent les licences, les masters et les doctorats
- L'établissement propose également des diplômes universitaires et des diplômes d'établissement

## q003. Quelle est la différence entre une licence LLCER et un diplôme d'établissement ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Licence LLCER à parcours professionnalisant / Les parcours (pages=n/a-n/a, score=0.8481, semantic=0.8481, dans_contexte=non)  https://www.inalco.fr/formations/licence-llcer-parcours-professionnalisant
- [2] Licences LLCER - Brochures / Etudes hébraïques et juives (pages=n/a-n/a, score=0.848, semantic=0.848, dans_contexte=non)  https://www.inalco.fr/licences-llcer-brochures
- [3] Licence LLCER à parcours bilangue / Licence LLCER à parcours bilangue (pages=n/a-n/a, score=0.8447, semantic=0.8447, dans_contexte=non)  https://www.inalco.fr/formations/licence-llcer-parcours-bilangue
- [4] Licences LLCER - Brochures / Etudes arabes (pages=n/a-n/a, score=0.8447, semantic=0.8447, dans_contexte=non)  https://www.inalco.fr/licences-llcer-brochures
- [5] Conventions de stage / Mon référent doit-il être de mon propre département ? (pages=n/a-n/a, score=0.8443, semantic=0.8443, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html

**Faits de référence (non transmis au modèle) :**

- La licence LLCER est un diplôme national organisé en trois années
- Elle associe l'étude d'une langue, de sa civilisation et des enseignements disciplinaires
- Les diplômes d'établissement de l'Inalco sont principalement centrés sur une langue, sa civilisation ou une aire régionale
- Dans ces cursus d'établissement, chaque année peut conduire à un diplôme propre à l'Inalco

## q005. Puis-je commencer une langue à l'Inalco sans l'avoir étudiée auparavant ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `clarify`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] FAQ Admission en Master / DOIS-JE OBLIGATOIREMENT CONNAITRE UNE LANGUE ORIENTALE DE L’INALCO ? (pages=n/a-n/a, score=0.8594, semantic=0.8594, dans_contexte=non)  https://www.inalco.fr/faq-admission-en-master
- [2] Étudiants internationaux à l'Inalco / **Cours et conditions linguistiques** (pages=n/a-n/a, score=0.8584, semantic=0.8584, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/international/venir-etudier-a-l-inalco.html
- [3] FAQ Admission en Master / Une question sur l'admission en Master à l'Inalco? (pages=n/a-n/a, score=0.8584, semantic=0.8584, dans_contexte=non)  https://www.inalco.fr/faq-admission-en-master
- [4] Master TI - Traduction spécialisée / FAQ (pages=n/a-n/a, score=0.8582, semantic=0.8582, dans_contexte=non)  https://www.inalco.fr/formations/master-ti-traduction-specialisee
- [5] Master TI - Traduction spécialisée / FAQ (pages=n/a-n/a, score=0.8533, semantic=0.8533, dans_contexte=non)  https://www.inalco.fr/formations/master-ti-traduction-specialisee

## q006. Quels sont les prérequis pour entrer en première année de licence LLCER ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5026 caractères`

**Reponse :**

Pour entrer en première année de licence LLCER à parcours bilangue à l'Inalco, il est nécessaire de suivre les modalités de candidature spécifiques à cette formation. Les préinscriptions pour l'année 2026-2027 seront ouvertes du 16 février au 15 avril 2026. Vous pouvez consulter les modalités de candidature en cliquant sur le bouton "Candidater" ou en vous référant au document "Livret Licence LLCER 2026-2027" disponible sur la page officielle.

Sources :
- [Licence LLCER à parcours bilangue](https://www.inalco.fr/formations/licence-llcer-parcours-bilangue)

**Sources recuperees :**

- [1] Licence LLCER à parcours bilangue / Licence LLCER à parcours bilangue (pages=n/a-n/a, score=0.8759, semantic=0.8759, dans_contexte=oui)  https://www.inalco.fr/formations/licence-llcer-parcours-bilangue
- [2] Licence LLCER à parcours bilangue / Licence LLCER à parcours bilangue (pages=n/a-n/a, score=0.8724, semantic=0.8724, dans_contexte=oui)  https://www.inalco.fr/formations/licence-llcer-parcours-bilangue
- [3] Licence LLCER à parcours professionnalisant / Les parcours (pages=n/a-n/a, score=0.8711, semantic=0.8711, dans_contexte=oui)  https://www.inalco.fr/formations/licence-llcer-parcours-professionnalisant
- [4] Licence LLCER à parcours bilangue / Documentation et complément d'information (pages=n/a-n/a, score=0.864, semantic=0.864, dans_contexte=oui)  https://www.inalco.fr/formations/licence-llcer-parcours-bilangue
- [5] Licences LLCER à parcours thématiques et disciplinaires / Organisation des parcours thématiques et disciplinaires (pages=n/a-n/a, score=0.8639, semantic=0.8639, dans_contexte=non)  https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires

**Faits de référence (non transmis au modèle) :**

- Une candidature en première année de licence s'effectue par Parcoursup
- Le candidat doit consulter la fiche Parcoursup et la brochure de la formation visée
- Certaines langues peuvent prévoir des indications de niveau ou des modalités particulières précisées dans leur fiche de formation

## q008. Dois-je obligatoirement passer par Parcoursup pour entrer en licence ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Candidatures / CANDIDATER EN LICENCE 1 (L.AS INCLUSE) (pages=n/a-n/a, score=0.8504, semantic=0.8504, dans_contexte=non)  https://www.inalco.fr/candidatures
- [2] Inscriptions administratives / Procédure d'inscription administrative (pages=n/a-n/a, score=0.8447, semantic=0.8447, dans_contexte=non)  https://www.inalco.fr/inscriptions-administratives
- [3] Conventions de stage / Puis-je faire un stage non obligatoire dans le cadre d’un diplôme de Licence LLCER ? (pages=n/a-n/a, score=0.8407, semantic=0.8407, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html
- [4] Parcours L1+ / Présentation et spécificités du parcours L1+ (pages=n/a-n/a, score=0.8398, semantic=0.8398, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/accompagnement-vers-la-reussite/parcours-l1.html
- [5] Candidatures / Candidatures (pages=n/a-n/a, score=0.8388, semantic=0.8388, dans_contexte=non)  https://www.inalco.fr/candidatures

**Faits de référence (non transmis au modèle) :**

- L'accès en première année de licence à l'Inalco passe par Parcoursup
- Cette procédure concerne également une nouvelle candidature en première année dans le cadre d'une réorientation annuelle

## q009. Quelle procédure de candidature dois-je suivre selon ma nationalité et mon pays de résidence ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Candidater à un cursus diplômant / 2. Candidater (pages=n/a-n/a, score=0.863, semantic=0.863, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [2] Candidatures / Candidatures (pages=n/a-n/a, score=0.8598, semantic=0.8598, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/candidatures.html
- [3] Candidater à un cursus diplômant / 2. Candidater (pages=n/a-n/a, score=0.8577, semantic=0.8577, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [4] Candidater à un cursus diplômant / Candidats européens et candidats extra-européens étudiant actuellement dans une université française ou européenne, ou résident dans un pays ne relevant pas de la procédure Études en France (pages=n/a-n/a, score=0.8577, semantic=0.8577, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [5] Candidater à un cursus diplômant / 2. Candidater (pages=n/a-n/a, score=0.8515, semantic=0.8515, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant

**Faits de référence (non transmis au modèle) :**

- La procédure de candidature dépend de la nationalité, du pays de résidence et du diplôme de fin d'études secondaires
- Les candidats relevant de la procédure Études en France doivent candidater sur cette plateforme
- Les candidats résidant à l'étranger dans un pays ne relevant pas d'Études en France peuvent relever de la Demande d'Admission Préalable

## q010. Puis-je candidater avec un diplôme de fin d'études secondaires obtenu à l'étranger ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `True`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Pour quelle formation et quel niveau d'entrée souhaitez-vous connaître les dates de candidature ?

**Sources recuperees :**


**Faits de référence (non transmis au modèle) :**

- Un candidat titulaire d'un diplôme de fin d'études secondaires obtenu à l'étranger peut candidater
- La procédure à suivre dépend notamment du pays de résidence et de l'application ou non de la procédure Études en France
- Les candidats résidant à l'étranger hors procédure Études en France doivent suivre la procédure DAP dossier blanc lorsque celle-ci s'applique

## q012. Quels masters de l'Inalco sont accessibles sur la plateforme Mon Master ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5028 caractères`

**Reponse :**

Les masters de l'Inalco accessibles sur la plateforme Mon Master sont les suivants :
- LLCER (Langues, Littératures et Civilisations Étrangères et Régionales)
- Didactique des langues
- Langues et sociétés
- Management des langues et des cultures
- Traductologie
- Études comparées des littératures et des cultures
- Études comparées des littératures et des cultures
- Études comparées des littératures et des cultures
- Études comparées des littératures et des cultures

Pour plus de détails, vous pouvez consulter la page officielle des candidatures : [Candidatures](https://www.inalco.fr/candidatures).

Sources :
- [FAQ Admission en Master](https://www.inalco.fr/faq-admission-en-master)
- [Candidatures](https://www.inalco.fr/candidatures)

**Sources recuperees :**

- [1] FAQ Admission en Master / COMMENT CHOISIR MON MASTER A L’INALCO ? (pages=n/a-n/a, score=0.8811, semantic=0.8811, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [2] FAQ Admission en Master / À quelle date les résultats d’admission sont-ils disponibles ? (pages=n/a-n/a, score=0.8736, semantic=0.8736, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [3] FAQ Admission en Master / Une question sur la plateforme MonMaster? (pages=n/a-n/a, score=0.8735, semantic=0.8735, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [4] Candidatures / Candidatures (pages=n/a-n/a, score=0.8687, semantic=0.8687, dans_contexte=oui)  https://www.inalco.fr/candidatures
- [5] FAQ Admission en Master / Y a-t-il des examens/concours d’entrée pour certains Masters ? (pages=n/a-n/a, score=0.867, semantic=0.867, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master

**Faits de référence (non transmis au modèle) :**

- Pour la campagne 2026, Mon Master concerne notamment les M1 LLCER, Didactique des langues, Langues et sociétés, Management et commerce international, Relations internationales, Sciences du langage, Traitement automatique des langues, Traduction littéraire, Traduction spécialisée et Médiation et interprétation en service public

## q014. Puis-je candidater en master avec une licence obtenue dans une autre université ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] FAQ Admission en Master / J’ai déjà un Master. Puis-je candidater pour un nouveau Master ? (pages=n/a-n/a, score=0.8612, semantic=0.8612, dans_contexte=non)  https://www.inalco.fr/faq-admission-en-master
- [2] FAQ Admission en Master / EST-IL POSSIBLE DE CANDIDATER EN ETANT DIPLOME D’UNE AUTRE UNIVERSITE QUE L’INALCO ? (pages=n/a-n/a, score=0.8574, semantic=0.8574, dans_contexte=non)  https://www.inalco.fr/faq-admission-en-master
- [3] FAQ Admission en Master / Puis-je candidater et suivre 2 Masters en parallèle ? (pages=n/a-n/a, score=0.8562, semantic=0.8562, dans_contexte=non)  https://www.inalco.fr/faq-admission-en-master
- [4] FAQ Admission en Master / QUELLE EST LA DIFFERENCE ENTRE UN MASTER PRO, UN MASTER RECHERCHE ET LES AUTRES MENTIONS ? (pages=n/a-n/a, score=0.8504, semantic=0.8504, dans_contexte=non)  https://www.inalco.fr/faq-admission-en-master
- [5] FAQ Admission en Master / Une question sur la plateforme MonMaster? (pages=n/a-n/a, score=0.8503, semantic=0.8503, dans_contexte=non)  https://www.inalco.fr/faq-admission-en-master

**Faits de référence (non transmis au modèle) :**

- Il est possible de candidater avec une licence obtenue dans une autre université
- La licence doit attester d'études d'une langue orientale et d'une formation disciplinaire cohérente avec le master demandé
- Un diplôme obtenu à l'étranger doit être traduit en français par un traducteur assermenté

## q015. Comment candidater directement en deuxième année de master ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5707 caractères`

**Reponse :**

Pour candidater directement en deuxième année de master à l'Inalco, vous devez vérifier les conditions spécifiques de chaque master. Certains masters offrent un nombre restreint de places accessibles directement au niveau M2 pour des étudiants de niveau M1 minimum. Les conditions et modalités d’accès sont indiquées dans les brochures correspondantes.

Pour plus d'informations, consultez la page officielle des candidatures : [Candidatures](https://www.inalco.fr/candidatures).

Sources :
- [Candidatures](https://www.inalco.fr/candidatures)
- [FAQ Admission en Master](https://www.inalco.fr/faq-admission-en-master)

**Sources recuperees :**

- [1] Candidatures / CANDIDATER EN MASTER 2 (pages=n/a-n/a, score=0.8775, semantic=0.8775, dans_contexte=oui)  https://www.inalco.fr/candidatures
- [2] FAQ Admission en Master / Une question sur la plateforme MonMaster? (pages=n/a-n/a, score=0.8732, semantic=0.8732, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [3] FAQ Admission en Master / Puis-je candidater directement en Master 2 ? (pages=n/a-n/a, score=0.8708, semantic=0.8708, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [4] Candidater à un cursus diplômant / Candidater en Master (pages=n/a-n/a, score=0.8705, semantic=0.8705, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [5] FAQ Admission en Master / QUELLE EST LA DIFFERENCE ENTRE UN MASTER PRO, UN MASTER RECHERCHE ET LES AUTRES MENTIONS ? (pages=n/a-n/a, score=0.8617, semantic=0.8617, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master

**Faits de référence (non transmis au modèle) :**

- Certains masters acceptent une admission directe en M2 pour des candidats ayant au minimum un niveau M1
- Pour les candidats extérieurs à l'Inalco, la campagne M2 2026 annoncée se déroule du 17 février au 16 mars
- La candidature directe en M2 s'effectue sur eCandidat pour les masters concernés

## q016. Quels tests de langue sont demandés pour le master Traduction et interprétation ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Master TI - Traduction spécialisée / FAQ (pages=n/a-n/a, score=0.8685, semantic=0.8685, dans_contexte=non)  https://www.inalco.fr/formations/master-ti-traduction-specialisee
- [2] Master TI - Traduction spécialisée / Master TI - Traduction spécialisée (pages=n/a-n/a, score=0.8658, semantic=0.8658, dans_contexte=non)  https://www.inalco.fr/formations/master-ti-traduction-specialisee
- [3] Master TI - Traduction spécialisée / Master TI - Traduction spécialisée (pages=n/a-n/a, score=0.8645, semantic=0.8645, dans_contexte=non)  https://www.inalco.fr/formations/master-ti-traduction-specialisee
- [4] Master TI - Traduction spécialisée / Master TI - Traduction spécialisée (pages=n/a-n/a, score=0.8645, semantic=0.8645, dans_contexte=non)  https://www.inalco.fr/formations/master-ti-traduction-specialisee
- [5] Master TI - Traduction spécialisée / Attendus (pages=n/a-n/a, score=0.8628, semantic=0.8628, dans_contexte=non)  https://www.inalco.fr/formations/master-ti-traduction-specialisee

**Faits de référence (non transmis au modèle) :**

- Les épreuves d'admission évaluent les compétences en français, en anglais et en langue orientale
- Les candidats sont évalués sur la traduction, l'orthographe, la précision de l'expression et la capacité d'analyse
- Le niveau correspondant généralement à une L3 est le niveau B2 du CECRL
- Un TOEFL peut être exigé par certaines universités partenaires pour le semestre intégré

## q017. Quels sont les prérequis pour candidater au master Traitement automatique des langues ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5350 caractères`

**Reponse :**

Les prérequis pour candidater au master Traitement automatique des langues (TAL) sont les suivants :
- Être titulaire de la Licence LLCER parcours Traitement automatique des langues délivrée par l’Inalco.
- Justifier d'un niveau suffisant dans une langue enseignée à l'Inalco et faire preuve de compétences en linguistique ou en informatique.

Sources :
- [Source 1]

**Sources recuperees :**

- [1] Master Traitement automatique des langues (TAL) / Candidatures (pages=n/a-n/a, score=0.8972, semantic=0.8972, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [2] Master Traitement automatique des langues (TAL) / Public visé (pages=n/a-n/a, score=0.8853, semantic=0.8853, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [3] Master Traitement automatique des langues (TAL) / Master Traitement automatique des langues (TAL) (pages=n/a-n/a, score=0.8841, semantic=0.8841, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [4] Master Traitement automatique des langues (TAL) / Spécialités du master TAL (pages=n/a-n/a, score=0.8833, semantic=0.8833, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [5] Master Traitement automatique des langues (TAL) / Master Traitement automatique des langues (TAL) (pages=n/a-n/a, score=0.8795, semantic=0.8795, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal

**Faits de référence (non transmis au modèle) :**

- Un candidat au Master TAL peut être titulaire de la licence LLCER parcours Traitement automatique des langues de l'Inalco
- À défaut, il doit justifier d'un niveau suffisant dans une langue enseignée à l'Inalco et de compétences en linguistique ou en informatique

## q020. Est-il encore possible de candidater après la fermeture de la campagne principale ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `clarify`  
**Abstention produite :** `False`
**Clarification produite :** `True`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Pour quelle formation et quel niveau d'entrée souhaitez-vous connaître les dates de candidature ?

**Sources recuperees :**


## q021. Quand et comment les résultats d'admission sont-ils communiqués ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `True`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Pour quelle formation et quel niveau d'entrée souhaitez-vous connaître les dates de candidature ?

**Sources recuperees :**


**Faits de référence (non transmis au modèle) :**

- Pour la campagne 2026 mentionnée dans la FAQ, les résultats d'admission en master sont disponibles sur Mon Master à partir du 3 juin 2026

## q022. Que dois-je faire après avoir reçu une autorisation d'admission ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Candidater à un cursus diplômant / 3. Après l'admission, demander son visa et s'inscrire administrativement à l'Inalco (pages=n/a-n/a, score=0.8299, semantic=0.8299, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [2] Candidater à un cursus diplômant / 3. Après l'admission, demander son visa et s'inscrire administrativement à l'Inalco (pages=n/a-n/a, score=0.8289, semantic=0.8289, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [3] Candidater à un cursus diplômant / 3. Après l'admission, demander son visa et s'inscrire administrativement à l'Inalco (pages=n/a-n/a, score=0.8265, semantic=0.8265, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [4] Candidater à un cursus diplômant / 3. Après l'admission, demander son visa et s'inscrire administrativement à l'Inalco (pages=n/a-n/a, score=0.8254, semantic=0.8254, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [5] FAQ Admission en Master / Une fois que j'aurai une autorisation d'admission, quelle sera la suite ? (pages=n/a-n/a, score=0.8253, semantic=0.8253, dans_contexte=non)  https://www.inalco.fr/faq-admission-en-master

**Faits de référence (non transmis au modèle) :**

- Après une proposition d'admission, le candidat doit confirmer son acceptation dans le délai indiqué par la plateforme utilisée
- Un candidat relevant d'Études en France doit obtenir son visa avant l'inscription administrative
- L'inscription administrative doit être réalisée après l'admission
- L'inscription pédagogique intervient après l'inscription administrative

## q023. Quelle est la différence entre candidature, admission, inscription administrative et inscription pédagogique ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Foire aux questions (FAQ) - Procédure d'inscription / Envoi du dossier d'inscription administrative (pages=n/a-n/a, score=0.8618, semantic=0.8618, dans_contexte=non)  https://www.inalco.fr/foire-aux-questions-faq-procedure-dinscription
- [2] Inscription et réinscription administrative / Inscription et réinscription administrative (pages=n/a-n/a, score=0.8587, semantic=0.8587, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-administrative.html
- [3] Inscriptions administratives / Inscriptions administratives (pages=n/a-n/a, score=0.8581, semantic=0.8581, dans_contexte=non)  https://www.inalco.fr/inscriptions-administratives
- [4] Inscriptions administratives / Reprise d'études : formation initiale ou continue ? (pages=n/a-n/a, score=0.8581, semantic=0.8581, dans_contexte=non)  https://www.inalco.fr/inscriptions-administratives
- [5] Candidatures et réinscriptions / Candidatures et réinscriptions (pages=n/a-n/a, score=0.856, semantic=0.856, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions.html

**Faits de référence (non transmis au modèle) :**

- La candidature consiste à déposer une demande d'accès à une formation
- L'admission correspond à la décision favorable rendue sur cette candidature
- L'inscription administrative confère le statut d'étudiant après vérification du dossier et paiement des droits
- L'inscription pédagogique correspond notamment au choix et à l'enregistrement des enseignements suivis

## q027. Dans quelles situations peut-on demander une exonération des droits d'inscription ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Droits de scolarité : tarifs, exonération, annulation, remboursement / Autres exonérations pouvant être accordées par le Président (pages=n/a-n/a, score=0.8593, semantic=0.8593, dans_contexte=non)  https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement
- [2] Droits de scolarité : tarifs, exonération, annulation, remboursement / Modalités d’exonération sur demande des droits d’inscription applicables aux usagers de l’Inalco, communautaires ou extra-communautaires, pour l’année universitaire 2026/2027 (pages=n/a-n/a, score=0.856, semantic=0.856, dans_contexte=non)  https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement
- [3] Droits de scolarité : tarifs, exonération, annulation, remboursement / Modalités d’exonération sur demande des droits d’inscription applicables aux usagers de l’Inalco, communautaires ou extra-communautaires, pour l’année universitaire 2026/2027 (pages=n/a-n/a, score=0.8506, semantic=0.8506, dans_contexte=non)  https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement
- [4] Droits de scolarité : tarifs, exonération, annulation, remboursement / Modalités d’exonération sur demande des droits d’inscription applicables aux usagers de l’Inalco, communautaires ou extra-communautaires, pour l’année universitaire 2026/2027 (pages=n/a-n/a, score=0.8489, semantic=0.8489, dans_contexte=non)  https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement
- [5] Droits de scolarité : tarifs, exonération, annulation, remboursement / Modalités d’exonération sur demande des droits d’inscription applicables aux usagers de l’Inalco, communautaires ou extra-communautaires, pour l’année universitaire 2026/2027 (pages=n/a-n/a, score=0.8474, semantic=0.8474, dans_contexte=non)  https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement

**Faits de référence (non transmis au modèle) :**

- Une exonération peut être demandée en raison de la situation personnelle de l'étudiant
- La demande doit être accompagnée de pièces justificatives
- Les réfugiés, bénéficiaires de protections, demandeurs d'asile, bénéficiaires du RSA et certains étudiants en situation de handicap figurent parmi les catégories pouvant demander une exonération
- L'exonération sur demande porte sur un seul diplôme dans les conditions indiquées
- Lorsqu'elle est accordée, l'exonération est effectuée par remboursement des droits déjà payés

## q028. Puis-je demander une bourse ou une aide financière avant mon inscription définitive ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Foire aux questions (FAQ) - Procédure d'inscription / Foire aux questions (FAQ) - Procédure d'inscription (pages=n/a-n/a, score=0.8649, semantic=0.8649, dans_contexte=non)  https://www.inalco.fr/foire-aux-questions-faq-procedure-dinscription
- [2] Candidater à un cursus diplômant / Bourse (pages=n/a-n/a, score=0.8552, semantic=0.8552, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [3] Foire aux questions (FAQ) - Procédure d'inscription / Etudiant boursier (pages=n/a-n/a, score=0.8531, semantic=0.8531, dans_contexte=non)  https://www.inalco.fr/foire-aux-questions-faq-procedure-dinscription
- [4] Inscriptions administratives / Procédure d'inscription administrative (pages=n/a-n/a, score=0.8525, semantic=0.8525, dans_contexte=non)  https://www.inalco.fr/inscriptions-administratives
- [5] Bourses et aides sociales / Bourses et aides sociales (pages=n/a-n/a, score=0.8509, semantic=0.8509, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-aides-sociales.html

**Faits de référence (non transmis au modèle) :**

- Le Dossier social étudiant permet de demander une bourse et un logement en résidence universitaire
- Le DSE doit être renouvelé chaque année sur messervices.etudiant.gouv.fr
- La demande peut être déposée avant de disposer de tous les éléments définitifs et être modifiée ensuite

## q029. Quelles solutions de logement sont proposées aux futurs étudiants de l'Inalco ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4627 caractères`

**Reponse :**

L’Inalco ne propose pas de service de logement pour la communauté étudiante. Cependant, vous pouvez consulter la page suivante pour obtenir des informations et des conseils sur la recherche de logements, les procédures d’emménagement et les aides locatives : [Se loger](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html).

Sources :
- [Se loger](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html)

**Sources recuperees :**

- [1] Se loger / Se loger (pages=n/a-n/a, score=0.8718, semantic=0.8718, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html
- [2] Accueil - Portail étudiant Inalco / Besoin d’un ordinateur ou d’internet ? L’Inalco vous prête le matériel (pages=n/a-n/a, score=0.8635, semantic=0.8635, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/index.html
- [3] Schéma Directeur de la Vie Étudiante 2023-2028 / Page 16 (pages=16-16, score=0.8618, semantic=0.8618, dans_contexte=oui)  https://www.inalco.fr/sites/default/files/2024-05/Sh%C3%A9ma%20Directeur%20de%20la%20Vie%20%C3%89tudiante-avec%20compression.pdf
- [4] Accueil et intégration / Bienvenue à l'Inalco ! (pages=n/a-n/a, score=0.8617, semantic=0.8617, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration.html
- [5] Schéma Directeur de la Vie Étudiante 2023-2028 / Page 9 (pages=9-9, score=0.8595, semantic=0.8595, dans_contexte=oui)  https://www.inalco.fr/sites/default/files/2024-05/Sh%C3%A9ma%20Directeur%20de%20la%20Vie%20%C3%89tudiante-avec%20compression.pdf

**Faits de référence (non transmis au modèle) :**

- L'Inalco ne dispose pas de service de logement pour les étudiants
- Le portail fournit des informations sur la recherche de logement, l'emménagement et les aides locatives
- Il renvoie notamment vers le Crous de Paris, Campus France et un guide des aides au logement

## q030. Existe-t-il des restaurants universitaires à proximité de l'Inalco ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4774 caractères`

**Reponse :**

Réponse :
Oui, il existe des restaurants universitaires à proximité de l'Inalco. Vous pouvez consulter les horaires d'ouverture sur le site du Crous ou sur l'application Crous Mobile.

Sources :
- [Se nourrir](https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html)

**Sources recuperees :**

- [1] Se nourrir / Restaurants et cafétérias universitaires (pages=n/a-n/a, score=0.8722, semantic=0.8722, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html
- [2] Distribution alimentaire gratuite / Luttons contre la précarité étudiante (pages=n/a-n/a, score=0.8593, semantic=0.8593, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/evenements/evenements-2026/avril-2026/distribution-alimentaire-gratuite.html
- [3] Distribution alimentaire gratuite / Luttons contre la précarité étudiante (pages=n/a-n/a, score=0.8542, semantic=0.8542, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/evenements/evenements-2026/avril-2026/distribution-alimentaire-gratuite.html
- [4] Santé, sport et bien-être / Santé, sport et bien-être (pages=n/a-n/a, score=0.8531, semantic=0.8531, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre.html
- [5] Faire sa rentrée à l'Inalco / Bienvenue à l'Inalco ! (pages=n/a-n/a, score=0.8509, semantic=0.8509, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juillet-2026/faire-sa-rentree.html

**Faits de référence (non transmis au modèle) :**

- La cafétéria de l'Inalco et plusieurs restaurants universitaires se trouvent à proximité
- Le Restaurant Universitaire de la Halle aux farines est situé au 3 esplanade Pierre Vidal-Naquet, 75013 Paris
- La Halle aux farines est ouverte du lundi au vendredi de 11h15 à 14h15 selon la page collectée

## q032. Comment se rendre au Pôle des langues et civilisations et à la Maison de la recherche ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Le Pôle des langues et civilisations / Adresse (pages=n/a-n/a, score=0.8624, semantic=0.8624, dans_contexte=non)  https://www.inalco.fr/le-pole-des-langues-et-civilisations
- [2] La Maison de la recherche / Accès (pages=n/a-n/a, score=0.8495, semantic=0.8495, dans_contexte=non)  https://www.inalco.fr/la-maison-de-la-recherche
- [3] Le Pôle des langues et civilisations / Le Pôle des langues et civilisations (pages=n/a-n/a, score=0.8494, semantic=0.8494, dans_contexte=non)  https://www.inalco.fr/le-pole-des-langues-et-civilisations
- [4] Le Pôle des langues et civilisations / Horaires d'ouverture (pages=n/a-n/a, score=0.8466, semantic=0.8466, dans_contexte=non)  https://www.inalco.fr/le-pole-des-langues-et-civilisations
- [5] Se rendre à l'Inalco / Le Pôle des langues et des civilisations (PLC) (pages=n/a-n/a, score=0.8463, semantic=0.8463, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-rendre-a-l-inalco.html

**Faits de référence (non transmis au modèle) :**

- Le Pôle des langues et civilisations est situé au 65 rue des Grands Moulins, 75013 Paris
- Le PLC est accessible par le RER C à Bibliothèque François Mitterrand
- Les bus 83, 89, 27, 62, 64, 132 et N31 desservent des arrêts indiqués à proximité du PLC
- La Maison de la recherche est située au 2 rue de Lille, 75007 Paris
- La Maison de la recherche est accessible notamment par les métros 1, 4, 7 et 12, par le RER C à Musée d'Orsay et par les bus 27, 39, 68, 69, 87 et 95

## q033. Existe-t-il des journées portes ouvertes pour découvrir l'Inalco ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Faire sa rentrée à l'Inalco / Bienvenue à l'Inalco ! (pages=n/a-n/a, score=0.8586, semantic=0.8586, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juillet-2026/faire-sa-rentree.html
- [2] Dejima - Association des étudiants du département Études japonaises / En savoir plus sur nous (pages=n/a-n/a, score=0.8558, semantic=0.8558, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/les-associations-etudiantes/dejima.html
- [3] Construire son projet d'études / DES EVENEMENTS DEDIES A L'ORIENTATION (pages=n/a-n/a, score=0.8544, semantic=0.8544, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/information-et-orientation/construire-son-projet-d-etudes.html
- [4] Journées européennes du patrimoine 2026 : appel à bénévoles / Journées européennes du patrimoine 2026 : appel à bénévoles (pages=n/a-n/a, score=0.8521, semantic=0.8521, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juillet-2026/journees-europeennes-du-patrimoine-2026-appel-a-benevoles-2.html
- [5] Faire sa rentrée / Bienvenue à l'Inalco ! (pages=n/a-n/a, score=0.8521, semantic=0.8521, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/faire-sa-rentree.html

**Faits de référence (non transmis au modèle) :**

- L'Inalco organise des événements consacrés à l'orientation tout au long de l'année universitaire
- Ces événements comprennent notamment une journée portes ouvertes, des forums lycéens, des salons étudiants et une journée d'information et d'orientation

## q034. Où puis-je consulter les brochures détaillées des licences et des masters ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Masters LLCER - Brochures / Brochures générales (pages=n/a-n/a, score=0.8616, semantic=0.8616, dans_contexte=non)  https://www.inalco.fr/masters-llcer-brochures
- [2] Masters LLCER - Brochures / Études chinoises (pages=n/a-n/a, score=0.8512, semantic=0.8512, dans_contexte=non)  https://www.inalco.fr/masters-llcer-brochures
- [3] Masters LLCER - Brochures / Études japonaises (pages=n/a-n/a, score=0.8495, semantic=0.8495, dans_contexte=non)  https://www.inalco.fr/masters-llcer-brochures
- [4] Masters LLCER - Brochures / Études hébraïques et juives (pages=n/a-n/a, score=0.8478, semantic=0.8478, dans_contexte=non)  https://www.inalco.fr/masters-llcer-brochures
- [5] Masters LLCER - Brochures / Études arabes (pages=n/a-n/a, score=0.8475, semantic=0.8475, dans_contexte=non)  https://www.inalco.fr/masters-llcer-brochures

**Faits de référence (non transmis au modèle) :**

- Les brochures des licences LLCER sont publiées sur la page Licences LLCER - Brochures
- Les brochures des masters LLCER sont publiées sur une page distincte consacrée aux masters
- Les brochures sont organisées par langue ou aire d'études

## q035. Où trouver le catalogue des enseignements et la description des cours ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Dates et calendriers / Comment utiliser le planning des cours (pages=n/a-n/a, score=0.8437, semantic=0.8437, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html
- [2] Dates et calendriers / Comment utiliser le planning des cours (pages=n/a-n/a, score=0.843, semantic=0.843, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html
- [3] Emplois du temps / Comment utiliser le planning ? (pages=n/a-n/a, score=0.8372, semantic=0.8372, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html
- [4] Sans titre / Catalogue de cours et de formations EUniWell : la sélection de septembre 202611 sept. 2026 10:12 - RSS Actu Faites passer vos compétences académiques et professionnelles au niveau supérieur ! Le catalogue EUniWell de cours et de formations est destiné aux étudiants, personnels administratifs et chercheurs de l'Inalco. (pages=n/a-n/a, score=0.8368, semantic=0.8368, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/recherche-2/flux-rss.html
- [5] Emplois du temps / Comment utiliser le planning ? (pages=n/a-n/a, score=0.8322, semantic=0.8322, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html

## q036. Puis-je consulter les emplois du temps avant de finaliser mon inscription ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Emplois du temps / Emplois du temps (pages=n/a-n/a, score=0.8495, semantic=0.8495, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html
- [2] Emplois du temps / Emplois du temps (pages=n/a-n/a, score=0.8493, semantic=0.8493, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html
- [3] Dates et calendriers / Emplois du temps (pages=n/a-n/a, score=0.8449, semantic=0.8449, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html
- [4] Dates et calendriers / Comment utiliser le planning des cours (pages=n/a-n/a, score=0.8434, semantic=0.8434, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html
- [5] Emplois du temps / Comment utiliser le planning ? (pages=n/a-n/a, score=0.842, semantic=0.842, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html

**Faits de référence (non transmis au modèle) :**

- Les emplois du temps sont consultables sur le planning public de l'Inalco
- Les emplois du temps affichés peuvent être modifiés jusqu'à la rentrée universitaire

## q038. Quelles formations professionnalisantes sont proposées par l'Inalco ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Formation en alternance / ÉLIGIBILITÉ (pages=n/a-n/a, score=0.8597, semantic=0.8597, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/formation-en-alternance.html
- [2] Master Traitement automatique des langues (TAL) / Débouchés professionnels (pages=n/a-n/a, score=0.8559, semantic=0.8559, dans_contexte=non)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [3] Diplômes d'établissement / Diplômes d'établissement (pages=n/a-n/a, score=0.8537, semantic=0.8537, dans_contexte=non)  https://www.inalco.fr/formations/diplomes-detablissement
- [4] Étudiants internationaux à l'Inalco / **Cours et conditions linguistiques** (pages=n/a-n/a, score=0.8507, semantic=0.8507, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/international/venir-etudier-a-l-inalco.html
- [5] Candidater à un cursus diplômant / 1. Choisir sa formation (pages=n/a-n/a, score=0.8506, semantic=0.8506, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant

## q040. L'Inalco propose-t-il des parcours permettant d'étudier deux langues ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `4761 caractères`

**Reponse :**

L'Inalco propose des parcours permettant d'étudier deux langues, notamment à travers la Licence LLCER à parcours bilangue. Pour plus d'informations, vous pouvez consulter la page officielle dédiée à cette formation : [Licence LLCER à parcours bilangue](https://www.inalco.fr/formations/licence-llcer-parcours-bilangue).

Sources :
- [Licence LLCER à parcours bilangue](https://www.inalco.fr/formations/licence-llcer-parcours-bilangue)

**Sources recuperees :**

- [1] Licence LLCER à parcours bilangue / Pourquoi étudier deux langues orientales ? (pages=n/a-n/a, score=0.8779, semantic=0.8779, dans_contexte=oui)  https://www.inalco.fr/formations/licence-llcer-parcours-bilangue
- [2] Étudiants internationaux à l'Inalco / **Cours et conditions linguistiques** (pages=n/a-n/a, score=0.8701, semantic=0.8701, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/international/venir-etudier-a-l-inalco.html
- [3] Master Traitement automatique des langues (TAL) / Master Traitement automatique des langues (TAL) (pages=n/a-n/a, score=0.868, semantic=0.868, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [4] Master Traitement automatique des langues (TAL) / Master Traitement automatique des langues (TAL) (pages=n/a-n/a, score=0.8648, semantic=0.8648, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [5] Licence LLCER à parcours bilangue / Licence LLCER à parcours bilangue (pages=n/a-n/a, score=0.8645, semantic=0.8645, dans_contexte=non)  https://www.inalco.fr/formations/licence-llcer-parcours-bilangue

**Faits de référence (non transmis au modèle) :**

- L'Inalco propose des licences LLCER bilangues permettant d'étudier deux langues
- Ces parcours permettent d'associer notamment des langues apparentées, voisines ou liées par des relations historiques, économiques ou géopolitiques

## q041. Quels parcours thématiques ou disciplinaires peut-on choisir en licence LLCER ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4824 caractères`

**Reponse :**

Les parcours thématiques et disciplinaires disponibles en licence LLCER à l'Inalco sont les suivants :

1. **Parcours thématiques :**
   - Parcours thématique 1
   - Parcours thématique 2
   - Parcours thématique 3
   - Parcours thématique 4
   - Parcours thématique 5
   - Parcours thématique 6
   - Parcours thématique 7
   - Parcours thématique 8
   - Parcours thématique 9
   - Parcours thématique 10
   - Parcours thématique 11
   - Parcours thématique 12

2. **Parcours disciplinaires :**
   - Parcours disciplinaire 1
   - Parcours disciplinaire 2
   - Parcours disciplinaire 3
   - Parcours disciplinaire 4
   - Parcours disciplinaire 5
   - Parcours disciplinaire 6
   - Parcours disciplinaire 7
   - Parcours disciplinaire 8
   - Parcours disciplinaire 9
   - Parcours disciplinaire 10
   - Parcours disciplinaire 11
   - Parcours disciplinaire 12

Pour plus de détails sur chaque parcours, vous pouvez consulter la brochure détaillée et le livret synthétique disponibles sur la page officielle des licences LLCER à parcours thématiques et disciplinaires.

Sources :
- [Licences LLCER à parcours thématiques et disciplinaires](https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires)

**Sources recuperees :**

- [1] Licences LLCER à parcours thématiques et disciplinaires / Licences LLCER à parcours thématiques et disciplinaires (pages=n/a-n/a, score=0.9145, semantic=0.9145, dans_contexte=oui)  https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires
- [2] Licences LLCER à parcours thématiques et disciplinaires / Licences LLCER à parcours thématiques et disciplinaires (pages=n/a-n/a, score=0.9106, semantic=0.9106, dans_contexte=oui)  https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires
- [3] Licences LLCER à parcours thématiques et disciplinaires / En complément des parcours : ouverture, anglais, engagement étudiant (pages=n/a-n/a, score=0.9088, semantic=0.9088, dans_contexte=oui)  https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires
- [4] Licences LLCER à parcours thématiques et disciplinaires / Documentation (pages=n/a-n/a, score=0.9039, semantic=0.9039, dans_contexte=oui)  https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires
- [5] Licences LLCER à parcours thématiques et disciplinaires / Organisation des parcours thématiques et disciplinaires (pages=n/a-n/a, score=0.9018, semantic=0.9018, dans_contexte=oui)  https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires

**Faits de référence (non transmis au modèle) :**

- Après la L1, un étudiant peut poursuivre en L2-L3 dans l'un des douze parcours thématiques et disciplinaires
- Ce parcours complète les enseignements de langue et de civilisation
- Le choix du parcours est effectué lors de l'inscription pédagogique

## q044. Quels aménagements sont proposés aux candidats en situation de handicap ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Mission Handicap / Procédure de la mise en place du plan d'accompagnement (PAEH) (pages=n/a-n/a, score=0.842, semantic=0.842, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [2] Mission Handicap / Procédure de la mise en place du plan d'accompagnement (PAEH) (pages=n/a-n/a, score=0.8396, semantic=0.8396, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [3] Handicap / Journées de sensibilisation au Handicap (pages=n/a-n/a, score=0.8361, semantic=0.8361, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/journees-vie-de-campus/journees-thematiques/handicap.html
- [4] Aménagement du cursus / Aménagement du cursus (pages=n/a-n/a, score=0.8351, semantic=0.8351, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/amenagement-du-cursus.html
- [5] Mission Handicap / Attention (pages=n/a-n/a, score=0.8319, semantic=0.8319, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html

**Faits de référence (non transmis au modèle) :**

- La Mission Handicap met en place un plan d'accompagnement de l'étudiant en situation de handicap
- Le PAEH précise les aménagements prévus pour les cours et les examens
- Une demande d'aménagement d'examen nécessite un PAEH validé
- La demande d'aménagement doit être renouvelée chaque année universitaire

## q045. Existe-t-il une procédure particulière pour les candidats en exil ou réfugiés ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Candidater à un cursus diplômant / Candidats en exil primo-arrivants (pages=n/a-n/a, score=0.8455, semantic=0.8455, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [2] Candidater à un cursus diplômant / Situation familiale (pages=n/a-n/a, score=0.8403, semantic=0.8403, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [3] Candidater à un cursus diplômant / Bourse (pages=n/a-n/a, score=0.8321, semantic=0.8321, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [4] Candidater à un cursus diplômant / Candidats européens, candidats intéressés par un diplôme d'établissement ou candidats en exil (pages=n/a-n/a, score=0.8319, semantic=0.8319, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [5] Candidatures / Pour candidater aux cours de préparation à l'agrégation d'arabe, voir la page ci-dessous (pages=n/a-n/a, score=0.8312, semantic=0.8312, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/candidatures.html

**Faits de référence (non transmis au modèle) :**

- Les candidats en exil primo-arrivants comprennent les réfugiés, apatrides et bénéficiaires de la protection subsidiaire ou temporaire
- Selon leur profil, ils peuvent être éligibles au DU Passerelle Inalco
- Pour candidater à un autre diplôme par la procédure indiquée, un niveau B1 minimum en français est demandé

## q047. Quelles sont les conditions d'admission pour le parcours XXX ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `clarify`  
**Abstention produite :** `False`
**Clarification produite :** `True`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Pouvez-vous préciser la composante, la formation, la langue ou le parcours concerné ?

**Sources recuperees :**


## q048. Puis-je candidater à plusieurs masters de l'Inalco en même temps ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `True`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Pour quelle formation et quel niveau d'entrée souhaitez-vous connaître les dates de candidature ?

**Sources recuperees :**


**Faits de référence (non transmis au modèle) :**

- Il est possible de candidater à plusieurs masters
- Pour la phase de candidature Mon Master 2026 mentionnée, un candidat peut déposer au maximum quinze candidatures, auxquelles peuvent s'ajouter quinze candidatures en alternance
- Suivre plusieurs masters simultanément peut être difficile en raison de la charge de travail et des chevauchements d'emploi du temps

## q049. Puis-je candidater à un nouveau master si je possède déjà un diplôme de master ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5657 caractères`

**Reponse :**

Réponse :
Oui, il est possible de candidater à un nouveau master si vous possédez déjà un diplôme de master. Cependant, il n’est pas possible de se réinscrire dans un parcours de master déjà acquis. Il est suggéré dans la démarche de candidature d’expliciter les motifs qui vous encouragent à solliciter l’obtention d’un autre master.

Sources :
- [FAQ Admission en Master](https://www.inalco.fr/faq-admission-en-master)

**Sources recuperees :**

- [1] FAQ Admission en Master / J’ai déjà un Master. Puis-je candidater pour un nouveau Master ? (pages=n/a-n/a, score=0.895, semantic=0.895, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [2] FAQ Admission en Master / Une question sur la plateforme MonMaster? (pages=n/a-n/a, score=0.8644, semantic=0.8644, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [3] FAQ Admission en Master / Je suis un adulte en reprise d’études, puis-je candidater pour un Master ? (pages=n/a-n/a, score=0.8642, semantic=0.8642, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [4] FAQ Admission en Master / Puis-je candidater et suivre 2 Masters en parallèle ? (pages=n/a-n/a, score=0.8609, semantic=0.8609, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [5] FAQ Admission en Master / Une question sur la plateforme MonMaster? (pages=n/a-n/a, score=0.8573, semantic=0.8573, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master

**Faits de référence (non transmis au modèle) :**

- Une personne déjà titulaire d'un master peut candidater à un nouveau master
- Il n'est pas possible de se réinscrire dans un parcours de master déjà acquis

## q050. Quels sont les débouchés professionnels après une formation à l'Inalco ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `clarify`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Master Traitement automatique des langues (TAL) / Débouchés professionnels (pages=n/a-n/a, score=0.851, semantic=0.851, dans_contexte=non)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [2] Diplômes d'établissement / Diplômes d'établissement (pages=n/a-n/a, score=0.8459, semantic=0.8459, dans_contexte=non)  https://www.inalco.fr/formations/diplomes-detablissement
- [3] Schéma Directeur Développement Durable et Responsabilité Sociale et Environnementale (SD DD&RSE) / Schéma Directeur Développement Durable et Responsabilité Sociale et Environnementale (SD DD&RSE) (pages=n/a-n/a, score=0.8413, semantic=0.8413, dans_contexte=non)  https://www.inalco.fr/ddrse
- [4] Schéma Directeur Développement Durable et Responsabilité Sociale et Environnementale (SD DD&RSE) / Schéma Directeur Développement Durable et Responsabilité Sociale et Environnementale (SD DD&RSE) (pages=n/a-n/a, score=0.8411, semantic=0.8411, dans_contexte=non)  https://www.inalco.fr/ddrse
- [5] Construire son projet pro / Construire son projet pro (pages=n/a-n/a, score=0.841, semantic=0.841, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/construire-son-projet-pro.html

## q052. Que faire si un cours ou un groupe n'apparaît pas dans mon emploi du temps ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Dates et calendriers / Comment utiliser le planning des cours (pages=n/a-n/a, score=0.8351, semantic=0.8351, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html
- [2] Emplois du temps / Comment utiliser le planning ? (pages=n/a-n/a, score=0.833, semantic=0.833, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html
- [3] Tutorat / Vous êtes étudiant en L1, L2, L3 LLCER : (pages=n/a-n/a, score=0.8312, semantic=0.8312, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/tutorat.html
- [4] Emplois du temps / Comment utiliser le planning ? (pages=n/a-n/a, score=0.8299, semantic=0.8299, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html
- [5] Tutorat / Vous êtes étudiant en parcours aménagé L1+ ou Tempo 1.1 : (pages=n/a-n/a, score=0.8293, semantic=0.8293, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/tutorat.html

**Faits de référence (non transmis au modèle) :**

- Les enseignements transversaux disciplinaires de L2 et L3 ne figurent pas dans le planning principal du parcours
- Pour les retrouver, il faut rechercher la rubrique Parcours et sélectionner le parcours concerné
- Les enseignements de civilisation communs à plusieurs langues doivent être recherchés par aire géographique ou département
- Pour afficher plusieurs cours simultanés, il faut utiliser les chiffres affichés à gauche de la plage horaire

## q053. Comment accéder à Moodle et retrouver les espaces de mes cours ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5425 caractères`

**Reponse :**

Pour accéder à Moodle et retrouver les espaces de vos cours, suivez ces étapes :

1. **Inscription administrative et pédagogique** : Assurez-vous d'avoir effectué votre inscription administrative et votre inscription pédagogique (IP) à l'Inalco.
2. **Activation du compte numérique Inalco** : Activez votre compte numérique Inalco sur [https://compte.inalco.fr/](https://compte.inalco.fr/).
3. **Connexion à Moodle** : Connectez-vous à Moodle en entrant votre numéro d'étudiant et le mot de passe choisi lors de l'activation de votre compte numérique Inalco.
4. **Tableau de bord** : Une fois connecté, vous serez dirigé vers votre espace personnel, le tableau de bord, qui contient la liste des cours auxquels vous êtes inscrit pédagogiquement. Seuls les cours ouverts par vos enseignants sont visibles.

Si certaines matières n'apparaissent pas, vérifiez d'abord votre inscription pédagogique sur [MonDossierWeb](https://mondossierweb.inalco.fr/) puis contactez votre enseignant pour vérifier que le cours est bien ouvert.

Pour plus d'informations, consultez la page officielle sur les services et ressources numériques de l'Inalco : [https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html).

Sources :
- [Services et ressources numériques](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html)

**Sources recuperees :**

- [1] Services et ressources numériques / Moodle (pages=n/a-n/a, score=0.8695, semantic=0.8695, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [2] Services et ressources numériques / Moodle (pages=n/a-n/a, score=0.868, semantic=0.868, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [3] Services et ressources numériques / Scolarité (pages=n/a-n/a, score=0.8644, semantic=0.8644, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [4] Services et ressources numériques / Scolarité (pages=n/a-n/a, score=0.8581, semantic=0.8581, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [5] Services et ressources numériques / Wi-Fi (pages=n/a-n/a, score=0.8568, semantic=0.8568, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html

**Faits de référence (non transmis au modèle) :**

- L'accès à Moodle nécessite une inscription administrative et une inscription pédagogique à l'Inalco
- Le compte numérique Inalco doit être activé avant la connexion
- La connexion utilise le numéro étudiant et le mot de passe du compte numérique
- Le tableau de bord Moodle affiche les cours correspondant à l'inscription pédagogique
- Seuls les cours ouverts par les enseignants sont visibles

## q055. Comment activer mon compte numérique étudiant ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `4613 caractères`

**Reponse :**

Pour activer votre compte numérique étudiant, suivez ces étapes :

1. Connectez-vous à la page suivante : [https://compte.inalco.fr/](https://compte.inalco.fr/)
2. Entrez l’adresse e-mail personnelle fournie lors de votre inscription à l’Inalco et cliquez sur « Valider ».
3. Vous recevrez un mail avec un lien actif vous permettant de réinitialiser votre mot de passe.
4. Attention : notez bien votre identifiant usager, choisissez soigneusement votre mot de passe et retenez-le bien ; ils vous seront demandés pour vos futures connexions.

Sources :
- [Services et ressources numériques](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html)

**Sources recuperees :**

- [1] Services et ressources numériques / Compte numérique étudiant (pages=n/a-n/a, score=0.894, semantic=0.894, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [2] Services et ressources numériques / Compte numérique étudiant (pages=n/a-n/a, score=0.8922, semantic=0.8922, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [3] Consulter ses notes et son certificat de scolarité / 1-Se connecter au Portail Étudiant (pages=n/a-n/a, score=0.88, semantic=0.88, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [4] Faire sa rentrée à l'Inalco / Informations la création de votre compte numérique à l'Inalco durant la fermeture universitaire (pages=n/a-n/a, score=0.8665, semantic=0.8665, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juillet-2026/faire-sa-rentree.html
- [5] Faire sa rentrée à l'Inalco / Informations la création de votre compte numérique à l'Inalco durant la fermeture universitaire (pages=n/a-n/a, score=0.8655, semantic=0.8655, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juillet-2026/faire-sa-rentree.html

**Faits de référence (non transmis au modèle) :**

- Le compte numérique étudiant s'active sur compte.inalco.fr
- L'étudiant doit saisir l'adresse électronique personnelle fournie lors de son inscription
- Un courriel contenant un lien permet ensuite de définir ou réinitialiser le mot de passe

## q057. Les étudiantes et étudiants disposent-ils d'une adresse électronique institutionnelle ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Services et ressources numériques / Messagerie (pages=n/a-n/a, score=0.8411, semantic=0.8411, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [2] Services et ressources numériques / Messagerie (pages=n/a-n/a, score=0.8383, semantic=0.8383, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [3] Services et ressources numériques / Outils collaboratifs et services proposés (pages=n/a-n/a, score=0.8369, semantic=0.8369, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [4] Services et ressources numériques / Outils collaboratifs et services proposés (pages=n/a-n/a, score=0.8367, semantic=0.8367, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [5] Consulter ses notes et son certificat de scolarité / 1-Se connecter au Portail Étudiant (pages=n/a-n/a, score=0.8364, semantic=0.8364, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html

## q058. Quels outils et services numériques sont utiles pour suivre ma scolarité ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Services et ressources numériques / Services et ressources numériques (pages=n/a-n/a, score=0.865, semantic=0.865, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [2] Services et ressources numériques / Carte multi-services étudiante (pages=n/a-n/a, score=0.8637, semantic=0.8637, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [3] Services et ressources numériques / Moodle (pages=n/a-n/a, score=0.8629, semantic=0.8629, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [4] Consulter ses notes et son certificat de scolarité / 1-Se connecter au Portail Étudiant (pages=n/a-n/a, score=0.8613, semantic=0.8613, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [5] Consulter ses notes et son certificat de scolarité / 1-Se connecter au Portail Étudiant (pages=n/a-n/a, score=0.8547, semantic=0.8547, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html

**Faits de référence (non transmis au modèle) :**

- Le compte numérique Inalco donne accès aux services numériques étudiants
- Moodle permet d'accéder à des outils pédagogiques et à des contenus de cours à distance
- Le service REVE propose sous conditions des prêts d'ordinateurs et de galets 4G aux étudiants rencontrant des difficultés matérielles

## q059. Où consulter mes notes et mes résultats d'examen ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `3773 caractères`

**Reponse :**

Pour consulter vos notes et vos résultats d'examen, vous pouvez suivre ces étapes :

1. Connectez-vous au Portail Étudiant en utilisant vos identifiants numériques (moodle, eduspot, etc.).
2. Une fois connecté, allez dans la rubrique **"Mon espace perso"** située à droite de votre écran d'ordinateur ou en bas à droite de votre écran de smartphone.
3. Sélectionnez **"Ma scolarité"** puis cliquez sur **"Certificat & notes"**.
4. Cela vous redirigera vers **"MonDossierEtudiant"** où vous pourrez consulter vos notes et votre contrat pédagogique.

Sources :
- [Consulter ses notes et son certificat de scolarité](https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html)

**Sources recuperees :**

- [1] Consulter ses notes et son certificat de scolarité / 3-Consulter ses notes (pages=n/a-n/a, score=0.8697, semantic=0.8697, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [2] Consulter ses notes et son certificat de scolarité / 2-Accéder à mon dossier de scolarité (pages=n/a-n/a, score=0.8624, semantic=0.8624, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [3] Consulter ses notes et son certificat de scolarité / Consulter ses notes et son certificat de scolarité (pages=n/a-n/a, score=0.8576, semantic=0.8576, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [4] Consulter ses notes et son certificat de scolarité / 1-Se connecter au Portail Étudiant (pages=n/a-n/a, score=0.8554, semantic=0.8554, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [5] Consulter ses notes et son certificat de scolarité / Poursuivez le tutoriel ! (pages=n/a-n/a, score=0.8552, semantic=0.8552, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html

**Faits de référence (non transmis au modèle) :**

- Les notes sont consultables depuis le Portail étudiant
- L'accès utilise les identifiants du compte numérique Inalco
- Dans l'espace de scolarité, MonDossierEtudiant permet de consulter les résultats enregistrés

## q060. Comment télécharger mon certificat de scolarité ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4865 caractères`

**Reponse :**

Pour télécharger votre certificat de scolarité, suivez ces étapes :

1. Connectez-vous au Portail Étudiant à l'aide de vos identifiants numériques (moodle, eduspot, etc.).
2. Dans le bandeau **"Mon espace perso"** situé à droite de votre écran d'ordinateur ou en bas à droite de votre écran de smartphone, sélectionnez **"Ma scolarité"** puis cliquez sur **"Certificat & notes"**.
3. Une fois ces étapes réalisées, un nouvel onglet s'ouvrira vers **"MonDossierEtudiant"**.
4. Sur **"MonDossierEtudiant"**, vous pourrez consulter votre certificat de scolarité dans la rubrique **"Parcours"**. Ensuite, déroulez le menu en cliquant sur **"Détail de l'inscription"**.
5. Votre certificat de scolarité est téléchargeable au format PDF.

Si vous n'avez pas renouvelé votre inscription administrative pour les promotions 2025-2026 et antérieures, vous devez passer par le lien suivant pour consulter vos anciens relevés de notes et certificats de scolarité : [https://mondossierweb.inalco.fr/](https://mondossierweb.inalco.fr/)

Sources :
- [Consulter ses notes et son certificat de scolarité](https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html)

**Sources recuperees :**

- [1] Consulter ses notes et son certificat de scolarité / 4-Télécharger son certificat de scolarité (pages=n/a-n/a, score=0.8852, semantic=0.8852, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [2] Consulter ses notes et son certificat de scolarité / 2-Accéder à mon dossier de scolarité (pages=n/a-n/a, score=0.883, semantic=0.883, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [3] Consulter ses notes et son certificat de scolarité / 4-Télécharger son certificat de scolarité (pages=n/a-n/a, score=0.8792, semantic=0.8792, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [4] Consulter ses notes et son certificat de scolarité / 1-Se connecter au Portail Étudiant (pages=n/a-n/a, score=0.8717, semantic=0.8717, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [5] Consulter ses notes et son certificat de scolarité / 1-Se connecter au Portail Étudiant (pages=n/a-n/a, score=0.8692, semantic=0.8692, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html

**Faits de référence (non transmis au modèle) :**

- Le certificat de scolarité est accessible depuis MonDossierEtudiant
- Il se trouve dans la rubrique Parcours, sous Détail de l'inscription
- L'accès au dossier de scolarité se fait depuis le Portail étudiant avec le compte numérique

## q061. Comment effectuer ou renouveler mon inscription administrative ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5927 caractères`

**Reponse :**

Pour effectuer ou renouveler votre inscription administrative à l'Inalco, vous devez suivre les étapes suivantes :

1. **Connexion à la plateforme PEGASE** : Vous devez vous connecter à la plateforme PEGASE pour procéder à votre inscription administrative. Assurez-vous d'avoir les autorisations nécessaires pour accéder à cette plateforme.

2. **Dépôt des pièces justificatives** : Lors de votre inscription administrative, vous devrez déposer les pièces justificatives requises. Ces documents peuvent inclure des justificatifs de domicile, des relevés de notes, et d'autres documents spécifiques à votre situation.

3. **Paiement des droits de scolarité** : Si vous n'êtes pas boursier, vous devrez payer les droits de scolarité. Les étudiants boursiers sont exemptés de ces frais.

4. **Envoi des pièces justificatives** : Après avoir complété votre inscription administrative en ligne, vous devrez envoyer les pièces justificatives à l'adresse indiquée sur le récapitulatif de votre inscription.

Pour plus de détails, consultez la page officielle sur l'inscription et réinscription administrative : [Inscription et réinscription administrative](https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-administrative.html).

Sources :
- [Inscription et réinscription administrative](https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-administrative.html)
- [Inscriptions administratives](https://www.inalco.fr/inscriptions-administratives)

**Sources recuperees :**

- [1] Inscription et réinscription administrative / Inscription et réinscription administrative (pages=n/a-n/a, score=0.8697, semantic=0.8697, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-administrative.html
- [2] Inscriptions administratives / Reprise d'études : formation initiale ou continue ? (pages=n/a-n/a, score=0.8609, semantic=0.8609, dans_contexte=oui)  https://www.inalco.fr/inscriptions-administratives
- [3] Inscriptions administratives / Procédure d'inscription administrative (pages=n/a-n/a, score=0.8605, semantic=0.8605, dans_contexte=oui)  https://www.inalco.fr/inscriptions-administratives
- [4] Inscription et réinscription administrative / Pour connaître les dates et modalités d'inscription et réinscription administrative, consultez la page ci-dessous (pages=n/a-n/a, score=0.86, semantic=0.86, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-administrative.html
- [5] Foire aux questions (FAQ) - Procédure d'inscription / Foire aux questions (FAQ) - Procédure d'inscription (pages=n/a-n/a, score=0.853, semantic=0.853, dans_contexte=oui)  https://www.inalco.fr/foire-aux-questions-faq-procedure-dinscription

**Faits de référence (non transmis au modèle) :**

- L'inscription ou la réinscription administrative est annuelle et obligatoire
- Elle comprend le paiement des droits de scolarité et le dépôt des pièces justificatives sur PEGASE
- Elle permet d'obtenir le statut d'étudiant et le certificat de scolarité après validation
- L'inscription pédagogique intervient ensuite

## q063. Que faire si je constate une erreur dans mon inscription pédagogique ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Inscriptions pédagogiques / Procédure Master (pages=n/a-n/a, score=0.8497, semantic=0.8497, dans_contexte=non)  https://www.inalco.fr/inscriptions-pedagogiques
- [2] Inscription et réinscription pédagogique / **Pour connaître les dates et modalités d'inscription et réinscription pédagogique, consultez la page ci-dessous** (pages=n/a-n/a, score=0.8407, semantic=0.8407, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-pedagogique.html
- [3] Inscriptions pédagogiques / Inscriptions pédagogiques (pages=n/a-n/a, score=0.8376, semantic=0.8376, dans_contexte=non)  https://www.inalco.fr/inscriptions-pedagogiques
- [4] Inscriptions pédagogiques / Inscriptions pédagogiques (pages=n/a-n/a, score=0.837, semantic=0.837, dans_contexte=non)  https://www.inalco.fr/inscriptions-pedagogiques
- [5] Inscriptions pédagogiques / Précision parcours Tempo et L1+ (pages=n/a-n/a, score=0.8368, semantic=0.8368, dans_contexte=non)  https://www.inalco.fr/inscriptions-pedagogiques

## q064. Puis-je changer de groupe de cours après la validation de mon inscription pédagogique ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Inscriptions pédagogiques / Choix des groupes : (pages=n/a-n/a, score=0.8509, semantic=0.8509, dans_contexte=non)  https://www.inalco.fr/inscriptions-pedagogiques
- [2] Inscriptions pédagogiques / Choix des groupes : (pages=n/a-n/a, score=0.8489, semantic=0.8489, dans_contexte=non)  https://www.inalco.fr/inscriptions-pedagogiques
- [3] Inscriptions pédagogiques / Inscriptions pédagogiques (pages=n/a-n/a, score=0.841, semantic=0.841, dans_contexte=non)  https://www.inalco.fr/inscriptions-pedagogiques
- [4] Inscriptions pédagogiques / Procédure Master (pages=n/a-n/a, score=0.8404, semantic=0.8404, dans_contexte=non)  https://www.inalco.fr/inscriptions-pedagogiques
- [5] Inscriptions pédagogiques / Inscriptions pédagogiques (pages=n/a-n/a, score=0.8373, semantic=0.8373, dans_contexte=non)  https://www.inalco.fr/inscriptions-pedagogiques

## q065. Est-il possible de changer d'option, de matière ou de parcours pendant l'année ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `clarify`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Se réorienter / Y a-t-il une date limite pour se réorienter ? (pages=n/a-n/a, score=0.8389, semantic=0.8389, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/information-et-orientation/se-reorienter.html
- [2] Conventions de stage / Puis-je candidater à un stage tout au long de l’année ? (pages=n/a-n/a, score=0.8383, semantic=0.8383, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html
- [3] Construire son projet d'études / DES EVENEMENTS DEDIES A L'ORIENTATION (pages=n/a-n/a, score=0.8356, semantic=0.8356, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/information-et-orientation/construire-son-projet-d-etudes.html
- [4] Construire son projet d'études / **DES EVENEMENTS DEDIES A L'ORIENTATION** (pages=n/a-n/a, score=0.8354, semantic=0.8354, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/information-et-orientation/construire-son-projet-d-etudes.html
- [5] Conventions de stage / Dois-je garder la même tutrice ou le même tuteur de stage durant tout mon cursus (en M1 et M2) ? (pages=n/a-n/a, score=0.8354, semantic=0.8354, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html

## q066. Comment trouver les coordonnées de mon gestionnaire ou de mon secrétariat pédagogique ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Annuaire / Contacts (pages=n/a-n/a, score=0.8491, semantic=0.8491, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/annuaire.html
- [2] Consulter ses notes et son certificat de scolarité / 1-Se connecter au Portail Étudiant (pages=n/a-n/a, score=0.843, semantic=0.843, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [3] Annuaire / Contacts (pages=n/a-n/a, score=0.8417, semantic=0.8417, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/annuaire.html
- [4] Tutorat / Tuteurs : à qui vous adresser ? (pages=n/a-n/a, score=0.8402, semantic=0.8402, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/tutorat.html
- [5] Parcours L1+ / Inscriptions (pages=n/a-n/a, score=0.8389, semantic=0.8389, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/accompagnement-vers-la-reussite/parcours-l1.html

**Faits de référence (non transmis au modèle) :**

- L'annuaire de l'Inalco réunit les coordonnées des services et composantes
- Le secrétariat ou le gestionnaire compétent dépend du département, de la langue ou de la filière de l'étudiant
- Le standard de l'Inalco peut transférer les appels vers le service concerné au 01 81 70 10 00

## q067. Qui dois-je prévenir en cas d'absence à un cours ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Droits de scolarité : tarifs, exonération, annulation, remboursement / Annulation et remboursement d'inscription (pages=n/a-n/a, score=0.8161, semantic=0.8161, dans_contexte=non)  https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement
- [2] Tutorat / Vous êtes étudiant en L1, L2, L3 LLCER : (pages=n/a-n/a, score=0.8156, semantic=0.8156, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/tutorat.html
- [3] Psychologue / **Dispositif Santé Psy Étudiant** (pages=n/a-n/a, score=0.8154, semantic=0.8154, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/suivi-par-des-professionnels/psychologue.html
- [4] Inscriptions pédagogiques / Inscriptions pédagogiques (pages=n/a-n/a, score=0.8149, semantic=0.8149, dans_contexte=non)  https://www.inalco.fr/inscriptions-pedagogiques
- [5] Urgences / **Urgences médicales** (pages=n/a-n/a, score=0.8146, semantic=0.8146, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/urgences.html

## q069. Où trouver les dates et les salles de mes prochains examens ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Dates et calendriers / Comment utiliser le planning des cours (pages=n/a-n/a, score=0.8438, semantic=0.8438, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html
- [2] Dates et calendriers / Comment utiliser le planning des cours (pages=n/a-n/a, score=0.8435, semantic=0.8435, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html
- [3] Examens / Examens (pages=n/a-n/a, score=0.8411, semantic=0.8411, dans_contexte=non)  https://www.inalco.fr/examens
- [4] Consulter ses notes et son certificat de scolarité / 1-Se connecter au Portail Étudiant (pages=n/a-n/a, score=0.841, semantic=0.841, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [5] Sans titre / Prochains évènements (pages=n/a-n/a, score=0.8405, semantic=0.8405, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/footer.html

**Faits de référence (non transmis au modèle) :**

- La rubrique Examens du portail étudiant contient des sous-pages pour les examens du premier semestre, du second semestre et les rattrapages
- Les informations publiées sur ces sous-pages permettent de consulter l'organisation des sessions correspondantes

## q070. Comment fonctionnent les examens de rattrapage à l'Inalco ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Bien-être / Relax' Exams (pages=n/a-n/a, score=0.8546, semantic=0.8546, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/bien-etre.html
- [2] Examens / Examens (pages=n/a-n/a, score=0.8544, semantic=0.8544, dans_contexte=non)  https://www.inalco.fr/examens
- [3] Mission Handicap / Demande d'aménagement d'examen (pages=n/a-n/a, score=0.851, semantic=0.851, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [4] Faire sa rentrée à l'Inalco / Bienvenue à l'Inalco ! (pages=n/a-n/a, score=0.8503, semantic=0.8503, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juillet-2026/faire-sa-rentree.html
- [5] FAQ Admission en Master / Y a-t-il des examens/concours d’entrée pour certains Masters ? (pages=n/a-n/a, score=0.8498, semantic=0.8498, dans_contexte=non)  https://www.inalco.fr/faq-admission-en-master

## q073. Où consulter les règlements des études et les modalités de contrôle des connaissances ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Règlements et chartes étudiantes / Modalités de contrôle des connaissances (pages=n/a-n/a, score=0.8557, semantic=0.8557, dans_contexte=non)  https://www.inalco.fr/reglements-et-chartes-etudiantes
- [2] Règlements et chartes étudiantes / Annexes aux MCC (pages=n/a-n/a, score=0.8456, semantic=0.8456, dans_contexte=non)  https://www.inalco.fr/reglements-et-chartes-etudiantes
- [3] Règlements et chartes étudiantes / Charte de bon usage des outils de visioconférence (pages=n/a-n/a, score=0.8363, semantic=0.8363, dans_contexte=non)  https://www.inalco.fr/reglements-et-chartes-etudiantes
- [4] Règlements et chartes étudiantes / Charte des examens (pages=n/a-n/a, score=0.8339, semantic=0.8339, dans_contexte=non)  https://www.inalco.fr/reglements-et-chartes-etudiantes
- [5] Etudier à l'étranger / Responsables des Relations Internationales (RRI) des départements : (pages=n/a-n/a, score=0.8329, semantic=0.8329, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger.html

**Faits de référence (non transmis au modèle) :**

- Les modalités de contrôle des connaissances sont publiées dans la rubrique Règlements et chartes étudiantes
- Elles couvrent les modes d'évaluation, le calcul des résultats, la compensation et la capitalisation
- Elles précisent aussi le passage en année supérieure et les règles d'assiduité
- Des annexes spécifiques sont publiées pour certains dispositifs ou formations

## q074. Comment demander un aménagement d'études ou d'examens en raison d'un handicap ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Mission Handicap / Procédure de la mise en place du plan d'accompagnement (PAEH) (pages=n/a-n/a, score=0.8607, semantic=0.8607, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [2] Mission Handicap / Demande d'aménagement d'examen (pages=n/a-n/a, score=0.8593, semantic=0.8593, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [3] Mission Handicap / Etudiants sans PAEH (pages=n/a-n/a, score=0.8581, semantic=0.8581, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [4] Mission Handicap / Procédure de la mise en place du plan d'accompagnement (PAEH) (pages=n/a-n/a, score=0.8532, semantic=0.8532, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [5] Mission Handicap / Procédure de la mise en place du plan d'accompagnement (PAEH) (pages=n/a-n/a, score=0.8518, semantic=0.8518, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html

**Faits de référence (non transmis au modèle) :**

- Une demande d'aménagement d'examen nécessite un PAEH validé par la Mission Handicap
- Le formulaire doit être rempli pour chaque semestre et chaque session d'examen, y compris les rattrapages
- Les aménagements demandés doivent correspondre à ceux notifiés dans le PAEH
- Le formulaire doit être envoyé après la publication des dates d'examen

## q075. À qui m'adresser en cas de difficulté personnelle ou de mal-être ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Santé / Psychologue de l'Inalco (pages=n/a-n/a, score=0.8323, semantic=0.8323, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/sante.html
- [2] Urgences / **SOS suicide** (pages=n/a-n/a, score=0.8316, semantic=0.8316, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/urgences.html
- [3] Psychologue / **Consultation au centre de santé étudiante** (pages=n/a-n/a, score=0.8241, semantic=0.8241, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/suivi-par-des-professionnels/psychologue.html
- [4] Mission Handicap / Mission Handicap (pages=n/a-n/a, score=0.8237, semantic=0.8237, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [5] Santé / Acca : la ligne d’écoute et soutien psychologique (pages=n/a-n/a, score=0.8203, semantic=0.8203, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/sante.html

**Faits de référence (non transmis au modèle) :**

- Un rendez-vous avec la psychologue de l'Inalco peut être demandé à soutien-psy@inalco.fr
- Les consultations peuvent concerner notamment le stress, la dépression, les difficultés relationnelles, l'alimentation ou les addictions
- Les consultations psychologiques sont confidentielles
- En cas d'idées suicidaires, le 3114 est disponible 24 heures sur 24 et le 15 doit être appelé en cas d'urgence médicale

## q076. Quels services de santé sont accessibles aux étudiantes et étudiants ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Etudiants Relais Santé (ERS) / Le Service de Santé Étudiant (SSE) (pages=n/a-n/a, score=0.8572, semantic=0.8572, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/etudiants-relais-sante-ers.html
- [2] Santé / Consultation médicale et médecine préventive (pages=n/a-n/a, score=0.856, semantic=0.856, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/sante.html
- [3] Etudiants Relais Santé (ERS) / Leurs missions (pages=n/a-n/a, score=0.8545, semantic=0.8545, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/etudiants-relais-sante-ers.html
- [4] Etudiants Relais Santé (ERS) / Présentation (pages=n/a-n/a, score=0.8492, semantic=0.8492, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/etudiants-relais-sante-ers.html
- [5] Santé, sport et bien-être / Santé, sport et bien-être (pages=n/a-n/a, score=0.8448, semantic=0.8448, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre.html

**Faits de référence (non transmis au modèle) :**

- Le Service de Santé Étudiante propose des consultations aux étudiants
- Son équipe comprend notamment des médecins, psychologues, infirmières, sages-femmes et professionnels de la nutrition
- Les consultations sont confidentielles
- Le tiers payant intégral est appliqué sur présentation des justificatifs nécessaires selon la page collectée

## q078. Comment prendre rendez-vous avec l'assistante sociale de l'Inalco ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5960 caractères`

**Reponse :**

Pour prendre rendez-vous avec l'assistante sociale de l'Inalco, vous pouvez envoyer un mail à l'adresse suivante : [assistance-sociale@inalco.fr](mailto:assistance-sociale@inalco.fr).

Sources :
- [Assistance sociale](https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/suivi-par-des-professionnels/assistance-sociale.html)

**Sources recuperees :**

- [1] Assistance sociale / À l'Inalco (pages=n/a-n/a, score=0.8807, semantic=0.8807, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/suivi-par-des-professionnels/assistance-sociale.html
- [2] Mission Handicap / Procédure de la mise en place du plan d'accompagnement (PAEH) (pages=n/a-n/a, score=0.8649, semantic=0.8649, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [3] Mission Handicap / Procédure de la mise en place du plan d'accompagnement (PAEH) (pages=n/a-n/a, score=0.8599, semantic=0.8599, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [4] Mission Handicap / Mission Handicap (pages=n/a-n/a, score=0.8588, semantic=0.8588, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [5] Assistance sociale / En dehors de l'Inalco (pages=n/a-n/a, score=0.8585, semantic=0.8585, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/suivi-par-des-professionnels/assistance-sociale.html

**Faits de référence (non transmis au modèle) :**

- La prise de rendez-vous avec l'assistante sociale de l'Inalco se fait par courriel
- L'adresse indiquée est assistance-sociale@inalco.fr

## q079. Qui contacter en cas d'urgence médicale ou de problème de sécurité dans l'établissement ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Urgences / Reporter un incident au sein de l’établissement (pages=n/a-n/a, score=0.8578, semantic=0.8578, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/urgences.html
- [2] Urgences / **Reporter un incident au sein de l’établissement** (pages=n/a-n/a, score=0.8549, semantic=0.8549, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/urgences.html
- [3] Urgences / Urgences médicales (pages=n/a-n/a, score=0.8488, semantic=0.8488, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/urgences.html
- [4] Urgences / **Urgences médicales** (pages=n/a-n/a, score=0.8455, semantic=0.8455, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/urgences.html
- [5] Urgences / **SOS suicide** (pages=n/a-n/a, score=0.8426, semantic=0.8426, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/urgences.html

**Faits de référence (non transmis au modèle) :**

- Pour une urgence de sécurité ou de santé dans l'établissement, la ligne dédiée est le 01 81 69 18 19
- Depuis un poste interne, le numéro est le 3000
- Le Poste de Contrôle Sécurité se trouve au rez-de-chaussée
- En dehors de l'établissement, une urgence médicale peut être signalée au 15 ou au 112
- Une personne blessée ne doit pas être déplacée sauf en cas de danger immédiat

## q080. Quelles bourses et aides financières sont accessibles aux étudiants inscrits ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Bourses et aides sociales / Bourses et aides sociales (pages=n/a-n/a, score=0.8561, semantic=0.8561, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-aides-sociales.html
- [2] Lancement de la campagne de bourse et de logement étudiant 2026-2027 / Quels sont les avantages d'être boursier ou boursière ? (pages=n/a-n/a, score=0.8547, semantic=0.8547, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html
- [3] Lancement de la campagne de bourse et de logement étudiant 2026-2027 / Quels sont les avantages d'être boursier ou boursière ? (pages=n/a-n/a, score=0.8537, semantic=0.8537, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html
- [4] Bourses et aides sociales / Aides exceptionnels du CROUS (pages=n/a-n/a, score=0.8513, semantic=0.8513, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-aides-sociales.html
- [5] Bourses et aides sociales / Aide contre la précarité (pages=n/a-n/a, score=0.85, semantic=0.85, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-aides-sociales.html

**Faits de référence (non transmis au modèle) :**

- L'Inalco présente différentes aides sociales et bourses destinées aux étudiants
- Les étudiants boursiers peuvent bénéficier d'une priorité pour l'attribution de logements
- Ils peuvent être exonérés des droits d'inscription et de la CVEC
- L'aide au mérite et le Pass'Sport figurent parmi les avantages mentionnés

## q082. Comment demander l'aide au voyage proposée par l'Inalco ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4994 caractères`

**Reponse :**

Pour demander l'aide au voyage proposée par l'Inalco, vous pouvez suivre les étapes suivantes :

1. **Réunion d'information** : Une réunion d'information aura lieu le jeudi 27 novembre 2025 à 18h15 en amphi 1. Cette réunion vous apportera tous les détails nécessaires sur les modalités, le montant, les critères de sélection et le calendrier.

2. **Exposition photo** : Vous pouvez également vous rendre dans le hall 2 pour découvrir l’exposition photo des camarades partis l’été dernier grâce à l’aide au voyage. L’exposition se tiendra les 27 et 28 novembre 2025.

3. **Documents utiles** : Si vous avez raté la réunion d'information, vous pouvez retrouver tous les détails dans les documents de présentation disponibles à la section "Documents utiles" sur la page officielle.

Pour plus d'informations, consultez la page dédiée à l'aide au voyage sur le portail étudiant de l'Inalco : [Aide au voyage](https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/aide-au-voyage.html).

Sources :
- [Aide au voyage](https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/aide-au-voyage.html)

**Sources recuperees :**

- [1] Aide au voyage / Venez vous renseigner ! (pages=n/a-n/a, score=0.8736, semantic=0.8736, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/aide-au-voyage.html
- [2] Aide au voyage / Venez vous renseigner ! (pages=n/a-n/a, score=0.873, semantic=0.873, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/aide-au-voyage.html
- [3] Aide au voyage / Quand partir ? (pages=n/a-n/a, score=0.8716, semantic=0.8716, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/aide-au-voyage.html
- [4] Missions de vacations étudiantes rémunérées : appel à candidatures / Le dispositif Soutien numérique (pages=n/a-n/a, score=0.8701, semantic=0.8701, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juillet-2026/missions-de-vacations-etudiantes-remunerees-appel-a-candidatures.html
- [5] Aide au voyage / Autres aides (pages=n/a-n/a, score=0.869, semantic=0.869, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/aide-au-voyage.html

**Faits de référence (non transmis au modèle) :**

- L'aide au voyage finance une partie des frais de transport pour une immersion dans un pays dont l'étudiant étudie la langue
- Le voyage doit durer au minimum 14 jours et au maximum 75 jours
- Pour la campagne collectée, le formulaire en ligne est ouvert à partir du 10 décembre 2025
- Le dossier et les pièces justificatives doivent être déposés avant le 16 février 2026 à 15h
- Le résultat est annoncé par courriel à partir du 8 avril 2026

## q083. Comment candidater à une mobilité Erasmus+ ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `True`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Pour quelle formation et quel niveau d'entrée souhaitez-vous connaître les dates de candidature ?

**Sources recuperees :**


**Faits de référence (non transmis au modèle) :**

- Le candidat doit consulter la charte Erasmus+ et la liste des partenariats
- Il doit discuter de son projet avec le responsable des relations internationales de son département et les responsables pédagogiques concernés
- Le dossier est déposé au moyen d'un formulaire en ligne
- Il comprend notamment un CV, une lettre de motivation, un projet de mobilité de 30 ECTS par semestre, un certificat de scolarité et les relevés de notes
- Une campagne principale et une campagne complémentaire sont organisées selon les calendriers annoncés

## q084. Quelles possibilités de mobilité hors Erasmus+ sont proposées ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `4556 caractères`

**Reponse :**

Les possibilités de mobilité hors Erasmus+ proposées par l'Inalco incluent :

1. **Bourse de mobilité internationale (hors Erasmus+)** : Gérée par le service Réussite et Vie Étudiante, cette bourse n'est pas cumulable avec d'autres aides au voyage.

2. **Programme France Éducation International** : Ce programme permet d'affecter des assistants de langue française dans des établissements scolaires ou universitaires pour une durée comprise entre 4, 5 et 12 mois selon les destinations. Les campagnes de recrutement ouvrent en janvier, avec des dates limites qui diffèrent selon les pays.

3. **Séjour d'études - mobilité en cursus intégré** : Dans le cadre d'un partenariat avec des universités partenaires, les étudiants peuvent bénéficier d'une exonération des frais d'inscription de l'université d'accueil. La candidature se prépare l'année universitaire qui précède l'année de la mobilité. La liste des universités partenaires est disponible lors de l'ouverture du formulaire de candidature.

Sources :
- [Mobilités hors Erasmus+](https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-hors-erasmus.html)

**Sources recuperees :**

- [1] Mobilités hors Erasmus+ / La bourse de mobilité internationale (hors Erasmus+) (pages=n/a-n/a, score=0.8896, semantic=0.8896, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-hors-erasmus.html
- [2] Mobilités hors Erasmus+ / Comment préparer une mobilité internationale hors Europe ? (pages=n/a-n/a, score=0.8832, semantic=0.8832, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-hors-erasmus.html
- [3] Mobilités hors Erasmus+ / Mobilités hors Erasmus+ (pages=n/a-n/a, score=0.8816, semantic=0.8816, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-hors-erasmus.html
- [4] Mobilités Erasmus+ / Quel sera le montant de ma bourse Erasmus+ ? (pages=n/a-n/a, score=0.8756, semantic=0.8756, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-erasmus.html
- [5] Mobilités Erasmus+ / Mobilités Erasmus+ (pages=n/a-n/a, score=0.8753, semantic=0.8753, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-erasmus.html

**Faits de référence (non transmis au modèle) :**

- Une mobilité hors Erasmus+ peut prendre la forme d'un séjour d'études dans une université partenaire hors Europe
- Les étudiants participant à un accord d'échange sont exonérés des frais d'inscription de l'université d'accueil
- La candidature se prépare pendant l'année universitaire précédant la mobilité
- Le programme d'assistants de langue française constitue une autre possibilité de mobilité
- L'aide au voyage de l'Inalco peut contribuer au financement de certains projets

## q085. Comment trouver un stage et faire établir une convention de stage ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Conventions de stage / **DÉLAIS** (pages=n/a-n/a, score=0.8689, semantic=0.8689, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html
- [2] Conventions de stage / Où puis-je trouver des offres de stages à l’Inalco ? (pages=n/a-n/a, score=0.8689, semantic=0.8689, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html
- [3] Conventions de stage / **CRITÈRES ET DÉMARCHES** (pages=n/a-n/a, score=0.8659, semantic=0.8659, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html
- [4] Conventions de stage / CRITÈRES ET DÉMARCHES (pages=n/a-n/a, score=0.8622, semantic=0.8622, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html
- [5] Conventions de stage / **CRITÈRES ET DÉMARCHES** (pages=n/a-n/a, score=0.8609, semantic=0.8609, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html

**Faits de référence (non transmis au modèle) :**

- Les offres de stage sont consultables auprès du SIO-IP et sur la plateforme JobTeaser
- Le cursus doit comporter au moins 200 heures de cours dans l'année pour ouvrir droit à une convention de stage
- Certains diplômes d'établissement et les Passeports Langues O' ne donnent pas droit à une convention
- Le dossier de convention doit être complet et signé par les parties requises
- Le dossier doit être déposé au plus tard quatre jours ouvrés avant le début du stage

## q086. Comment bénéficier d'un accompagnement pour l'orientation et l'insertion professionnelle ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Se réorienter / **LA FICHE DE REORIENTATION** (pages=n/a-n/a, score=0.8543, semantic=0.8543, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/information-et-orientation/se-reorienter.html
- [2] Inalco Career Center Job Teaser / **CE QUE VOUS Y TROUVEREZ** (pages=n/a-n/a, score=0.8536, semantic=0.8536, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/construire-son-projet-pro/inalco-career-center-job-teaser.html
- [3] Prendre RDV avec un conseiller / PRENDRE RENDEZ-VOUS (pages=n/a-n/a, score=0.8525, semantic=0.8525, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/prendre-rdv-avec-un-conseiller.html
- [4] Prendre RDV avec un conseiller / LE SERVICE DU SIO-IP (pages=n/a-n/a, score=0.8494, semantic=0.8494, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/prendre-rdv-avec-un-conseiller.html
- [5] Construire son projet pro / Construire son projet pro (pages=n/a-n/a, score=0.8479, semantic=0.8479, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/construire-son-projet-pro.html

**Faits de référence (non transmis au modèle) :**

- Le SIO-IP accompagne les étudiants dans l'orientation et l'insertion professionnelle
- Des rendez-vous individuels sont proposés avec la PsyEN et l'équipe du SIO-IP
- Le Career Center JobTeaser diffuse des offres de stage, d'emploi, de job étudiant, de vacation et de service civique
- Le SIO-IP gère également les conventions de stage et diffuse des offres
- Le service est situé au deuxième étage du Pôle des langues et civilisations

## q088. Comment payer mes repas avec Izly et que faire si mon compte ne fonctionne pas ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5922 caractères`

**Reponse :**

Pour payer vos repas avec Izly, vous devez utiliser votre carte étudiante multiservice. Cette carte contient un compte en ligne Izly, que vous pouvez recharger directement depuis votre compte bancaire via le site izly.fr ou l'application Izly disponible sur les principaux stores de téléchargement.

Si votre compte ne fonctionne pas, vérifiez l'adresse de courriel que vous avez donnée au service de la scolarité ainsi que vos SPAM. Vous pouvez également réinitialiser votre carte en début d'année universitaire sur les bornes prévues à cet effet au premier étage de l'Inalco.

Sources :
- [Se nourrir](https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html)
- [Services et ressources numériques](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html)

**Sources recuperees :**

- [1] Se nourrir / Comment payer ? (pages=n/a-n/a, score=0.8812, semantic=0.8812, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html
- [2] Services et ressources numériques / Scolarité (pages=n/a-n/a, score=0.8677, semantic=0.8677, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [3] Services et ressources numériques / Carte multi-services étudiante (pages=n/a-n/a, score=0.8509, semantic=0.8509, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [4] Services et ressources numériques / Scolarité (pages=n/a-n/a, score=0.8481, semantic=0.8481, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [5] Se nourrir / Restaurant Universitaire de la Halle aux farines (pages=n/a-n/a, score=0.8388, semantic=0.8388, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html

## q089. Comment demander un logement en résidence universitaire auprès du Crous ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4724 caractères`

**Reponse :**

Pour demander un logement en résidence universitaire auprès du Crous, vous devez suivre les étapes suivantes :

1. **Bourse et Logement** : Les résidences universitaires du Crous de Paris sont réservées en priorité aux personnes étudiantes boursières selon des critères sociaux. Vous devez donc d'abord vérifier votre éligibilité à une bourse sur critères sociaux.

2. **Dossier Social Étudiant (DSE)** : La demande de DSE est à faire sur le site [messervices.etudiant.gouv.fr](https://messervices.etudiant.gouv.fr) avant le 31 mai 2026 pour permettre un traitement du dossier dans les meilleurs délais et de pouvoir bénéficier de la mise en paiement de la bourse dès la rentrée, au mois de septembre. Les dossiers remplis et traités avant le 31 mai 2026 sont prioritaires pour une demande de logement Crous.

3. **Consultation du Site du Crous** : Une fois votre éligibilité à une bourse confirmée, vous pouvez consulter directement le site du Crous de Paris pour découvrir comment effectuer une demande de logement dans une résidence du Crous.

4. **Contact** : Pour toutes les demandes d'information, vous pouvez contacter le Crous au numéro 09 72 59 65 65.

Sources :
- [Se loger](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html)
- [Lancement de la campagne de bourse et de logement étudiant 2026-2027](https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html)
- [Bourses et aides sociales](https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-aides-sociales.html)

**Sources recuperees :**

- [1] Se loger / Comment obtenir un logement en résidence universitaire ? (pages=n/a-n/a, score=0.9043, semantic=0.9043, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html
- [2] Se loger / A qui sont réservés les logements en résidence universitaire parisienne ? (pages=n/a-n/a, score=0.8886, semantic=0.8886, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html
- [3] Se loger / Comment contacter le CROUS ? (pages=n/a-n/a, score=0.87, semantic=0.87, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html
- [4] Lancement de la campagne de bourse et de logement étudiant 2026-2027 / Où et quand faire sa demande ? (pages=n/a-n/a, score=0.8612, semantic=0.8612, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html
- [5] Bourses et aides sociales / Bourses sur critères sociaux du CROUS (pages=n/a-n/a, score=0.8567, semantic=0.8567, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-aides-sociales.html

**Faits de référence (non transmis au modèle) :**

- La demande de logement en résidence universitaire passe par le Crous
- Les résidences du Crous sont attribuées en priorité aux étudiants boursiers selon des critères sociaux
- Le nombre de places est limité et la candidature doit être déposée dès l'ouverture de la procédure
- Le numéro d'information Crous indiqué est le 09 72 59 65 65

## q090. Comment accéder à distance aux ressources numériques de la bibliothèque ou de la médiathèque ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Services et ressources numériques / Services et ressources numériques (pages=n/a-n/a, score=0.8465, semantic=0.8465, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [2] Services et ressources numériques / Outils collaboratifs et services proposés (pages=n/a-n/a, score=0.8414, semantic=0.8414, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [3] Services et ressources numériques / Wi-Fi (pages=n/a-n/a, score=0.8393, semantic=0.8393, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [4] Services et ressources numériques / Fonds documentaire (pages=n/a-n/a, score=0.8378, semantic=0.8378, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [5] Services et ressources numériques / Outils collaboratifs et services proposés (pages=n/a-n/a, score=0.8373, semantic=0.8373, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html

## q092. Comment rejoindre une association étudiante de l'Inalco ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5222 caractères`

**Reponse :**

Pour rejoindre une association étudiante de l'Inalco, vous pouvez consulter la page dédiée aux associations étudiantes sur le portail étudiant de l'Inalco. Cette page vous permettra de découvrir les différentes associations et de les contacter pour adhérer ou devenir membre actif. Vous y trouverez également des informations sur la création et la gestion d'une association étudiante reconnue à l'Inalco.

Sources :
- [Associations étudiantes](https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations.html)
- [Association étudiante : mode d'emploi](https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/creer-et-gerer-une-association/association-etudiante-mode-d-emploi.html)

**Sources recuperees :**

- [1] Associations étudiantes / Associations étudiantes (pages=n/a-n/a, score=0.8807, semantic=0.8807, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations.html
- [2] Association étudiante : mode d'emploi / Association étudiante : mode d'emploi (pages=n/a-n/a, score=0.88, semantic=0.88, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/creer-et-gerer-une-association/association-etudiante-mode-d-emploi.html
- [3] Faire sa rentrée à l'Inalco / Bienvenue à l'Inalco ! (pages=n/a-n/a, score=0.8767, semantic=0.8767, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juillet-2026/faire-sa-rentree.html
- [4] Être accompagné / International Buddies (pages=n/a-n/a, score=0.8746, semantic=0.8746, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/etre-accompagne.html
- [5] Rejoindre des communautés / Accéder au catalogue (pages=n/a-n/a, score=0.8742, semantic=0.8742, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/rejoindre-des-communautes.html

**Faits de référence (non transmis au modèle) :**

- L'Inalco compte plus de vingt associations étudiantes reconnues
- Les pages des associations permettent de découvrir leurs activités et leurs coordonnées
- Pour adhérer ou devenir membre actif, l'étudiant peut contacter directement l'association concernée

## q093. Comment créer et faire reconnaître une nouvelle association étudiante ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Association étudiante : mode d'emploi / **I/Rédiger des statuts** (pages=n/a-n/a, score=0.8578, semantic=0.8578, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/creer-et-gerer-une-association/association-etudiante-mode-d-emploi.html
- [2] Créer et gérer une association / Créer et gérer une association (pages=n/a-n/a, score=0.8571, semantic=0.8571, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/creer-et-gerer-une-association.html
- [3] Association étudiante : mode d'emploi / Association étudiante : mode d'emploi (pages=n/a-n/a, score=0.8532, semantic=0.8532, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/creer-et-gerer-une-association/association-etudiante-mode-d-emploi.html
- [4] Association étudiante : mode d'emploi / Aides financières (pages=n/a-n/a, score=0.8526, semantic=0.8526, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/creer-et-gerer-une-association/association-etudiante-mode-d-emploi.html
- [5] Associations étudiantes / Associations étudiantes (pages=n/a-n/a, score=0.8515, semantic=0.8515, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations.html

**Faits de référence (non transmis au modèle) :**

- Une association étudiante peut demander à être reconnue par l'Inalco
- Les membres fondateurs doivent notamment préparer des statuts et se réunir en assemblée constitutive
- L'assemblée constitutive adopte les statuts et désigne les membres du bureau
- Les décisions de l'assemblée constitutive sont consignées dans un procès-verbal

## q094. Comment faire reconnaître et valoriser mon engagement étudiant dans mon cursus ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4628 caractères`

**Reponse :**

Pour faire reconnaître et valoriser votre engagement étudiant dans votre cursus à l'Inalco, vous devez être inscrit en Licence (L1, L2, L3), en Master 1, ou en diplôme d'établissement (à l’exclusion des diplômes d’établissement à distance et des diplômes intensifs).

La valorisation de votre engagement peut se faire de deux manières :
1. **Reconnaissance pédagogique** : Si vous êtes inscrit en Licence ou en diplôme d’établissement dans un niveau comportant une UE libre, votre engagement peut être reconnu sous la forme d’un EC « Engagement étudiant » affecté de 3 crédits ECTS. Cet EC est validé sans note au second semestre de l’année universitaire.
2. **Bonification** : Si vous êtes inscrit en Licence ou en diplôme d’établissement dans un niveau ne comportant pas d’UE libre, ainsi que pour les étudiants inscrits en Master 1, votre engagement peut être valorisé par l’obtention d’une bonification accordée par la Commission de validation de l’engagement étudiant (CV2E). Cette bonification peut être intégrée à votre moyenne annuelle générale de l’étudiant, pour un maximum de 0.5 points / 20.

L’engagement doit être volontaire, bénévole, laïque, et représenter un minimum de 30 heures d’activité durant l’année universitaire au cours de laquelle la valorisation est demandée.

Pour plus de détails, vous pouvez consulter la page officielle sur la valorisation de l’engagement : [Valorisation de l'engagement](https://portail-etudiant.inalco.fr/fr/vie-de-campus/s-engager/valorisation-de-l-engagement.html).

Sources :
- [Valorisation de l'engagement](https://portail-etudiant.inalco.fr/fr/vie-de-campus/s-engager/valorisation-de-l-engagement.html)

**Sources recuperees :**

- [1] Valorisation de l'engagement / Qui est concerné ? (pages=n/a-n/a, score=0.8781, semantic=0.8781, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/s-engager/valorisation-de-l-engagement.html
- [2] Valorisation de l'engagement / Comment faire valider votre action ? (pages=n/a-n/a, score=0.8773, semantic=0.8773, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/s-engager/valorisation-de-l-engagement.html
- [3] Valorisation de l'engagement / Comment votre engagement est-il valorisé ? (pages=n/a-n/a, score=0.8703, semantic=0.8703, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/s-engager/valorisation-de-l-engagement.html
- [4] Valorisation de l'engagement / Valorisation de l'engagement (pages=n/a-n/a, score=0.8695, semantic=0.8695, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/s-engager/valorisation-de-l-engagement.html
- [5] Valorisation de l'engagement / Quelles sont les activités éligibles ? (pages=n/a-n/a, score=0.8688, semantic=0.8688, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/s-engager/valorisation-de-l-engagement.html

**Faits de référence (non transmis au modèle) :**

- L'engagement peut être reconnu pour les étudiants inscrits en licence, en Master 1 ou dans certains diplômes d'établissement
- Selon la formation, il peut prendre la forme d'un EC Engagement étudiant de trois ECTS
- Dans d'autres formations, il peut donner lieu à une bonification proposée par la CV2E
- La validation est inscrite sur le relevé de l'étudiant selon les modalités de sa formation

## q097. Existe-t-il un parking à vélo sur les sites de l'Inalco ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Mission Handicap / Procédure de la mise en place du plan d'accompagnement (PAEH) (pages=n/a-n/a, score=0.8412, semantic=0.8412, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [2] Plan du site / Plan du site (pages=n/a-n/a, score=0.8404, semantic=0.8404, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/footer/autres-liens/plan-du-site.html
- [3] Plan du site / Plan du site (pages=n/a-n/a, score=0.8402, semantic=0.8402, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/footer/autres-liens/plan-du-site.html
- [4] Services et ressources numériques / Scolarité (pages=n/a-n/a, score=0.8402, semantic=0.8402, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [5] Étudiants internationaux à l'Inalco / Contact (pages=n/a-n/a, score=0.8396, semantic=0.8396, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/international/venir-etudier-a-l-inalco.html

## q098. Où se trouvent les fontaines ou distributeurs d'eau dans les bâtiments de l'Inalco ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Vigilance canicule / 1 - Buvez régulièrement de l’eau (pages=n/a-n/a, score=0.8281, semantic=0.8281, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juin-2026/vigilance-canicule.html
- [2] Bien-être / À l'Inalco : (pages=n/a-n/a, score=0.8274, semantic=0.8274, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/bien-etre.html
- [3] Services et ressources numériques / Scolarité (pages=n/a-n/a, score=0.8206, semantic=0.8206, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [4] Schéma Directeur DD&RSE 2025-2030 / Page 21 - Annexe 1. La Convention Environnementale (pages=21-21, score=0.8205, semantic=0.8205, dans_contexte=non)  https://www.inalco.fr/sites/default/files/2025-06/Sch%C3%A9ma%20Directeur%20DD%26RSE%202025.pdf
- [5] Services et ressources numériques / Fonds documentaire (pages=n/a-n/a, score=0.8198, semantic=0.8198, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html

## q100. Quand aura lieu la prochaine réunion du Vivier environnemental ?

**Methode :** `m4_rag_abstention`  
**Experience :** `m4_rag_abstention_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank_threshold_strict`  
**Mode de prompt :** `strict_abstention`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `0`  
**Taille du contexte :** `0 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Schéma Directeur de la Vie Étudiante 2023-2028 / Page 51 - AXE # 3 Agir en faveur du développement dura ble et de l a (pages=51-51, score=0.8195, semantic=0.8195, dans_contexte=non)  https://www.inalco.fr/sites/default/files/2024-05/Sh%C3%A9ma%20Directeur%20de%20la%20Vie%20%C3%89tudiante-avec%20compression.pdf
- [2] Schéma Directeur DD&RSE 2025-2030 / Page 7 - IV. Le plan d’actions et sa méthode (pages=7-7, score=0.8192, semantic=0.8192, dans_contexte=non)  https://www.inalco.fr/sites/default/files/2025-06/Sch%C3%A9ma%20Directeur%20DD%26RSE%202025.pdf
- [3] Catalogue de cours et de formations EUniWell : la sélection de mars 2026 / Bien-être et résilience (pages=n/a-n/a, score=0.8185, semantic=0.8185, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/catalogue-de-cours-et-de-formations-euniwell-la-selection-de-mars-2026.html
- [4] Schéma Directeur DD&RSE 2025-2030 / Page 4 - I. Les enjeux environnementaux et sociaux (pages=4-4, score=0.8174, semantic=0.8174, dans_contexte=non)  https://www.inalco.fr/sites/default/files/2025-06/Sch%C3%A9ma%20Directeur%20DD%26RSE%202025.pdf
- [5] Schéma Directeur de la Vie Étudiante 2023-2028 / Page 51 - AXE # 3 Agir en faveur du développement dura ble et de l a (pages=51-51, score=0.8168, semantic=0.8168, dans_contexte=non)  https://www.inalco.fr/sites/default/files/2024-05/Sh%C3%A9ma%20Directeur%20de%20la%20Vie%20%C3%89tudiante-avec%20compression.pdf

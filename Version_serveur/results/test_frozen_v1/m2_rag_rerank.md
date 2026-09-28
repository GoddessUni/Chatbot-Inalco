# Reponses du prototype Inalco + vLLM

## q002. Quelles sont les principales formations diplômantes proposées par l'Inalco ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `3575 caractères`

**Reponse :**

Les principales formations diplômantes proposées par l'Inalco incluent :

- **Diplôme d'initiation (DIN)**
- **Diplôme intensif**
- **Diplôme de langue et civilisation (DLC)**
- **Diplôme de langue (DL)**
- **Diplôme de civilisation (DC)**
- **Diplôme professionnel de commerce international et langue orientale (DP CILO)**
- **Certificat de langue (CL)**
- **Certificat de langue et civilisation (CLC)**

Ces formations sont principalement axées sur l’acquisition de connaissances et de compétences relatives à une langue et sa civilisation, ou sur la connaissance pointue avec une approche pluridisciplinaire d’une région.

Sources :
- [Diplômes d'établissement](https://www.inalco.fr/formations/diplomes-detablissement)
- [Formations diplômantes](https://www.inalco.fr/formations-diplomantes)
- [Candidater à un cursus diplômant](https://www.inalco.fr/candidater-un-cursus-diplomant)
- [Nos formations proposées en diplômes d'établissement](https://www.inalco.fr/formations/diplomes-detablissement)
- [Nos formations](https://www.inalco.fr/nos-formations)

**Sources recuperees :**

- [1] Diplômes d'établissement / Diplômes d'établissement (pages=n/a-n/a, score=0.8969, semantic=0.8789, dans_contexte=oui)  https://www.inalco.fr/formations/diplomes-detablissement
- [2] Formations diplômantes / Formations diplômantes (pages=n/a-n/a, score=0.8931, semantic=0.8751, dans_contexte=oui)  https://www.inalco.fr/formations-diplomantes
- [3] Candidater à un cursus diplômant / 1. Choisir sa formation (pages=n/a-n/a, score=0.8836, semantic=0.8776, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [4] Diplômes d'établissement / Nos formations proposées en diplômes d'établissement (pages=n/a-n/a, score=0.883, semantic=0.865, dans_contexte=oui)  https://www.inalco.fr/formations/diplomes-detablissement
- [5] Nos formations / Formations diplômantes (pages=n/a-n/a, score=0.8828, semantic=0.8648, dans_contexte=oui)  https://www.inalco.fr/nos-formations

**Faits de référence (non transmis au modèle) :**

- Les principales formations diplômantes de l'Inalco comprennent les licences, les masters et les doctorats
- L'établissement propose également des diplômes universitaires et des diplômes d'établissement

## q003. Quelle est la différence entre une licence LLCER et un diplôme d'établissement ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5142 caractères`

**Reponse :**

La licence LLCER (Langues, Littératures et Civilisations Étrangères et Régionales) est un diplôme national français qui permet d'acquérir une solide maîtrise d'une ou plusieurs langues étrangères, ainsi que des connaissances approfondies sur les cultures et les civilisations associées. Elle est proposée par l'Inalco et d'autres établissements d'enseignement supérieur en France.

Un diplôme d'établissement, quant à lui, est un diplôme délivré par un établissement d'enseignement supérieur spécifique. À l'Inalco, les diplômes d'établissement peuvent inclure des licences LLCER, des licences professionnalisantes, des licences bilangues, et d'autres parcours spécialisés.

La principale différence entre une licence LLCER et un diplôme d'établissement réside dans le fait que la licence LLCER est un diplôme national reconnu par l'État français, tandis qu'un diplôme d'établissement est un diplôme spécifique à l'établissement qui le délivre. Les deux types de diplômes peuvent être obtenus à l'Inalco, mais ils ont des caractéristiques et des objectifs différents.

Sources :
- [Licence LLCER à parcours professionnalisant](https://www.inalco.fr/formations/licence-llcer-parcours-professionnalisant)
- [Licences LLCER - Brochures](https://www.inalco.fr/licences-llcer-brochures)
- [Licence LLCER à parcours bilangue](https://www.inalco.fr/formations/licence-llcer-parcours-bilangue)
- [Licences LLCER à parcours thématiques et disciplinaires](https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires)

**Sources recuperees :**

- [1] Licence LLCER à parcours professionnalisant / Les parcours (pages=n/a-n/a, score=0.8661, semantic=0.8481, dans_contexte=oui)  https://www.inalco.fr/formations/licence-llcer-parcours-professionnalisant
- [2] Licences LLCER - Brochures / Etudes hébraïques et juives (pages=n/a-n/a, score=0.866, semantic=0.848, dans_contexte=oui)  https://www.inalco.fr/licences-llcer-brochures
- [3] Licence LLCER à parcours bilangue / Licence LLCER à parcours bilangue (pages=n/a-n/a, score=0.8627, semantic=0.8447, dans_contexte=oui)  https://www.inalco.fr/formations/licence-llcer-parcours-bilangue
- [4] Licences LLCER - Brochures / Etudes arabes (pages=n/a-n/a, score=0.8627, semantic=0.8447, dans_contexte=oui)  https://www.inalco.fr/licences-llcer-brochures
- [5] Licences LLCER à parcours thématiques et disciplinaires / En complément des parcours : ouverture, anglais, engagement étudiant (pages=n/a-n/a, score=0.8618, semantic=0.8438, dans_contexte=oui)  https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires

**Faits de référence (non transmis au modèle) :**

- La licence LLCER est un diplôme national organisé en trois années
- Elle associe l'étude d'une langue, de sa civilisation et des enseignements disciplinaires
- Les diplômes d'établissement de l'Inalco sont principalement centrés sur une langue, sa civilisation ou une aire régionale
- Dans ces cursus d'établissement, chaque année peut conduire à un diplôme propre à l'Inalco

## q005. Puis-je commencer une langue à l'Inalco sans l'avoir étudiée auparavant ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `clarify`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5187 caractères`

**Reponse :**

Réponse :
Oui, il est possible de commencer une langue à l'Inalco sans l'avoir étudiée auparavant. Cependant, il est important de vérifier les prérequis linguistiques spécifiques à la formation choisie. Par exemple, pour les cours de Langues et Civilisations, il est souvent exigé d'avoir déjà suivi au moins 200 heures de cours de langue pour certaines langues comme l'arabe, le chinois ou le russe. Pour plus d'informations, il est recommandé de consulter les brochures des Masters ou de contacter le secrétariat pédagogique concerné.

Sources :
- [FAQ Admission en Master](https://www.inalco.fr/faq-admission-en-master)
- [Étudiants internationaux à l'Inalco](https://portail-etudiant.inalco.fr/fr/international/venir-etudier-a-l-inalco.html)

**Sources recuperees :**

- [1] FAQ Admission en Master / DOIS-JE OBLIGATOIREMENT CONNAITRE UNE LANGUE ORIENTALE DE L’INALCO ? (pages=n/a-n/a, score=0.8594, semantic=0.8594, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [2] Étudiants internationaux à l'Inalco / **Cours et conditions linguistiques** (pages=n/a-n/a, score=0.8584, semantic=0.8584, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/international/venir-etudier-a-l-inalco.html
- [3] FAQ Admission en Master / Une question sur l'admission en Master à l'Inalco? (pages=n/a-n/a, score=0.8584, semantic=0.8584, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [4] Master TI - Traduction spécialisée / FAQ (pages=n/a-n/a, score=0.8582, semantic=0.8582, dans_contexte=oui)  https://www.inalco.fr/formations/master-ti-traduction-specialisee
- [5] Master TI - Traduction spécialisée / FAQ (pages=n/a-n/a, score=0.8533, semantic=0.8533, dans_contexte=non)  https://www.inalco.fr/formations/master-ti-traduction-specialisee

## q006. Quels sont les prérequis pour entrer en première année de licence LLCER ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5026 caractères`

**Reponse :**

Pour entrer en première année de licence LLCER à parcours bilangue à l'Inalco, il n'y a pas de prérequis spécifiques mentionnés dans le contexte fourni. Les préinscriptions pour l'année 2026-2027 seront ouvertes du 16 février au 15 avril 2026. Pour plus d'informations, vous pouvez consulter le livret de la licence LLCER 2026-2027 disponible sur le site de l'Inalco.

Sources :
- [Licence LLCER à parcours bilangue](https://www.inalco.fr/formations/licence-llcer-parcours-bilangue)

**Sources recuperees :**

- [1] Licence LLCER à parcours bilangue / Licence LLCER à parcours bilangue (pages=n/a-n/a, score=0.8939, semantic=0.8759, dans_contexte=oui)  https://www.inalco.fr/formations/licence-llcer-parcours-bilangue
- [2] Licence LLCER à parcours bilangue / Licence LLCER à parcours bilangue (pages=n/a-n/a, score=0.8904, semantic=0.8724, dans_contexte=oui)  https://www.inalco.fr/formations/licence-llcer-parcours-bilangue
- [3] Licence LLCER à parcours professionnalisant / Les parcours (pages=n/a-n/a, score=0.8891, semantic=0.8711, dans_contexte=oui)  https://www.inalco.fr/formations/licence-llcer-parcours-professionnalisant
- [4] Licence LLCER à parcours bilangue / Documentation et complément d'information (pages=n/a-n/a, score=0.882, semantic=0.864, dans_contexte=oui)  https://www.inalco.fr/formations/licence-llcer-parcours-bilangue
- [5] Licences LLCER à parcours thématiques et disciplinaires / Organisation des parcours thématiques et disciplinaires (pages=n/a-n/a, score=0.8819, semantic=0.8639, dans_contexte=non)  https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires

**Faits de référence (non transmis au modèle) :**

- Une candidature en première année de licence s'effectue par Parcoursup
- Le candidat doit consulter la fiche Parcoursup et la brochure de la formation visée
- Certaines langues peuvent prévoir des indications de niveau ou des modalités particulières précisées dans leur fiche de formation

## q008. Dois-je obligatoirement passer par Parcoursup pour entrer en licence ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `4795 caractères`

**Reponse :**

Pour intégrer la première année de Licence à l'Inalco, vous devez suivre la procédure Parcoursup. Cette plateforme nationale de préinscription en première année de l’enseignement supérieur en France est utilisée pour formuler des vœux en phase d'admission principale du 19 janvier au 12 mars 2026 à 23h59, et en phase complémentaire du 11 juin 2026 jusqu'au 8 septembre 2026, 23h59 heure de Paris.

Sources :
- [Candidatures](https://www.inalco.fr/candidatures)

**Sources recuperees :**

- [1] Candidatures / CANDIDATER EN LICENCE 1 (L.AS INCLUSE) (pages=n/a-n/a, score=0.8744, semantic=0.8504, dans_contexte=oui)  https://www.inalco.fr/candidatures
- [2] FAQ Admission en Master / Puis-je candidater et suivre 2 Masters en parallèle ? (pages=n/a-n/a, score=0.8639, semantic=0.8279, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [3] Inscriptions administratives / Procédure d'inscription administrative (pages=n/a-n/a, score=0.8627, semantic=0.8447, dans_contexte=oui)  https://www.inalco.fr/inscriptions-administratives
- [4] Candidater à un cursus diplômant / Candidater en Master (pages=n/a-n/a, score=0.8603, semantic=0.8243, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [5] Candidatures / CANDIDATER EN LICENCE 1 (L.AS INCLUSE) (pages=n/a-n/a, score=0.8603, semantic=0.8363, dans_contexte=non)  https://www.inalco.fr/candidatures

**Faits de référence (non transmis au modèle) :**

- L'accès en première année de licence à l'Inalco passe par Parcoursup
- Cette procédure concerne également une nouvelle candidature en première année dans le cadre d'une réorientation annuelle

## q009. Quelle procédure de candidature dois-je suivre selon ma nationalité et mon pays de résidence ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `4986 caractères`

**Reponse :**

Réponse :
La procédure de candidature à l'Inalco dépend de votre nationalité et de votre pays de résidence. Voici les informations pertinentes :

1. **Candidats extra-européens résidant ou étudiant actuellement dans un pays hors UE ou EEE relevant de la procédure Études en France** :
   - Vous devez candidater directement en ligne sur la plateforme Études en France.
   - Pour plus d'informations, consultez la page suivante.

2. **Candidats résidant à l'étranger dans un pays ne relevant pas de la procédure Études en France** :
   - Vous devez suivre la procédure de Demande d'Admission Préalable (DAP) dossier blanc.
   - Pour connaître les modalités de la DAP Blanche, veuillez prendre contact avec l'Espace Campus France de l'Ambassade de France du pays dans lequel vous résidez.
   - L'Inalco ne traite directement aucune DAP de candidat résidant en dehors de la France.

3. **Candidats européens et candidats extra-européens étudiant actuellement dans une université française ou européenne, ou résident dans un pays ne relevant pas de la procédure Études en France** :
   - Vous devez suivre la même procédure que les ressortissants français ; veuillez vous référer à la page suivante via la plateforme MonMaster.

Sources :
- [Candidater à un cursus diplômant](https://www.inalco.fr/candidater-un-cursus-diplomant)
- [Candidatures](https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/candidatures.html)

**Sources recuperees :**

- [1] Candidater à un cursus diplômant / 2. Candidater (pages=n/a-n/a, score=0.887, semantic=0.863, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [2] Candidater à un cursus diplômant / 2. Candidater (pages=n/a-n/a, score=0.8817, semantic=0.8577, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [3] Candidatures / Candidatures (pages=n/a-n/a, score=0.8778, semantic=0.8598, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/candidatures.html
- [4] Candidater à un cursus diplômant / Candidats européens et candidats extra-européens étudiant actuellement dans une université française ou européenne, ou résident dans un pays ne relevant pas de la procédure Études en France (pages=n/a-n/a, score=0.8757, semantic=0.8577, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [5] Candidater à un cursus diplômant / 2. Candidater (pages=n/a-n/a, score=0.8755, semantic=0.8515, dans_contexte=non)  https://www.inalco.fr/candidater-un-cursus-diplomant

**Faits de référence (non transmis au modèle) :**

- La procédure de candidature dépend de la nationalité, du pays de résidence et du diplôme de fin d'études secondaires
- Les candidats relevant de la procédure Études en France doivent candidater sur cette plateforme
- Les candidats résidant à l'étranger dans un pays ne relevant pas d'Études en France peuvent relever de la Demande d'Admission Préalable

## q010. Puis-je candidater avec un diplôme de fin d'études secondaires obtenu à l'étranger ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `4533 caractères`

**Reponse :**

Réponse :
Oui, vous pouvez candidater avec un diplôme de fin d'études secondaires obtenu à l'étranger. Cependant, vous devez suivre la procédure de Demande d'Admission Préalable (DAP) dossier blanc si vous résidez à l'étranger dans un pays ne relevant pas de la procédure Études en France. Pour connaître les modalités de la DAP Blanche, veuillez prendre contact avec l'Espace Campus France de l'Ambassade de France du pays dans lequel vous résidez. L'Inalco ne traite directement aucune DAP de candidat résidant en dehors de la France.

Sources :
- [Source 1]
- [Source 2]
- [Source 3]
- [Source 4]

**Sources recuperees :**

- [1] Candidater à un cursus diplômant / Candidats extra-européens en possession d'un baccalauréat international ou d'un diplôme de fin d'études secondaires délivré par un pays hors UE et EEE (pages=n/a-n/a, score=0.873, semantic=0.855, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [2] Candidater à un cursus diplômant / 2. Candidater (pages=n/a-n/a, score=0.871, semantic=0.853, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [3] FAQ Admission en Master / EST-IL POSSIBLE DE CANDIDATER EN ETANT DIPLOME D’UNE AUTRE UNIVERSITE QUE L’INALCO ? (pages=n/a-n/a, score=0.8703, semantic=0.8523, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [4] Candidater à un cursus diplômant / 2. Candidater (pages=n/a-n/a, score=0.87, semantic=0.852, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [5] FAQ Admission en Master / Une question sur l'admission en Master à l'Inalco? (pages=n/a-n/a, score=0.8696, semantic=0.8516, dans_contexte=non)  https://www.inalco.fr/faq-admission-en-master

**Faits de référence (non transmis au modèle) :**

- Un candidat titulaire d'un diplôme de fin d'études secondaires obtenu à l'étranger peut candidater
- La procédure à suivre dépend notamment du pays de résidence et de l'application ou non de la procédure Études en France
- Les candidats résidant à l'étranger hors procédure Études en France doivent suivre la procédure DAP dossier blanc lorsque celle-ci s'applique

## q012. Quels masters de l'Inalco sont accessibles sur la plateforme Mon Master ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4186 caractères`

**Reponse :**

Les masters de l'Inalco accessibles sur la plateforme Mon Master sont les suivants :

1. Master en Langues et Civilisations Étrangères et Régionales (LCER)
2. Master en Langues et Civilisations Étrangères et Régionales (LCER) - Spécialité XXX
3. Master en Langues et Civilisations Étrangères et Régionales (LCER) - Spécialité YYY
4. Master en Langues et Civilisations Étrangères et Régionales (LCER) - Spécialité ZZZ
5. Master en Langues et Civilisations Étrangères et Régionales (LCER) - Spécialité WWW
6. Master en Langues et Civilisations Étrangères et Régionales (LCER) - Spécialité VVV
7. Master en Langues et Civilisations Étrangères et Régionales (LCER) - Spécialité UUU
8. Master en Langues et Civilisations Étrangères et Régionales (LCER) - Spécialité TTT
9. Master en Langues et Civilisations Étrangères et Régionales (LCER) - Spécialité SSS

Pour plus de détails sur chaque spécialité, veuillez consulter la page officielle des formations de l'Inalco : [Formations de l'Inalco](https://www.inalco.fr/formations).

Sources :
- [FAQ Admission en Master](https://www.inalco.fr/faq-admission-en-master)

**Sources recuperees :**

- [1] FAQ Admission en Master / COMMENT CHOISIR MON MASTER A L’INALCO ? (pages=n/a-n/a, score=0.9171, semantic=0.8811, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [2] FAQ Admission en Master / À quelle date les résultats d’admission sont-ils disponibles ? (pages=n/a-n/a, score=0.9096, semantic=0.8736, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [3] FAQ Admission en Master / Une question sur la plateforme MonMaster? (pages=n/a-n/a, score=0.9095, semantic=0.8735, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [4] FAQ Admission en Master / Y a-t-il des examens/concours d’entrée pour certains Masters ? (pages=n/a-n/a, score=0.903, semantic=0.867, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [5] FAQ Admission en Master / Quelle est la période de candidature sur la plateforme MonMaster ? (pages=n/a-n/a, score=0.901, semantic=0.865, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master

**Faits de référence (non transmis au modèle) :**

- Pour la campagne 2026, Mon Master concerne notamment les M1 LLCER, Didactique des langues, Langues et sociétés, Management et commerce international, Relations internationales, Sciences du langage, Traitement automatique des langues, Traduction littéraire, Traduction spécialisée et Médiation et interprétation en service public

## q014. Puis-je candidater en master avec une licence obtenue dans une autre université ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `4702 caractères`

**Reponse :**

Oui, il est possible de candidater en master avec une licence obtenue dans une autre université. L'Inalco accepte les étudiants titulaires de diplôme de Licence attestant d’études d’une langue orientale et d’une formation disciplinaire en cohérence avec la formation disciplinaire demandée. Les diplômes obtenus à l’étranger doivent être traduits en français par un traducteur assermenté. Les candidats peuvent également être contactés pour passer un test de niveau dans la langue de spécialité choisie.

Sources :
- [FAQ Admission en Master](https://www.inalco.fr/faq-admission-en-master)

**Sources recuperees :**

- [1] FAQ Admission en Master / J’ai déjà un Master. Puis-je candidater pour un nouveau Master ? (pages=n/a-n/a, score=0.8972, semantic=0.8612, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [2] FAQ Admission en Master / EST-IL POSSIBLE DE CANDIDATER EN ETANT DIPLOME D’UNE AUTRE UNIVERSITE QUE L’INALCO ? (pages=n/a-n/a, score=0.8934, semantic=0.8574, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [3] FAQ Admission en Master / Puis-je candidater et suivre 2 Masters en parallèle ? (pages=n/a-n/a, score=0.8922, semantic=0.8562, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [4] FAQ Admission en Master / QUELLE EST LA DIFFERENCE ENTRE UN MASTER PRO, UN MASTER RECHERCHE ET LES AUTRES MENTIONS ? (pages=n/a-n/a, score=0.8864, semantic=0.8504, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [5] FAQ Admission en Master / Une question sur la plateforme MonMaster? (pages=n/a-n/a, score=0.8863, semantic=0.8503, dans_contexte=non)  https://www.inalco.fr/faq-admission-en-master

**Faits de référence (non transmis au modèle) :**

- Il est possible de candidater avec une licence obtenue dans une autre université
- La licence doit attester d'études d'une langue orientale et d'une formation disciplinaire cohérente avec le master demandé
- Un diplôme obtenu à l'étranger doit être traduit en français par un traducteur assermenté

## q015. Comment candidater directement en deuxième année de master ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5707 caractères`

**Reponse :**

Pour candidater directement en deuxième année de master à l'Inalco, il est important de vérifier les conditions spécifiques de chaque master. Certains masters offrent des places directement accessibles au niveau M2 pour des étudiants ayant validé une première année de master. Les conditions et modalités d’accès sont indiquées dans les brochures correspondantes.

Pour les masters suivants : LLCER, Didactique des langues, IMAS, Management et commerce international, Relations internationales, Sciences du langage, Traitement automatique des langues, Traduction littéraire et Traduction spécialisée, il est possible de candidater directement en deuxième année de master.

La campagne de candidature en M2 (destinée aux candidats extérieurs à l'Inalco) se déroule du 17 février au 16 mars 2026 sur la plateforme [eCandidat1](https://admissions.inalco.fr).

Il est recommandé de bien préparer son dossier de candidature et de ne pas attendre les derniers jours pour éviter un dossier bâclé et donc non valide.

Sources :
- [Candidatures](https://www.inalco.fr/candidatures)
- [FAQ Admission en Master](https://www.inalco.fr/faq-admission-en-master)
- [Candidater à un cursus diplômant](https://www.inalco.fr/candidater-un-cursus-diplomant)

**Sources recuperees :**

- [1] Candidatures / CANDIDATER EN MASTER 2 (pages=n/a-n/a, score=0.9135, semantic=0.8775, dans_contexte=oui)  https://www.inalco.fr/candidatures
- [2] FAQ Admission en Master / Une question sur la plateforme MonMaster? (pages=n/a-n/a, score=0.9092, semantic=0.8732, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [3] FAQ Admission en Master / Puis-je candidater directement en Master 2 ? (pages=n/a-n/a, score=0.9068, semantic=0.8708, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [4] Candidater à un cursus diplômant / Candidater en Master (pages=n/a-n/a, score=0.9065, semantic=0.8705, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [5] FAQ Admission en Master / QUELLE EST LA DIFFERENCE ENTRE UN MASTER PRO, UN MASTER RECHERCHE ET LES AUTRES MENTIONS ? (pages=n/a-n/a, score=0.8977, semantic=0.8617, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master

**Faits de référence (non transmis au modèle) :**

- Certains masters acceptent une admission directe en M2 pour des candidats ayant au minimum un niveau M1
- Pour les candidats extérieurs à l'Inalco, la campagne M2 2026 annoncée se déroule du 17 février au 16 mars
- La candidature directe en M2 s'effectue sur eCandidat pour les masters concernés

## q016. Quels tests de langue sont demandés pour le master Traduction et interprétation ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5629 caractères`

**Reponse :**

Pour le master Traduction et interprétation (TSI) à l'Inalco, les tests de langue demandés sont les suivants :

1. **Français** : Les candidats doivent démontrer leur compétence en français, y compris leur capacité à traduire, leur orthographe, la richesse et la précision de leur expression, et leur faculté d’analyse.
2. **Anglais** : Les candidats doivent également démontrer leur compétence en anglais, qui sert de base commune aux enseignements de traduction spécialisée.
3. **Langue orientale** : Les candidats doivent démontrer leur compétence en une langue orientale enseignée à l’Inalco, qui peut être leur langue maternelle ou de scolarisation.

Ces compétences sont évaluées lors des épreuves d’admission, qui visent à évaluer la capacité des candidats à traduire et à analyser des textes dans ces langues.

Sources :
- [Master TI - Traduction spécialisée](https://www.inalco.fr/formations/master-ti-traduction-specialisee)

**Sources recuperees :**

- [1] Master TI - Traduction spécialisée / FAQ (pages=n/a-n/a, score=0.8865, semantic=0.8685, dans_contexte=oui)  https://www.inalco.fr/formations/master-ti-traduction-specialisee
- [2] Master TI - Traduction spécialisée / Master TI - Traduction spécialisée (pages=n/a-n/a, score=0.8838, semantic=0.8658, dans_contexte=oui)  https://www.inalco.fr/formations/master-ti-traduction-specialisee
- [3] Master TI - Traduction spécialisée / Master TI - Traduction spécialisée (pages=n/a-n/a, score=0.8825, semantic=0.8645, dans_contexte=oui)  https://www.inalco.fr/formations/master-ti-traduction-specialisee
- [4] Master TI - Traduction spécialisée / Master TI - Traduction spécialisée (pages=n/a-n/a, score=0.8825, semantic=0.8645, dans_contexte=oui)  https://www.inalco.fr/formations/master-ti-traduction-specialisee
- [5] Master TI - Traduction spécialisée / Attendus (pages=n/a-n/a, score=0.8808, semantic=0.8628, dans_contexte=non)  https://www.inalco.fr/formations/master-ti-traduction-specialisee

**Faits de référence (non transmis au modèle) :**

- Les épreuves d'admission évaluent les compétences en français, en anglais et en langue orientale
- Les candidats sont évalués sur la traduction, l'orthographe, la précision de l'expression et la capacité d'analyse
- Le niveau correspondant généralement à une L3 est le niveau B2 du CECRL
- Un TOEFL peut être exigé par certaines universités partenaires pour le semestre intégré

## q017. Quels sont les prérequis pour candidater au master Traitement automatique des langues ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
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
- [Source 2]

**Sources recuperees :**

- [1] Master Traitement automatique des langues (TAL) / Candidatures (pages=n/a-n/a, score=0.9332, semantic=0.8972, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [2] Master Traitement automatique des langues (TAL) / Public visé (pages=n/a-n/a, score=0.9033, semantic=0.8853, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [3] Master Traitement automatique des langues (TAL) / Master Traitement automatique des langues (TAL) (pages=n/a-n/a, score=0.9021, semantic=0.8841, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [4] Master Traitement automatique des langues (TAL) / Spécialités du master TAL (pages=n/a-n/a, score=0.9013, semantic=0.8833, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [5] Master Traitement automatique des langues (TAL) / Master Traitement automatique des langues (TAL) (pages=n/a-n/a, score=0.8975, semantic=0.8795, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal

**Faits de référence (non transmis au modèle) :**

- Un candidat au Master TAL peut être titulaire de la licence LLCER parcours Traitement automatique des langues de l'Inalco
- À défaut, il doit justifier d'un niveau suffisant dans une langue enseignée à l'Inalco et de compétences en linguistique ou en informatique

## q020. Est-il encore possible de candidater après la fermeture de la campagne principale ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `clarify`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4780 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Se présenter aux élections / Étape 1 : retirer les formulaires de candidature (pages=n/a-n/a, score=0.8439, semantic=0.8259, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/s-engager/se-presenter-aux-elections.html
- [2] Se présenter aux élections / Étape 1 : retirer les formulaires de candidature (pages=n/a-n/a, score=0.8416, semantic=0.8236, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/s-engager/se-presenter-aux-elections.html
- [3] Elections aux conseils centraux CA et CS / Formulaire de candidature (pages=n/a-n/a, score=0.8388, semantic=0.8208, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/s-engager/se-presenter-aux-elections/elections-aux-conseils-centraux-ca-et-cs.html
- [4] FAQ Admission en Master / Je suis un adulte en reprise d’études, puis-je candidater pour un Master ? (pages=n/a-n/a, score=0.8388, semantic=0.8208, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [5] FAQ Admission en Master / Une question sur la plateforme MonMaster? (pages=n/a-n/a, score=0.8387, semantic=0.8207, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master

## q021. Quand et comment les résultats d'admission sont-ils communiqués ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4262 caractères`

**Reponse :**

Les résultats d'admission pour les Masters à l'Inalco sont disponibles à partir du **3 juin 2026** sur la plateforme Mon Master.

**Sources recuperees :**

- [1] FAQ Admission en Master / À quelle date les résultats d’admission sont-ils disponibles ? (pages=n/a-n/a, score=0.8765, semantic=0.8405, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [2] FAQ Admission en Master / Y a-t-il des examens/concours d’entrée pour certains Masters ? (pages=n/a-n/a, score=0.8537, semantic=0.8177, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [3] Elections aux conseils centraux CA et CS / Formulaire de candidature (pages=n/a-n/a, score=0.8512, semantic=0.8272, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/s-engager/se-presenter-aux-elections/elections-aux-conseils-centraux-ca-et-cs.html
- [4] Elections aux conseils centraux CA et CS / Formulaire de candidature (pages=n/a-n/a, score=0.8495, semantic=0.8255, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/s-engager/se-presenter-aux-elections/elections-aux-conseils-centraux-ca-et-cs.html
- [5] FAQ Admission en Master / Une question sur la plateforme MonMaster? (pages=n/a-n/a, score=0.8491, semantic=0.8251, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master

**Faits de référence (non transmis au modèle) :**

- Pour la campagne 2026 mentionnée dans la FAQ, les résultats d'admission en master sont disponibles sur Mon Master à partir du 3 juin 2026

## q022. Que dois-je faire après avoir reçu une autorisation d'admission ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5516 caractères`

**Reponse :**

Réponse :
Après avoir reçu une autorisation d'admission, vous devez suivre les étapes suivantes :

1. **Confirmer votre admission** : Si vous avez candidaté via la plateforme Études en France, vous devez confirmer votre acceptation de la proposition d'admission avant la date limite indiquée dans le message. Si vous avez candidaté par une autre procédure, vous devez confirmer votre acceptation de la proposition d'admission avant la date limite indiquée dans le mail.

2. **Demander votre visa** : Une fois votre confirmation d'admission effectuée, vous pouvez déposer votre demande de visa auprès du consulat. La procédure est simplifiée si vous avez candidaté via Études en France.

3. **Inscription administrative** : Après avoir obtenu votre visa, vous recevrez un message via la plateforme Études en France contenant le lien vers le site où vous pourrez réaliser votre inscription administrative. Vous devrez vous acquitter des frais d'inscription avant de pouvoir finaliser cette étape.

4. **Inscription pédagogique** : Une fois votre inscription administrative terminée, vous pourrez procéder à votre inscription pédagogique. Pour cela, consultez la page suivante : [Inscriptions Pédagogiques](https://www.inalco.fr/candidater-un-cursus-diplomant).

Sources :
- [Candidater à un cursus diplômant](https://www.inalco.fr/candidater-un-cursus-diplomant)
- [FAQ Admission en Master](https://www.inalco.fr/faq-admission-en-master)

**Sources recuperees :**

- [1] Candidater à un cursus diplômant / 3. Après l'admission, demander son visa et s'inscrire administrativement à l'Inalco (pages=n/a-n/a, score=0.8479, semantic=0.8299, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [2] Candidater à un cursus diplômant / 3. Après l'admission, demander son visa et s'inscrire administrativement à l'Inalco (pages=n/a-n/a, score=0.8469, semantic=0.8289, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [3] Candidater à un cursus diplômant / 3. Après l'admission, demander son visa et s'inscrire administrativement à l'Inalco (pages=n/a-n/a, score=0.8445, semantic=0.8265, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [4] Candidater à un cursus diplômant / 3. Après l'admission, demander son visa et s'inscrire administrativement à l'Inalco (pages=n/a-n/a, score=0.8434, semantic=0.8254, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [5] FAQ Admission en Master / Une fois que j'aurai une autorisation d'admission, quelle sera la suite ? (pages=n/a-n/a, score=0.8433, semantic=0.8253, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master

**Faits de référence (non transmis au modèle) :**

- Après une proposition d'admission, le candidat doit confirmer son acceptation dans le délai indiqué par la plateforme utilisée
- Un candidat relevant d'Études en France doit obtenir son visa avant l'inscription administrative
- L'inscription administrative doit être réalisée après l'admission
- L'inscription pédagogique intervient après l'inscription administrative

## q023. Quelle est la différence entre candidature, admission, inscription administrative et inscription pédagogique ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4178 caractères`

**Reponse :**

Réponse :

La différence entre candidature, admission, inscription administrative et inscription pédagogique à l'Inalco est la suivante :

1. **Candidature** : C'est le processus par lequel un étudiant exprime son intérêt pour une formation à l'Inalco. Cela inclut le dépôt d'un dossier de candidature et la soumission des documents nécessaires.

2. **Admission** : Une fois que la candidature est examinée, l'étudiant est admis ou non à la formation. L'admission est la décision officielle de l'Inalco d'accepter l'étudiant dans le programme choisi.

3. **Inscription administrative** : Après avoir été admis, l'étudiant doit procéder à son inscription administrative. Cette étape est annuelle et obligatoire pour obtenir le statut d'étudiant. Elle inclut le paiement des droits de scolarité et la validation des informations administratives.

4. **Inscription pédagogique** : Une fois l'inscription administrative effectuée, l'étudiant doit procéder à son inscription pédagogique. Cette étape concerne la sélection des cours et des options pédagogiques pour l'année universitaire.

Sources :
- [Foire aux questions (FAQ) - Procédure d'inscription](https://www.inalco.fr/foire-aux-questions-faq-procedure-dinscription)
- [Inscription et réinscription administrative](https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-administrative.html)
- [Candidatures et réinscriptions](https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions.html)
- [Inscription et réinscription pédagogique](https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-pedagogique.html)

**Sources recuperees :**

- [1] Foire aux questions (FAQ) - Procédure d'inscription / Envoi du dossier d'inscription administrative (pages=n/a-n/a, score=0.8798, semantic=0.8618, dans_contexte=oui)  https://www.inalco.fr/foire-aux-questions-faq-procedure-dinscription
- [2] Inscription et réinscription administrative / Inscription et réinscription administrative (pages=n/a-n/a, score=0.8767, semantic=0.8587, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-administrative.html
- [3] Candidatures et réinscriptions / Candidatures et réinscriptions (pages=n/a-n/a, score=0.874, semantic=0.856, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions.html
- [4] Inscription et réinscription pédagogique / **Pour connaître les dates et modalités d'inscription et réinscription pédagogique, consultez la page ci-dessous** (pages=n/a-n/a, score=0.8712, semantic=0.8532, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-pedagogique.html
- [5] Inscription et réinscription pédagogique / Pour connaître les dates et modalités d'inscription et réinscription pédagogique, consultez la page ci-dessous (pages=n/a-n/a, score=0.8709, semantic=0.8529, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-pedagogique.html

**Faits de référence (non transmis au modèle) :**

- La candidature consiste à déposer une demande d'accès à une formation
- L'admission correspond à la décision favorable rendue sur cette candidature
- L'inscription administrative confère le statut d'étudiant après vérification du dossier et paiement des droits
- L'inscription pédagogique correspond notamment au choix et à l'enregistrement des enseignements suivis

## q027. Dans quelles situations peut-on demander une exonération des droits d'inscription ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `3`  
**Taille du contexte :** `4546 caractères`

**Reponse :**

Les situations dans lesquelles une exonération des droits d'inscription peut être demandée à l'Inalco sont les suivantes :

1. **Étudiants ayant le statut de réfugié ou bénéficiant de la protection subsidiaire.**
2. **Étudiants bénéficiant de la protection temporaire, apatrides ou demandeurs d’asile.**
3. **Travailleurs privés d’emploi en France et non indemnisés par France Travail.**
4. **Bénéficiaires du Régime de Solidarité Active (RSA).**

Ces exonérations doivent être demandées par les étudiants communautaires et extracommunautaires, accompagnées des pièces justificatives nécessaires. Les demandes d'exonération totale des droits d'inscription sont possibles pour un seul diplôme, national (L, M, D) ou d’établissement, ainsi que pour le FLE (dans le cas d’une inscription en FLE complémentaire à une inscription dans une formation diplômante de l’Inalco).

Les exonérations, si acceptées par le Président, s’effectuent uniquement par remboursement des droits d’inscription payés. Le délai de remboursement est de 4 à 6 mois à compter de la décision d’exonération.

Pour plus de détails, vous pouvez consulter la page officielle sur les droits de scolarité : [Droits de scolarité : tarifs, exonération, annulation, remboursement](https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement).

Sources :
- [Droits de scolarité : tarifs, exonération, annulation, remboursement](https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement)

**Sources recuperees :**

- [1] Droits de scolarité : tarifs, exonération, annulation, remboursement / Autres exonérations pouvant être accordées par le Président (pages=n/a-n/a, score=0.8593, semantic=0.8593, dans_contexte=oui)  https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement
- [2] Droits de scolarité : tarifs, exonération, annulation, remboursement / Modalités d’exonération sur demande des droits d’inscription applicables aux usagers de l’Inalco, communautaires ou extra-communautaires, pour l’année universitaire 2026/2027 (pages=n/a-n/a, score=0.856, semantic=0.856, dans_contexte=oui)  https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement
- [3] Droits de scolarité : tarifs, exonération, annulation, remboursement / Modalités d’exonération sur demande des droits d’inscription applicables aux usagers de l’Inalco, communautaires ou extra-communautaires, pour l’année universitaire 2026/2027 (pages=n/a-n/a, score=0.8506, semantic=0.8506, dans_contexte=oui)  https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement
- [4] Droits de scolarité : tarifs, exonération, annulation, remboursement / Modalités d’exonération sur demande des droits d’inscription applicables aux usagers de l’Inalco, communautaires ou extra-communautaires, pour l’année universitaire 2026/2027 (pages=n/a-n/a, score=0.8489, semantic=0.8489, dans_contexte=non)  https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement
- [5] Droits de scolarité : tarifs, exonération, annulation, remboursement / Modalités d’exonération sur demande des droits d’inscription applicables aux usagers de l’Inalco, communautaires ou extra-communautaires, pour l’année universitaire 2026/2027 (pages=n/a-n/a, score=0.8474, semantic=0.8474, dans_contexte=non)  https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement

**Faits de référence (non transmis au modèle) :**

- Une exonération peut être demandée en raison de la situation personnelle de l'étudiant
- La demande doit être accompagnée de pièces justificatives
- Les réfugiés, bénéficiaires de protections, demandeurs d'asile, bénéficiaires du RSA et certains étudiants en situation de handicap figurent parmi les catégories pouvant demander une exonération
- L'exonération sur demande porte sur un seul diplôme dans les conditions indiquées
- Lorsqu'elle est accordée, l'exonération est effectuée par remboursement des droits déjà payés

## q028. Puis-je demander une bourse ou une aide financière avant mon inscription définitive ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `4781 caractères`

**Reponse :**

Réponse :
Oui, vous pouvez demander une bourse ou une aide financière avant votre inscription définitive. Pour cela, vous devez constituer votre **Dossier Social Étudiant (DSE)**. Vous pouvez le faire en ligne sur [messervices.etudiant.gouv.fr](http://messervices.etudiant.gouv.fr/). Il est recommandé de le faire le plus tôt possible, car les demandes sont traitées par ordre d'arrivée.

Sources :
- [Bourses et aides sociales](https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-aides-sociales.html)
- [Lancement de la campagne de bourse et de logement étudiant 2026-2027](https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html)

**Sources recuperees :**

- [1] Candidater à un cursus diplômant / Bourse (pages=n/a-n/a, score=0.8732, semantic=0.8552, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [2] Bourses et aides sociales / Bourses et aides sociales (pages=n/a-n/a, score=0.8689, semantic=0.8509, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-aides-sociales.html
- [3] Lancement de la campagne de bourse et de logement étudiant 2026-2027 / Quelle que soit votre situation, ne ratez pas une aide à laquelle vous auriez droit ! (pages=n/a-n/a, score=0.8679, semantic=0.8499, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html
- [4] Bourses et aides sociales / Bourses sur critères sociaux du CROUS (pages=n/a-n/a, score=0.866, semantic=0.848, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-aides-sociales.html
- [5] Foire aux questions (FAQ) - Procédure d'inscription / Foire aux questions (FAQ) - Procédure d'inscription (pages=n/a-n/a, score=0.8649, semantic=0.8649, dans_contexte=non)  https://www.inalco.fr/foire-aux-questions-faq-procedure-dinscription

**Faits de référence (non transmis au modèle) :**

- Le Dossier social étudiant permet de demander une bourse et un logement en résidence universitaire
- Le DSE doit être renouvelé chaque année sur messervices.etudiant.gouv.fr
- La demande peut être déposée avant de disposer de tous les éléments définitifs et être modifiée ensuite

## q029. Quelles solutions de logement sont proposées aux futurs étudiants de l'Inalco ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5273 caractères`

**Reponse :**

L'Inalco ne propose pas de service de logement pour les étudiants. Cependant, des informations et des documents sont disponibles pour vous aider dans votre recherche de logement. Vous pouvez consulter les pages suivantes pour obtenir des conseils sur la recherche de logements, les procédures d’emménagement et les aides locatives :
- [Se loger](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html)
- [Accueil et intégration](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration.html)

Les étudiants boursiers bénéficient de plusieurs avantages, dont la priorité dans l’attribution des logements. Pour plus d'informations sur les aides aux logements, vous pouvez consulter la page dédiée :
- [Lancement de la campagne de bourse et de logement étudiant 2026-2027](https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html)

Sources :
- [Se loger](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html)
- [Accueil et intégration](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration.html)
- [Lancement de la campagne de bourse et de logement étudiant 2026-2027](https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html)

**Sources recuperees :**

- [1] Se loger / Se loger (pages=n/a-n/a, score=0.8898, semantic=0.8718, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html
- [2] Accueil et intégration / Bienvenue à l'Inalco ! (pages=n/a-n/a, score=0.8797, semantic=0.8617, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration.html
- [3] Se loger / Informations et documentations sur les logements (pages=n/a-n/a, score=0.876, semantic=0.858, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html
- [4] Lancement de la campagne de bourse et de logement étudiant 2026-2027 / Quels sont les avantages d'être boursier ou boursière ? (pages=n/a-n/a, score=0.8748, semantic=0.8568, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html
- [5] Schéma Directeur de la Vie Étudiante 2023-2028 / Page 9 (pages=9-9, score=0.8743, semantic=0.8563, dans_contexte=oui)  https://www.inalco.fr/sites/default/files/2024-05/Sh%C3%A9ma%20Directeur%20de%20la%20Vie%20%C3%89tudiante-avec%20compression.pdf

**Faits de référence (non transmis au modèle) :**

- L'Inalco ne dispose pas de service de logement pour les étudiants
- Le portail fournit des informations sur la recherche de logement, l'emménagement et les aides locatives
- Il renvoie notamment vers le Crous de Paris, Campus France et un guide des aides au logement

## q030. Existe-t-il des restaurants universitaires à proximité de l'Inalco ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4341 caractères`

**Reponse :**

Réponse :
Oui, il existe des restaurants universitaires à proximité de l'Inalco. Voici les informations disponibles :

1. **Restaurant Universitaire de la Halle aux farines** :
   - Adresse : 3 esplanade Pierre Vidal Naquet 75013 Paris
   - Ouverture : du lundi au vendredi de 11h15 à 14h15
   - Guichet Izly : disponible de 11h15 à 14h15

2. **Cafétéria de l'Inalco** :
   - Adresse : 1er étage du Pôle des Langues et Civilisations
   - Ouverture : du lundi au vendredi de 8h00 à 20h00, le samedi de 9h00 à 17h00
   - Vente à emporter
   - Accessible aux étudiants et personnels de l'INALCO
   - Accès wifi

3. **Restaurant Universitaire La Barge du Crous de Paris** :
   - Adresse : Port de la Gare Quai François Mauriac 75013 Paris
   - Horaires : du lundi au samedi de 11h30 à 14h

Pour plus d'informations, vous pouvez consulter les pages suivantes :
- [Restaurant Universitaire de la Halle aux farines](https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html#restaurant-universitaire-de-la-halle-aux-farines)
- [Cafétéria de l'Inalco](https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html#cafeteria-de-linalco)
- [Restaurant Universitaire La Barge du Crous de Paris](https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html#restaurant-universitaire-la-barge-du-crous-de-paris)

Sources :
- [Se nourrir](https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nour

**Sources recuperees :**

- [1] Se nourrir / Restaurants et cafétérias universitaires (pages=n/a-n/a, score=0.8902, semantic=0.8722, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html
- [2] Se nourrir / Comment payer ? (pages=n/a-n/a, score=0.8675, semantic=0.8495, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html
- [3] Se nourrir / Restaurant Universitaire de la Halle aux farines (pages=n/a-n/a, score=0.8672, semantic=0.8492, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html
- [4] Se nourrir / Cafétéria de l'Inalco (pages=n/a-n/a, score=0.8663, semantic=0.8483, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html
- [5] Se nourrir / Restaurant Universitaire La Barge du Crous de Paris (pages=n/a-n/a, score=0.8651, semantic=0.8471, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html

**Faits de référence (non transmis au modèle) :**

- La cafétéria de l'Inalco et plusieurs restaurants universitaires se trouvent à proximité
- Le Restaurant Universitaire de la Halle aux farines est situé au 3 esplanade Pierre Vidal-Naquet, 75013 Paris
- La Halle aux farines est ouverte du lundi au vendredi de 11h15 à 14h15 selon la page collectée

## q032. Comment se rendre au Pôle des langues et civilisations et à la Maison de la recherche ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `3399 caractères`

**Reponse :**

Pour se rendre au Pôle des langues et civilisations et à la Maison de la recherche, voici les informations disponibles :

### Pôle des langues et civilisations
- **Adresse :**
  - 65 rue des grands moulins
  - 75013 Paris
- **Accueil :**
  - +33 (0)1 81 70 10 00 (du lundi au vendredi)

### Maison de la recherche
- **En métro :**
  - M1 - station Palais-Royal - Musée du Louvre
  - M4 - station Saint-Germain-des-Prés
  - M7 - station Palais-Royal - Musée du Louvre
  - M12 - station rue du Bac
- **En bus :**
  - Lignes 27, 39, 68, 69, 87, 95 - arrêt Pont du Carrousel - Quai Voltaire
- **En RER :**
  - RER C - station Musée d’Orsay

### Horaires d'ouverture du Pôle des langues et civilisations
- **Horaires :**
  - de 7h45 à 22h du lundi au samedi (le comptoir d'accueil est fermé le samedi et à partir de 18h en semaine)

Sources :
- [Le Pôle des langues et civilisations](https://www.inalco.fr/le-pole-des-langues-et-civilisations)
- [La Maison de la recherche](https://www.inalco.fr/la-maison-de-la-recherche)
- [Se rendre à l'Inalco](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-rendre-a-l-inalco.html)

**Sources recuperees :**

- [1] Le Pôle des langues et civilisations / Adresse (pages=n/a-n/a, score=0.9244, semantic=0.8624, dans_contexte=oui)  https://www.inalco.fr/le-pole-des-langues-et-civilisations
- [2] La Maison de la recherche / Accès (pages=n/a-n/a, score=0.9125, semantic=0.8495, dans_contexte=oui)  https://www.inalco.fr/la-maison-de-la-recherche
- [3] Le Pôle des langues et civilisations / Le Pôle des langues et civilisations (pages=n/a-n/a, score=0.9114, semantic=0.8494, dans_contexte=oui)  https://www.inalco.fr/le-pole-des-langues-et-civilisations
- [4] Se rendre à l'Inalco / Le Pôle des langues et des civilisations (PLC) (pages=n/a-n/a, score=0.9093, semantic=0.8463, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-rendre-a-l-inalco.html
- [5] Le Pôle des langues et civilisations / Horaires d'ouverture (pages=n/a-n/a, score=0.9086, semantic=0.8466, dans_contexte=oui)  https://www.inalco.fr/le-pole-des-langues-et-civilisations

**Faits de référence (non transmis au modèle) :**

- Le Pôle des langues et civilisations est situé au 65 rue des Grands Moulins, 75013 Paris
- Le PLC est accessible par le RER C à Bibliothèque François Mitterrand
- Les bus 83, 89, 27, 62, 64, 132 et N31 desservent des arrêts indiqués à proximité du PLC
- La Maison de la recherche est située au 2 rue de Lille, 75007 Paris
- La Maison de la recherche est accessible notamment par les métros 1, 4, 7 et 12, par le RER C à Musée d'Orsay et par les bus 27, 39, 68, 69, 87 et 95

## q033. Existe-t-il des journées portes ouvertes pour découvrir l'Inalco ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5712 caractères`

**Reponse :**

Réponse :
Oui, il existe des journées portes ouvertes pour découvrir l'Inalco. Vous pouvez consulter les informations sur les réunions de rentrée organisées du 14 au 18 septembre 2026 sur la page suivante : [Lien vers la page des réunions de rentrée](https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juillet-2026/faire-sa-rentree.html).

Sources :
- [Faire sa rentrée à l'Inalco](https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juillet-2026/faire-sa-rentree.html)

**Sources recuperees :**

- [1] Faire sa rentrée à l'Inalco / Bienvenue à l'Inalco ! (pages=n/a-n/a, score=0.8586, semantic=0.8586, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juillet-2026/faire-sa-rentree.html
- [2] Dejima - Association des étudiants du département Études japonaises / En savoir plus sur nous (pages=n/a-n/a, score=0.8558, semantic=0.8558, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/les-associations-etudiantes/dejima.html
- [3] Construire son projet d'études / DES EVENEMENTS DEDIES A L'ORIENTATION (pages=n/a-n/a, score=0.8544, semantic=0.8544, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/information-et-orientation/construire-son-projet-d-etudes.html
- [4] Journées européennes du patrimoine 2026 : appel à bénévoles / Journées européennes du patrimoine 2026 : appel à bénévoles (pages=n/a-n/a, score=0.8521, semantic=0.8521, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juillet-2026/journees-europeennes-du-patrimoine-2026-appel-a-benevoles-2.html
- [5] Faire sa rentrée / Bienvenue à l'Inalco ! (pages=n/a-n/a, score=0.8521, semantic=0.8521, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/faire-sa-rentree.html

**Faits de référence (non transmis au modèle) :**

- L'Inalco organise des événements consacrés à l'orientation tout au long de l'année universitaire
- Ces événements comprennent notamment une journée portes ouvertes, des forums lycéens, des salons étudiants et une journée d'information et d'orientation

## q034. Où puis-je consulter les brochures détaillées des licences et des masters ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `2837 caractères`

**Reponse :**

Pour consulter les brochures détaillées des licences et des masters à l'Inalco, vous pouvez visiter la page suivante : [Masters LLCER - Brochures](https://www.inalco.fr/masters-llcer-brochures).

Sources :
- [Masters LLCER - Brochures](https://www.inalco.fr/masters-llcer-brochures)

**Sources recuperees :**

- [1] Masters LLCER - Brochures / Brochures générales (pages=n/a-n/a, score=0.8616, semantic=0.8616, dans_contexte=oui)  https://www.inalco.fr/masters-llcer-brochures
- [2] Masters LLCER - Brochures / Études chinoises (pages=n/a-n/a, score=0.8512, semantic=0.8512, dans_contexte=oui)  https://www.inalco.fr/masters-llcer-brochures
- [3] Masters LLCER - Brochures / Études japonaises (pages=n/a-n/a, score=0.8495, semantic=0.8495, dans_contexte=oui)  https://www.inalco.fr/masters-llcer-brochures
- [4] Masters LLCER - Brochures / Études hébraïques et juives (pages=n/a-n/a, score=0.8478, semantic=0.8478, dans_contexte=oui)  https://www.inalco.fr/masters-llcer-brochures
- [5] Masters LLCER - Brochures / Études arabes (pages=n/a-n/a, score=0.8475, semantic=0.8475, dans_contexte=oui)  https://www.inalco.fr/masters-llcer-brochures

**Faits de référence (non transmis au modèle) :**

- Les brochures des licences LLCER sont publiées sur la page Licences LLCER - Brochures
- Les brochures des masters LLCER sont publiées sur une page distincte consacrée aux masters
- Les brochures sont organisées par langue ou aire d'études

## q035. Où trouver le catalogue des enseignements et la description des cours ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5537 caractères`

**Reponse :**

Pour trouver le catalogue des enseignements et la description des cours à l'Inalco, vous pouvez consulter les pages suivantes :

1. **Planning des cours** : Utilisez le planning des cours disponible sur le portail étudiant. Vous pouvez y accéder via le lien suivant : [Planning des cours](https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html).

2. **Catalogue de cours et de formations EUniWell** : Pour explorer les offres de cours et de formations, consultez le catalogue EUniWell. Vous pouvez y accéder via le lien suivant : [Catalogue EUniWell](https://portail-etudiant.inalco.fr/fr/recherche-2/flux-rss.html).

Ces ressources vous permettront de visualiser les cours disponibles, de consulter les descriptions et de planifier votre emploi du temps.

Sources :
- [Planning des cours](https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html)
- [Catalogue EUniWell](https://portail-etudiant.inalco.fr/fr/recherche-2/flux-rss.html)

**Sources recuperees :**

- [1] Dates et calendriers / Comment utiliser le planning des cours (pages=n/a-n/a, score=0.8437, semantic=0.8437, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html
- [2] Dates et calendriers / Comment utiliser le planning des cours (pages=n/a-n/a, score=0.843, semantic=0.843, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html
- [3] Emplois du temps / Comment utiliser le planning ? (pages=n/a-n/a, score=0.8372, semantic=0.8372, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html
- [4] Sans titre / Catalogue de cours et de formations EUniWell : la sélection de septembre 202611 sept. 2026 10:12 - RSS Actu Faites passer vos compétences académiques et professionnelles au niveau supérieur ! Le catalogue EUniWell de cours et de formations est destiné aux étudiants, personnels administratifs et chercheurs de l'Inalco. (pages=n/a-n/a, score=0.8368, semantic=0.8368, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/recherche-2/flux-rss.html
- [5] Emplois du temps / Comment utiliser le planning ? (pages=n/a-n/a, score=0.8322, semantic=0.8322, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html

## q036. Puis-je consulter les emplois du temps avant de finaliser mon inscription ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5043 caractères`

**Reponse :**

Oui, vous pouvez consulter les emplois du temps avant de finaliser votre inscription. Les emplois du temps sont disponibles sur le site officiel de l'Inalco. Vous pouvez y accéder en suivant ce lien : [Accéder au planning](https://planning.inalco.fr/). Les emplois du temps affichés sont susceptibles d'être modifiés jusqu'à la rentrée universitaire, donc il est recommandé de vérifier les informations à nouveau avant de finaliser votre inscription.

Sources :
- [Emplois du temps](https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html)
- [Dates et calendriers](https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html)

**Sources recuperees :**

- [1] Emplois du temps / Emplois du temps (pages=n/a-n/a, score=0.8495, semantic=0.8495, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html
- [2] Emplois du temps / Emplois du temps (pages=n/a-n/a, score=0.8493, semantic=0.8493, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html
- [3] Dates et calendriers / Emplois du temps (pages=n/a-n/a, score=0.8449, semantic=0.8449, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html
- [4] Dates et calendriers / Comment utiliser le planning des cours (pages=n/a-n/a, score=0.8434, semantic=0.8434, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html
- [5] Emplois du temps / Comment utiliser le planning ? (pages=n/a-n/a, score=0.842, semantic=0.842, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html

**Faits de référence (non transmis au modèle) :**

- Les emplois du temps sont consultables sur le planning public de l'Inalco
- Les emplois du temps affichés peuvent être modifiés jusqu'à la rentrée universitaire

## q038. Quelles formations professionnalisantes sont proposées par l'Inalco ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4719 caractères`

**Reponse :**

Réponse :
L'Inalco propose plusieurs formations professionnalisantes, notamment le Master Traitement automatique des langues (TAL). Ce master est axé sur l'ingénierie linguistique et l'intelligence artificielle, et il s'adresse à des étudiants ayant des compétences en informatique ou en langues, souhaitant travailler dans des domaines tels que la traduction, le traitement automatique du langage naturel (NLP), et d'autres métiers de l'ingénierie linguistique.

Sources :
- [Master Traitement automatique des langues (TAL)](https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal)
- [FAQ Admission en Master](https://www.inalco.fr/faq-admission-en-master)

**Sources recuperees :**

- [1] Master Traitement automatique des langues (TAL) / Débouchés professionnels (pages=n/a-n/a, score=0.8739, semantic=0.8559, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [2] Diplômes d'établissement / Diplômes d'établissement (pages=n/a-n/a, score=0.8717, semantic=0.8537, dans_contexte=oui)  https://www.inalco.fr/formations/diplomes-detablissement
- [3] FAQ Admission en Master / COMMENT CHOISIR MON MASTER A L’INALCO ? (pages=n/a-n/a, score=0.8657, semantic=0.8477, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [4] Master Traitement automatique des langues (TAL) / Public visé (pages=n/a-n/a, score=0.8653, semantic=0.8473, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [5] Formations diplômantes / Formations diplômantes (pages=n/a-n/a, score=0.8644, semantic=0.8464, dans_contexte=oui)  https://www.inalco.fr/formations-diplomantes

## q040. L'Inalco propose-t-il des parcours permettant d'étudier deux langues ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `4930 caractères`

**Reponse :**

L'Inalco propose des parcours permettant d'étudier deux langues, notamment à travers la Licence LLCER à parcours bilangue. Ce programme permet de développer une double compétence en trois ans, en étudiant deux langues et cultures différentes de manière parallèle. Pour plus d'informations, vous pouvez consulter la page officielle dédiée à cette formation : [Licence LLCER à parcours bilangue](https://www.inalco.fr/formations/licence-llcer-parcours-bilangue).

Sources :
- [Licence LLCER à parcours bilangue](https://www.inalco.fr/formations/licence-llcer-parcours-bilangue)

**Sources recuperees :**

- [1] Licence LLCER à parcours bilangue / Pourquoi étudier deux langues orientales ? (pages=n/a-n/a, score=0.8959, semantic=0.8779, dans_contexte=oui)  https://www.inalco.fr/formations/licence-llcer-parcours-bilangue
- [2] Master Traitement automatique des langues (TAL) / Master Traitement automatique des langues (TAL) (pages=n/a-n/a, score=0.886, semantic=0.868, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [3] Master Traitement automatique des langues (TAL) / Master Traitement automatique des langues (TAL) (pages=n/a-n/a, score=0.8828, semantic=0.8648, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [4] Licence LLCER à parcours bilangue / Licence LLCER à parcours bilangue (pages=n/a-n/a, score=0.8825, semantic=0.8645, dans_contexte=oui)  https://www.inalco.fr/formations/licence-llcer-parcours-bilangue
- [5] Master Traitement automatique des langues (TAL) / Master Traitement automatique des langues (TAL) (pages=n/a-n/a, score=0.8818, semantic=0.8638, dans_contexte=non)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal

**Faits de référence (non transmis au modèle) :**

- L'Inalco propose des licences LLCER bilangues permettant d'étudier deux langues
- Ces parcours permettent d'associer notamment des langues apparentées, voisines ou liées par des relations historiques, économiques ou géopolitiques

## q041. Quels parcours thématiques ou disciplinaires peut-on choisir en licence LLCER ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4824 caractères`

**Reponse :**

Réponse :
En licence LLCER à l'Inalco, vous pouvez choisir parmi 12 parcours thématiques et disciplinaires. Ces parcours permettent d'affiner votre formation en complément des enseignements de langue et civilisation choisis. Le choix d'un parcours se fait lors de l'inscription pédagogique.

Sources :
- [Licences LLCER à parcours thématiques et disciplinaires](https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires)

**Sources recuperees :**

- [1] Licences LLCER à parcours thématiques et disciplinaires / Licences LLCER à parcours thématiques et disciplinaires (pages=n/a-n/a, score=0.9325, semantic=0.9145, dans_contexte=oui)  https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires
- [2] Licences LLCER à parcours thématiques et disciplinaires / Licences LLCER à parcours thématiques et disciplinaires (pages=n/a-n/a, score=0.9286, semantic=0.9106, dans_contexte=oui)  https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires
- [3] Licences LLCER à parcours thématiques et disciplinaires / En complément des parcours : ouverture, anglais, engagement étudiant (pages=n/a-n/a, score=0.9268, semantic=0.9088, dans_contexte=oui)  https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires
- [4] Licences LLCER à parcours thématiques et disciplinaires / Documentation (pages=n/a-n/a, score=0.9219, semantic=0.9039, dans_contexte=oui)  https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires
- [5] Licences LLCER à parcours thématiques et disciplinaires / Organisation des parcours thématiques et disciplinaires (pages=n/a-n/a, score=0.9198, semantic=0.9018, dans_contexte=oui)  https://www.inalco.fr/formations/licences-llcer-parcours-thematiques-et-disciplinaires

**Faits de référence (non transmis au modèle) :**

- Après la L1, un étudiant peut poursuivre en L2-L3 dans l'un des douze parcours thématiques et disciplinaires
- Ce parcours complète les enseignements de langue et de civilisation
- Le choix du parcours est effectué lors de l'inscription pédagogique

## q044. Quels aménagements sont proposés aux candidats en situation de handicap ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4163 caractères`

**Reponse :**

Les aménagements proposés aux candidats en situation de handicap à l'Inalco incluent la mise en place de plans d'accompagnement (PAEH) qui mentionnent les aménagements spécifiques pour chaque situation. Ces aménagements sont valables pour une année universitaire et doivent être renouvelés chaque année lors d'un rendez-vous avec la Mission Handicap. Les journées de sensibilisation au handicap sont également organisées chaque année pour sensibiliser les étudiants à la réalité du handicap et valoriser les actions mises en place par les associations, la BULAC et la mission handicap de l'Inalco.

Sources :
- [Mission Handicap](https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html)
- [Journées de sensibilisation au Handicap](https://portail-etudiant.inalco.fr/fr/vie-de-campus/journees-vie-de-campus/journees-thematiques/handicap.html)

**Sources recuperees :**

- [1] Mission Handicap / Procédure de la mise en place du plan d'accompagnement (PAEH) (pages=n/a-n/a, score=0.842, semantic=0.842, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [2] Mission Handicap / Procédure de la mise en place du plan d'accompagnement (PAEH) (pages=n/a-n/a, score=0.8396, semantic=0.8396, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [3] Handicap / Journées de sensibilisation au Handicap (pages=n/a-n/a, score=0.8361, semantic=0.8361, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/journees-vie-de-campus/journees-thematiques/handicap.html
- [4] Aménagement du cursus / Aménagement du cursus (pages=n/a-n/a, score=0.8351, semantic=0.8351, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/amenagement-du-cursus.html
- [5] Mission Handicap / Attention (pages=n/a-n/a, score=0.8319, semantic=0.8319, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html

**Faits de référence (non transmis au modèle) :**

- La Mission Handicap met en place un plan d'accompagnement de l'étudiant en situation de handicap
- Le PAEH précise les aménagements prévus pour les cours et les examens
- Une demande d'aménagement d'examen nécessite un PAEH validé
- La demande d'aménagement doit être renouvelée chaque année universitaire

## q045. Existe-t-il une procédure particulière pour les candidats en exil ou réfugiés ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4772 caractères`

**Reponse :**

Réponse :
Oui, il existe une procédure particulière pour les candidats en exil ou réfugiés. Les candidats en exil primo-arrivants, qui sont réfugiés, apatrides ou bénéficiaires de la protection subsidiaire/temporaire, peuvent être éligibles au [DU Passerelle Inalco](http://www.inalco.fr/international/etudiants-internationaux/passerelle-inalco). Pour toute inscription dans un autre diplôme de l'Inalco, les candidatures sont ouvertes via un formulaire entre début mars et début avril chaque année. Pour toute question, contactez directement la Direction Europe et International à l'adresse mail suivante : .

Sources :
- [Candidater à un cursus diplômant](https://www.inalco.fr/candidater-un-cursus-diplomant)

**Sources recuperees :**

- [1] Candidater à un cursus diplômant / Candidats en exil primo-arrivants (pages=n/a-n/a, score=0.8455, semantic=0.8455, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [2] Candidater à un cursus diplômant / Situation familiale (pages=n/a-n/a, score=0.8403, semantic=0.8403, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [3] Candidater à un cursus diplômant / Bourse (pages=n/a-n/a, score=0.8321, semantic=0.8321, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [4] Candidater à un cursus diplômant / Candidats européens, candidats intéressés par un diplôme d'établissement ou candidats en exil (pages=n/a-n/a, score=0.8319, semantic=0.8319, dans_contexte=oui)  https://www.inalco.fr/candidater-un-cursus-diplomant
- [5] Candidatures / Pour candidater aux cours de préparation à l'agrégation d'arabe, voir la page ci-dessous (pages=n/a-n/a, score=0.8312, semantic=0.8312, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/candidatures.html

**Faits de référence (non transmis au modèle) :**

- Les candidats en exil primo-arrivants comprennent les réfugiés, apatrides et bénéficiaires de la protection subsidiaire ou temporaire
- Selon leur profil, ils peuvent être éligibles au DU Passerelle Inalco
- Pour candidater à un autre diplôme par la procédure indiquée, un niveau B1 minimum en français est demandé

## q047. Quelles sont les conditions d'admission pour le parcours XXX ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `clarify`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5480 caractères`

**Reponse :**

Pour les parcours LLCER en Master, les conditions d'admission incluent généralement les critères suivants :

1. **Dossier de candidature** : Les candidats doivent constituer un dossier de candidature complet et bien préparé. La constitution du dossier prend du temps, il est donc recommandé de ne pas attendre les derniers jours pour le préparer.

2. **Critères de sélection** : Les critères de sélection sont spécifiques à chaque Master et sont indiqués dans les brochures correspondantes. Outre l’examen du dossier, certains Masters organisent des entretiens de sélection où l’étudiant présente son projet au jury.

3. **Campagne de candidature** : La campagne de candidature pour les Masters de deuxième année, y compris les parcours LLCER, se déroule du 17 février au 16 mars 2026 sur la plateforme [eCandidat1](https://admissions.inalco.fr).

4. **Nombre de candidatures** : Lors de la phase de candidature, les étudiants peuvent déposer un maximum de 15 candidatures. Ils disposent également d’un maximum de 15 candidatures supplémentaires pour candidater dans des formations en alternance.

5. **Thématiques et disciplines** : Le Master LLCER propose une dizaine de choix de thématiques ou disciplines, accessibles à tous les étudiants de toutes les langues. Ces thématiques permettent d’apporter une ouverture sur divers domaines tels que l’anthropologie sociale, les arts du monde, la littérature, l’oralité, la linguistique, l’environnement, le genre et les sexualités dans le monde, l’histoire connectée du monde, la religion et les violences, les migrations et les mémoires.

Pour des informations plus détaillées et spécifiques, il est recommandé de consulter les brochures des parcours LLCER disponibles sur le site officiel de l'Inalco.

Sources :
- [FAQ Admission en Master](https://www.inalco.fr/faq-admission-en-master)
- [Candidatures](https://www.inalco.fr/candidatures)

**Sources recuperees :**

- [1] FAQ Admission en Master / Puis-je poursuivre mon parcours transversal thématique et disciplinaire LLCER en Master? (pages=n/a-n/a, score=0.8589, semantic=0.8229, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [2] FAQ Admission en Master / Une question sur l'admission en Master à l'Inalco? (pages=n/a-n/a, score=0.8553, semantic=0.8193, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [3] Candidatures / CANDIDATER EN MASTER 2 (pages=n/a-n/a, score=0.8535, semantic=0.8175, dans_contexte=oui)  https://www.inalco.fr/candidatures
- [4] FAQ Admission en Master / Une question sur la plateforme MonMaster? (pages=n/a-n/a, score=0.853, semantic=0.817, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [5] FAQ Admission en Master / Sur quels critères seront sélectionnés les étudiants ? (pages=n/a-n/a, score=0.8516, semantic=0.8156, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master

## q048. Puis-je candidater à plusieurs masters de l'Inalco en même temps ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5241 caractères`

**Reponse :**

Réponse :
En principe, les étudiants sont autorisés à candidater et à suivre plusieurs cursus. Cependant, il est attendu que les étudiants s’assurent, avant le début de l’année universitaire, qu’ils seront en mesure de concilier présence assidue aux cours et travail personnel. La charge de travail personnel demandée en Master est très importante, ce qui rend difficile le suivi de plusieurs cursus de Master en parallèle. De plus, la présence en cours peut être empêchée du fait de chevauchements horaires des divers emplois du temps. Il est recommandé d’en parler aux responsables de Master avant toute décision, certains Masters ayant des dispositions et une expérience spécifique en la matière.

Sources :
- [FAQ Admission en Master](https://www.inalco.fr/faq-admission-en-master)

**Sources recuperees :**

- [1] FAQ Admission en Master / Puis-je candidater et suivre 2 Masters en parallèle ? (pages=n/a-n/a, score=0.9093, semantic=0.8913, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [2] FAQ Admission en Master / A combien de Masters puis-je postuler ? (pages=n/a-n/a, score=0.8997, semantic=0.8817, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [3] FAQ Admission en Master / Une question sur la plateforme MonMaster? (pages=n/a-n/a, score=0.8972, semantic=0.8792, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [4] FAQ Admission en Master / J’ai déjà un Master. Puis-je candidater pour un nouveau Master ? (pages=n/a-n/a, score=0.8957, semantic=0.8777, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [5] FAQ Admission en Master / COMMENT CHOISIR MON MASTER A L’INALCO ? (pages=n/a-n/a, score=0.895, semantic=0.877, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master

**Faits de référence (non transmis au modèle) :**

- Il est possible de candidater à plusieurs masters
- Pour la phase de candidature Mon Master 2026 mentionnée, un candidat peut déposer au maximum quinze candidatures, auxquelles peuvent s'ajouter quinze candidatures en alternance
- Suivre plusieurs masters simultanément peut être difficile en raison de la charge de travail et des chevauchements d'emploi du temps

## q049. Puis-je candidater à un nouveau master si je possède déjà un diplôme de master ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
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

- [1] FAQ Admission en Master / J’ai déjà un Master. Puis-je candidater pour un nouveau Master ? (pages=n/a-n/a, score=0.931, semantic=0.895, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [2] FAQ Admission en Master / Une question sur la plateforme MonMaster? (pages=n/a-n/a, score=0.9004, semantic=0.8644, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [3] FAQ Admission en Master / Je suis un adulte en reprise d’études, puis-je candidater pour un Master ? (pages=n/a-n/a, score=0.9002, semantic=0.8642, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [4] FAQ Admission en Master / Puis-je candidater et suivre 2 Masters en parallèle ? (pages=n/a-n/a, score=0.8969, semantic=0.8609, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [5] FAQ Admission en Master / Une question sur la plateforme MonMaster? (pages=n/a-n/a, score=0.8933, semantic=0.8573, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master

**Faits de référence (non transmis au modèle) :**

- Une personne déjà titulaire d'un master peut candidater à un nouveau master
- Il n'est pas possible de se réinscrire dans un parcours de master déjà acquis

## q050. Quels sont les débouchés professionnels après une formation à l'Inalco ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `clarify`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4495 caractères`

**Reponse :**

Les débouchés professionnels après une formation à l'Inalco sont variés et dépendent du type de diplôme obtenu. Voici quelques exemples de débouchés professionnels :

1. **Master Traitement automatique des langues (TAL)** :
   - **Startups spécialisées** : Metyis, Aday, Proxem, Labsense, Cerence, Viasema, Nunki.co, Linagora, Clustaar, etc.
   - **Grandes entreprises** : Orange, BNP Paribas, Dassault Systèmes, SNCF, Agence spatiale européenne, Systran, Acolad.
   - **Métiers de niveau ingénieur** : Production, organisation et gestion de l'information numérique.

2. **Diplômes d'établissement** :
   - **Diplôme d'initiation (DIN)**
   - **Diplôme intensif**
   - **Diplôme de langue et civilisation (DLC)**
   - **Diplôme de langue (DL)**
   - **Diplôme de civilisation (DC)**
   - **Diplôme professionnel de commerce international et langue orientale (DP CILO)**
   - **Certificat de langue (CL)**
   - **Certificat de langue et civilisation (CLC)**

Ces diplômes sont axés sur l’acquisition de connaissances et de compétences relatives à une langue et sa civilisation, ou sur une approche pluridisciplinaire d’une région.

Pour plus d'informations sur les débouchés professionnels spécifiques à chaque diplôme, vous pouvez consulter les pages dédiées aux formations sur le site officiel de l'Inalco.

Sources :
- [Master Traitement automatique des langues (TAL)](https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal)
- [Diplômes d'établissement](https://www.inalco.fr/formations/diplomes-detablissement)

**Sources recuperees :**

- [1] Master Traitement automatique des langues (TAL) / Débouchés professionnels (pages=n/a-n/a, score=0.869, semantic=0.851, dans_contexte=oui)  https://www.inalco.fr/formations/master-traitement-automatique-des-langues-tal
- [2] Diplômes d'établissement / Diplômes d'établissement (pages=n/a-n/a, score=0.8639, semantic=0.8459, dans_contexte=oui)  https://www.inalco.fr/formations/diplomes-detablissement
- [3] Diplômes d'établissement / Nos formations proposées en diplômes d'établissement (pages=n/a-n/a, score=0.8543, semantic=0.8363, dans_contexte=oui)  https://www.inalco.fr/formations/diplomes-detablissement
- [4] Diplômes d'établissement - Brochures / Brochures par département (pages=n/a-n/a, score=0.8542, semantic=0.8362, dans_contexte=oui)  https://www.inalco.fr/diplomes-detablissement-brochures
- [5] Diplômes d'établissement - Brochures / Brochures des diplômes universitaires et du diplôme professionnel (pages=n/a-n/a, score=0.8524, semantic=0.8344, dans_contexte=oui)  https://www.inalco.fr/diplomes-detablissement-brochures

## q052. Que faire si un cours ou un groupe n'apparaît pas dans mon emploi du temps ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5909 caractères`

**Reponse :**

Si un cours ou un groupe n'apparaît pas dans votre emploi du temps, voici les étapes à suivre :

1. **Sélectionner la rubrique "Promotions"**.
2. **Sélectionner la recherche "saisie du nom"** et saisissez une langue, un diplôme et un niveau. Par exemple : japonais L2, hongrois L1, malgache L1, arabe maghrébin L2, etc.
3. **Visualisez le planning** du parcours en cliquant sur **"Personnalisée"** en haut à gauche du calendrier, puis choisissez **"Semestre 1"** ou **"Semestre 2"**.
4. **Afficher les détails d’un cours** : si le numéro de salle ou le nom de l’enseignante ou de l’enseignant n’apparaît pas, cliquez sur la case : une fenêtre s’ouvrira avec toutes les informations.
5. **Cours simultanés ?** Cliquez sur les chiffres 1, 2 ou 3 à gauche de la case pour afficher les différents cours proposés sur une plage horaire commune.
6. **Enseignements transversaux disciplinaires (L2/L3)** : cherchez **"Parcours"** et sélectionnez votre parcours (ex: Parcours Oralité, Parcours Arts du monde, etc.).
7. **Enseignements de civilisation** : cherchez par le nom de la région ou du département, par exemple "Asie du sud -- civilisation L1", "Eurasie -- civilisation L1", etc.

Si après ces étapes le cours ou le groupe n'apparaît toujours pas, il est possible que le cours soit en cours de mise à jour ou qu'il y ait une erreur dans le planning. Dans ce cas, il est recommandé de contacter le service de scolarité ou de consulter le site officiel pour obtenir des informations supplémentaires.

Sources :
- [Dates et calendriers](https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html)
- [Emplois du temps](https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html)

**Sources recuperees :**

- [1] Dates et calendriers / Comment utiliser le planning des cours (pages=n/a-n/a, score=0.8351, semantic=0.8351, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/scolarite-au-quotidien/calendrier-universitaire.html
- [2] Emplois du temps / Comment utiliser le planning ? (pages=n/a-n/a, score=0.833, semantic=0.833, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html
- [3] Tutorat / Vous êtes étudiant en L1, L2, L3 LLCER : (pages=n/a-n/a, score=0.8312, semantic=0.8312, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/tutorat.html
- [4] Emplois du temps / Comment utiliser le planning ? (pages=n/a-n/a, score=0.8299, semantic=0.8299, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/emplois-du-temps.html
- [5] Tutorat / Vous êtes étudiant en parcours aménagé L1+ ou Tempo 1.1 : (pages=n/a-n/a, score=0.8293, semantic=0.8293, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/tutorat.html

**Faits de référence (non transmis au modèle) :**

- Les enseignements transversaux disciplinaires de L2 et L3 ne figurent pas dans le planning principal du parcours
- Pour les retrouver, il faut rechercher la rubrique Parcours et sélectionner le parcours concerné
- Les enseignements de civilisation communs à plusieurs langues doivent être recherchés par aire géographique ou département
- Pour afficher plusieurs cours simultanés, il faut utiliser les chiffres affichés à gauche de la plage horaire

## q053. Comment accéder à Moodle et retrouver les espaces de mes cours ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5425 caractères`

**Reponse :**

Pour accéder à Moodle et retrouver les espaces de vos cours, suivez ces étapes :

1. **Inscription administrative et pédagogique** : Assurez-vous d'avoir effectué votre inscription administrative et votre inscription pédagogique (IP) à l'Inalco.
2. **Activation de votre compte numérique Inalco** : Activez votre compte numérique Inalco sur [https://compte.inalco.fr/](https://compte.inalco.fr/).
3. **Connexion à Moodle** : Connectez-vous à Moodle en entrant votre numéro d'étudiant et le mot de passe choisi lors de l'activation de votre compte numérique Inalco.
4. **Tableau de bord** : Une fois connecté, vous serez dirigé vers votre espace personnel, le tableau de bord, qui contient la liste des cours auxquels vous êtes inscrit pédagogiquement. Seuls les cours ouverts par vos enseignants sont visibles.

Si vous rencontrez des problèmes sur Moodle, vous pouvez signaler le problème à l'assistance en envoyant un email à [assistance-moodle@inalco.fr](mailto:assistance-moodle@inalco.fr) avec une capture d'écran.

Sources :
- [Services et ressources numériques - Moodle](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html)

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

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `4613 caractères`

**Reponse :**

Pour activer votre compte numérique étudiant, suivez ces étapes :

1. **Accédez au site de création de compte numérique** : [https://compte.inalco.fr/](https://compte.inalco.fr/)
2. **Entrez l’adresse e-mail personnelle** que vous avez fournie lors de votre inscription à l’Inalco.
3. **Cliquez sur « Valider »**. Vous recevrez un mail avec un lien actif vous permettant de réinitialiser votre mot de passe.
4. **Notez bien votre identifiant usager** et choisissez soigneusement votre mot de passe, car ils vous seront demandés pour vos futures connexions.

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

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5408 caractères`

**Reponse :**

Les étudiantes et étudiants de l'Inalco disposent d'une adresse électronique institutionnelle. Cette adresse est utilisée pour diverses communications institutionnelles, notamment pour l'activation de la carte étudiante multiservice IZLY, qui permet de gérer et de recharger le compte en ligne. Pour plus d'informations sur l'activation de cette carte, vous pouvez consulter la page dédiée sur le portail étudiant de l'Inalco.

Sources :
- [Se nourrir](https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html)

**Sources recuperees :**

- [1] Inscriptions pédagogiques / Procédure Master (pages=n/a-n/a, score=0.8738, semantic=0.8238, dans_contexte=oui)  https://www.inalco.fr/inscriptions-pedagogiques
- [2] Foire aux questions (FAQ) - Procédure d'inscription / Contacts en cas de difficultés (pages=n/a-n/a, score=0.8716, semantic=0.8216, dans_contexte=oui)  https://www.inalco.fr/foire-aux-questions-faq-procedure-dinscription
- [3] Se nourrir / Comment payer ? (pages=n/a-n/a, score=0.8697, semantic=0.8197, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html
- [4] Se rendre à l'Inalco / La Maison de la recherche (pages=n/a-n/a, score=0.869, semantic=0.806, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-rendre-a-l-inalco.html
- [5] Mobilités hors Erasmus+ / Déroulement de la candidature auprès de l'université partenaire (pages=n/a-n/a, score=0.8675, semantic=0.8175, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-hors-erasmus.html

## q058. Quels outils et services numériques sont utiles pour suivre ma scolarité ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4589 caractères`

**Reponse :**

Pour suivre votre scolarité à l'Inalco, plusieurs outils et services numériques sont disponibles :

1. **Moodle** : Cette plateforme pédagogique en ligne permet d'accéder à des cours, des devoirs, des évaluations et des activités de travail collaboratif. Vous pouvez également consulter la FAQ Moodle pour les étudiants sur la page d'accueil de Moodle.

2. **Portail Étudiant** : Vous pouvez consulter vos notes et votre certificat de scolarité en vous connectant au Portail Étudiant avec vos identifiants numériques (moodle, eduspot, etc.). Si vous n'avez pas encore initialisé votre compte numérique, consultez la page suivante : [Services et ressources numériques](/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html). Si vous rencontrez des problèmes pour vous authentifier, contactez l'assistance à l'adresse suivante : [assistance-portail-etudiant@inalco.fr](mailto:assistance-portail-etudiant@inalco.fr).

3. **Application IZLY** : Disponible sur les principaux stores de téléchargement, cette application permet de gérer vos services et ressources numériques.

4. **Service REVE** : Ce service renouvelle les prêts d'ordinateurs et/ou de galets 4G pour vous aider en cas de difficultés de connexion ou de manque de matériel informatique.

Sources :
- [Services et ressources numériques](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html)
- [Consulter ses notes et son certificat de scolarité](https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html)

**Sources recuperees :**

- [1] Services et ressources numériques / Services et ressources numériques (pages=n/a-n/a, score=0.865, semantic=0.865, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [2] Services et ressources numériques / Carte multi-services étudiante (pages=n/a-n/a, score=0.8637, semantic=0.8637, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [3] Services et ressources numériques / Moodle (pages=n/a-n/a, score=0.8629, semantic=0.8629, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [4] Consulter ses notes et son certificat de scolarité / 1-Se connecter au Portail Étudiant (pages=n/a-n/a, score=0.8613, semantic=0.8613, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [5] Consulter ses notes et son certificat de scolarité / 1-Se connecter au Portail Étudiant (pages=n/a-n/a, score=0.8547, semantic=0.8547, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html

**Faits de référence (non transmis au modèle) :**

- Le compte numérique Inalco donne accès aux services numériques étudiants
- Moodle permet d'accéder à des outils pédagogiques et à des contenus de cours à distance
- Le service REVE propose sous conditions des prêts d'ordinateurs et de galets 4G aux étudiants rencontrant des difficultés matérielles

## q059. Où consulter mes notes et mes résultats d'examen ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `3773 caractères`

**Reponse :**

Pour consulter vos notes et vos résultats d'examen, vous pouvez suivre les étapes suivantes :

1. Connectez-vous au Portail Étudiant en utilisant vos identifiants numériques (moodle, eduspot, etc.).
2. Une fois connecté, allez dans la rubrique **"Mon espace perso"** située à droite de votre écran d'ordinateur ou en bas à droite de votre écran de smartphone.
3. Sélectionnez **"Ma scolarité"** puis cliquez sur **"Certificat & notes"**.
4. Cela vous redirigera vers **"MonDossierEtudiant"** où vous pourrez consulter vos notes et votre contrat pédagogique.

Sources :
- [Consulter ses notes et son certificat de scolarité](https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html)

**Sources recuperees :**

- [1] Consulter ses notes et son certificat de scolarité / 3-Consulter ses notes (pages=n/a-n/a, score=0.8877, semantic=0.8697, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [2] Consulter ses notes et son certificat de scolarité / 2-Accéder à mon dossier de scolarité (pages=n/a-n/a, score=0.8804, semantic=0.8624, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [3] Consulter ses notes et son certificat de scolarité / Consulter ses notes et son certificat de scolarité (pages=n/a-n/a, score=0.8756, semantic=0.8576, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [4] Consulter ses notes et son certificat de scolarité / 1-Se connecter au Portail Étudiant (pages=n/a-n/a, score=0.8734, semantic=0.8554, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [5] Consulter ses notes et son certificat de scolarité / Poursuivez le tutoriel ! (pages=n/a-n/a, score=0.8732, semantic=0.8552, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html

**Faits de référence (non transmis au modèle) :**

- Les notes sont consultables depuis le Portail étudiant
- L'accès utilise les identifiants du compte numérique Inalco
- Dans l'espace de scolarité, MonDossierEtudiant permet de consulter les résultats enregistrés

## q060. Comment télécharger mon certificat de scolarité ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
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

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5682 caractères`

**Reponse :**

Pour effectuer ou renouveler votre inscription administrative à l'Inalco, suivez ces étapes :

1. **Connectez-vous à la plateforme PEGASE** : Vous devez vous connecter à la plateforme PEGASE pour procéder à votre inscription administrative. Le lien pour accéder à PEGASE est disponible sur la page des inscriptions administratives de l'Inalco.

2. **Paiement des droits de scolarité** : Le paiement des droits de scolarité est obligatoire et doit être effectué en ligne. Les tarifs sont disponibles sur la page des droits de scolarité.

3. **Dépôt des pièces justificatives** : Après avoir payé les droits de scolarité, vous devrez envoyer vos pièces justificatives à l'adresse indiquée sur le récapitulatif de votre inscription en ligne.

4. **Obtention du certificat de scolarité** : Une fois que votre dossier est complet et validé, vous recevrez un certificat de scolarité sur le portail étudiant de l'Inalco.

Pour plus de détails, consultez les pages suivantes :
- [Inscription et réinscription administrative](https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-administrative.html)
- [Inscriptions administratives](https://www.inalco.fr/inscriptions-administratives)

Sources :
- [Inscription et réinscription administrative](https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-administrative.html)
- [Inscriptions administratives](https://www.inalco.fr/inscriptions-administratives)

**Sources recuperees :**

- [1] Inscription et réinscription administrative / Inscription et réinscription administrative (pages=n/a-n/a, score=0.8877, semantic=0.8697, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-administrative.html
- [2] Inscriptions administratives / Procédure d'inscription administrative (pages=n/a-n/a, score=0.8785, semantic=0.8605, dans_contexte=oui)  https://www.inalco.fr/inscriptions-administratives
- [3] Inscription et réinscription administrative / Pour connaître les dates et modalités d'inscription et réinscription administrative, consultez la page ci-dessous (pages=n/a-n/a, score=0.878, semantic=0.86, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions/inscription-et-reinscription-administrative.html
- [4] Inscriptions administratives / Procédure d'inscription administrative (pages=n/a-n/a, score=0.8706, semantic=0.8526, dans_contexte=oui)  https://www.inalco.fr/inscriptions-administratives
- [5] Candidatures et réinscriptions / Candidatures et réinscriptions (pages=n/a-n/a, score=0.869, semantic=0.851, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/etudes/candidatures-et-re-inscriptions.html

**Faits de référence (non transmis au modèle) :**

- L'inscription ou la réinscription administrative est annuelle et obligatoire
- Elle comprend le paiement des droits de scolarité et le dépôt des pièces justificatives sur PEGASE
- Elle permet d'obtenir le statut d'étudiant et le certificat de scolarité après validation
- L'inscription pédagogique intervient ensuite

## q063. Que faire si je constate une erreur dans mon inscription pédagogique ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5760 caractères`

**Reponse :**

Si vous constatez une erreur dans votre inscription pédagogique, vous devez suivre les étapes suivantes :

1. **Consulter les fiches d'inscription pédagogique** : Vous trouverez l'ensemble des fiches IP à compléter sur la page [Fiches d'inscription pédagogique](https://www.inalco.fr/fiches-dinscription-pedagogique). Les documents sont à signer et faire signer par les enseignants responsables avant dépôt au bureau des masters LLCER : bureau 3.48 / boîte aux lettres H.

2. **Envoyer un email** : Si vous êtes inscrit en Licence dans votre établissement principal, envoyez un email au secrétariat pédagogique de la langue étudiée. Si vous êtes inscrit en Master ou en Doctorat, envoyez un email au bureau des Masters. Le mail doit comprendre obligatoirement les informations suivantes :
   - votre numéro étudiant
   - votre nom de naissance
   - votre prénom
   - le nom de l'établissement public d'enseignement supérieur et de recherche en France dans lequel vous êtes inscrit au titre de 2026/2027. Vous devrez joindre dans ce formulaire votre certificat de scolarité 2026/2027
   - le niveau dans lequel vous êtes inscrit dans votre établissement principal (Lice...

3. **Télécharger et envoyer le contrat pédagogique** : Une fois votre inscription pédagogique validée, vous devez télécharger votre contrat pédagogique avant de vous déconnecter. Ce contrat pédagogique est à envoyer par mail à votre gestionnaire pédagogique avec, UNIQUEMENT pour les L2 et les L3, vos choix de matières pour les UE3 et / ou UE4 avec le code et le nom de la matière.

Sources :
- [Inscriptions pédagogiques](https://www.inalco.fr/inscriptions-pedagogiques)

**Sources recuperees :**

- [1] Inscriptions pédagogiques / Procédure Master (pages=n/a-n/a, score=0.8677, semantic=0.8497, dans_contexte=oui)  https://www.inalco.fr/inscriptions-pedagogiques
- [2] Inscriptions pédagogiques / Inscriptions pédagogiques (pages=n/a-n/a, score=0.8556, semantic=0.8376, dans_contexte=oui)  https://www.inalco.fr/inscriptions-pedagogiques
- [3] Inscriptions pédagogiques / Inscriptions pédagogiques (pages=n/a-n/a, score=0.855, semantic=0.837, dans_contexte=oui)  https://www.inalco.fr/inscriptions-pedagogiques
- [4] Inscriptions pédagogiques / Précision parcours Tempo et L1+ (pages=n/a-n/a, score=0.8548, semantic=0.8368, dans_contexte=oui)  https://www.inalco.fr/inscriptions-pedagogiques
- [5] Inscriptions pédagogiques / Inscriptions pédagogiques (pages=n/a-n/a, score=0.8533, semantic=0.8353, dans_contexte=non)  https://www.inalco.fr/inscriptions-pedagogiques

## q064. Puis-je changer de groupe de cours après la validation de mon inscription pédagogique ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5819 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Inscriptions pédagogiques / Choix des groupes : (pages=n/a-n/a, score=0.8689, semantic=0.8509, dans_contexte=oui)  https://www.inalco.fr/inscriptions-pedagogiques
- [2] Inscriptions pédagogiques / Choix des groupes : (pages=n/a-n/a, score=0.8669, semantic=0.8489, dans_contexte=oui)  https://www.inalco.fr/inscriptions-pedagogiques
- [3] Inscriptions pédagogiques / Inscriptions pédagogiques (pages=n/a-n/a, score=0.859, semantic=0.841, dans_contexte=oui)  https://www.inalco.fr/inscriptions-pedagogiques
- [4] Inscriptions pédagogiques / Procédure Master (pages=n/a-n/a, score=0.8584, semantic=0.8404, dans_contexte=oui)  https://www.inalco.fr/inscriptions-pedagogiques
- [5] Inscriptions pédagogiques / Inscriptions pédagogiques (pages=n/a-n/a, score=0.8553, semantic=0.8373, dans_contexte=non)  https://www.inalco.fr/inscriptions-pedagogiques

## q065. Est-il possible de changer d'option, de matière ou de parcours pendant l'année ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `clarify`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5955 caractères`

**Reponse :**

Réponse :
Non, il n'est pas possible de changer d'option, de matière ou de parcours pendant l'année. Les parcours et les options sont définis au début de l'année académique et ne peuvent pas être modifiés par la suite.

Sources :
- [Source 1]
- [Source 2]
- [Source 3]
- [Source 4]
- [Source 5]

**Sources recuperees :**

- [1] Conventions de stage / Puis-je faire le même stage deux années de suite (exemple en master) ? (pages=n/a-n/a, score=0.8501, semantic=0.8321, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html
- [2] Conventions de stage / Puis-je faire un stage non obligatoire dans le cadre d’un diplôme de Licence LLCER ? (pages=n/a-n/a, score=0.8489, semantic=0.8309, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html
- [3] Master TI - Traduction spécialisée / Master TI - Traduction spécialisée (pages=n/a-n/a, score=0.8489, semantic=0.8129, dans_contexte=oui)  https://www.inalco.fr/formations/master-ti-traduction-specialisee
- [4] Master TI - Traduction spécialisée / Master TI - Traduction spécialisée (pages=n/a-n/a, score=0.8486, semantic=0.8126, dans_contexte=oui)  https://www.inalco.fr/formations/master-ti-traduction-specialisee
- [5] Master TI - Traduction spécialisée / FAQ (pages=n/a-n/a, score=0.848, semantic=0.812, dans_contexte=oui)  https://www.inalco.fr/formations/master-ti-traduction-specialisee

## q066. Comment trouver les coordonnées de mon gestionnaire ou de mon secrétariat pédagogique ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `4712 caractères`

**Reponse :**

Pour trouver les coordonnées de votre gestionnaire ou de votre secrétariat pédagogique, vous pouvez consulter l'annuaire officiel de l'Inalco. Voici les coordonnées disponibles dans l'annuaire :

- **Direction générale des services (DGS)** : [dgs@inalco.fr](mailto:dgs@inalco.fr)
- **Service de réussite étudiante** : [reussite-etudiante@inalco.fr](mailto:reussite-etudiante@inalco.fr)

Ces contacts sont disponibles sur la page de l'annuaire de l'Inalco : [Annuaire](https://portail-etudiant.inalco.fr/fr/autres/annuaire.html).

Sources :
- [Annuaire](https://portail-etudiant.inalco.fr/fr/autres/annuaire.html)

**Sources recuperees :**

- [1] Annuaire / Contacts (pages=n/a-n/a, score=0.8491, semantic=0.8491, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/annuaire.html
- [2] Consulter ses notes et son certificat de scolarité / 1-Se connecter au Portail Étudiant (pages=n/a-n/a, score=0.843, semantic=0.843, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [3] Annuaire / Contacts (pages=n/a-n/a, score=0.8417, semantic=0.8417, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/annuaire.html
- [4] Tutorat / Tuteurs : à qui vous adresser ? (pages=n/a-n/a, score=0.8402, semantic=0.8402, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/tutorat.html
- [5] Parcours L1+ / Inscriptions (pages=n/a-n/a, score=0.8389, semantic=0.8389, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/etudes/accompagnement-vers-la-reussite/parcours-l1.html

**Faits de référence (non transmis au modèle) :**

- L'annuaire de l'Inalco réunit les coordonnées des services et composantes
- Le secrétariat ou le gestionnaire compétent dépend du département, de la langue ou de la filière de l'étudiant
- Le standard de l'Inalco peut transférer les appels vers le service concerné au 01 81 70 10 00

## q067. Qui dois-je prévenir en cas d'absence à un cours ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5497 caractères`

**Reponse :**

Pour prévenir en cas d'absence à un cours, vous devez informer votre enseignant référent. Vous pouvez le faire par courriel en indiquant votre numéro étudiant, votre nom, prénom, et la raison de votre absence.

**Sources recuperees :**

- [1] Droits de scolarité : tarifs, exonération, annulation, remboursement / Annulation et remboursement d'inscription (pages=n/a-n/a, score=0.8161, semantic=0.8161, dans_contexte=oui)  https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement
- [2] Tutorat / Vous êtes étudiant en L1, L2, L3 LLCER : (pages=n/a-n/a, score=0.8156, semantic=0.8156, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/tutorat.html
- [3] Psychologue / **Dispositif Santé Psy Étudiant** (pages=n/a-n/a, score=0.8154, semantic=0.8154, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/suivi-par-des-professionnels/psychologue.html
- [4] Inscriptions pédagogiques / Inscriptions pédagogiques (pages=n/a-n/a, score=0.8149, semantic=0.8149, dans_contexte=oui)  https://www.inalco.fr/inscriptions-pedagogiques
- [5] Urgences / **Urgences médicales** (pages=n/a-n/a, score=0.8146, semantic=0.8146, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/autres/urgences.html

## q069. Où trouver les dates et les salles de mes prochains examens ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4831 caractères`

**Reponse :**

Pour trouver les dates et les salles de vos prochains examens, vous pouvez consulter la section "Examens" du site officiel de l'Inalco. Voici le lien vers cette page : [Examens](https://www.inalco.fr/examens).

Sources :
- [Examens](https://www.inalco.fr/examens)

**Sources recuperees :**

- [1] Examens / Examens (pages=n/a-n/a, score=0.8591, semantic=0.8411, dans_contexte=oui)  https://www.inalco.fr/examens
- [2] Consulter ses notes et son certificat de scolarité / 1-Se connecter au Portail Étudiant (pages=n/a-n/a, score=0.859, semantic=0.841, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [3] Consulter ses notes et son certificat de scolarité / 4-Télécharger son certificat de scolarité (pages=n/a-n/a, score=0.8584, semantic=0.8404, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [4] Consulter ses notes et son certificat de scolarité / 4-Télécharger son certificat de scolarité (pages=n/a-n/a, score=0.8562, semantic=0.8382, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html
- [5] Consulter ses notes et son certificat de scolarité / 2-Accéder à mon dossier de scolarité (pages=n/a-n/a, score=0.8557, semantic=0.8377, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/aide/consulter-son-dossier-de-scolarite.html

**Faits de référence (non transmis au modèle) :**

- La rubrique Examens du portail étudiant contient des sous-pages pour les examens du premier semestre, du second semestre et les rattrapages
- Les informations publiées sur ces sous-pages permettent de consulter l'organisation des sessions correspondantes

## q070. Comment fonctionnent les examens de rattrapage à l'Inalco ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4510 caractères`

**Reponse :**

Les examens de rattrapage à l'Inalco sont organisés pour permettre aux étudiants de réussir leurs cours en cas d'échec. Les informations spécifiques sur les dates, les modalités et les procédures pour les examens de rattrapage ne sont pas détaillées dans le contexte fourni. Pour obtenir des informations précises sur les examens de rattrapage, je vous recommande de consulter la page officielle des examens de l'Inalco : [Examens](https://www.inalco.fr/examens).

Sources :
- [Examens](https://www.inalco.fr/examens)

**Sources recuperees :**

- [1] Examens / Examens (pages=n/a-n/a, score=0.8724, semantic=0.8544, dans_contexte=oui)  https://www.inalco.fr/examens
- [2] FAQ Admission en Master / Y a-t-il des examens/concours d’entrée pour certains Masters ? (pages=n/a-n/a, score=0.8678, semantic=0.8498, dans_contexte=oui)  https://www.inalco.fr/faq-admission-en-master
- [3] Aide au voyage / Quand partir ? (pages=n/a-n/a, score=0.865, semantic=0.847, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/aide-au-voyage.html
- [4] Bien-être / Relax' Exams (pages=n/a-n/a, score=0.8606, semantic=0.8546, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/bien-etre.html
- [5] Examens / Examens (pages=n/a-n/a, score=0.86, semantic=0.842, dans_contexte=oui)  https://www.inalco.fr/examens

## q073. Où consulter les règlements des études et les modalités de contrôle des connaissances ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5163 caractères`

**Reponse :**

Pour consulter les règlements des études et les modalités de contrôle des connaissances à l'Inalco, vous pouvez vous rendre sur la page suivante : [Règlements et chartes étudiantes](https://www.inalco.fr/reglements-et-chartes-etudiantes).

Cette page contient les documents suivants :
- Les modalités de contrôle des connaissances (MCC) pour l'année 2025-2026.
- Les modalités de contrôle des connaissances (MCC) pour l'année 2024-2025 - Cadrage général.
- Les modalités de contrôle des connaissances - annexe Réussite étudiante - Licence +.
- Les dispositions spécifiques Licences LAS 2024-2025.

Ces documents détaillent les règles essentielles applicables en matière de régime d'inscription au contrôle des connaissances, des modes d'évaluation, du calcul des résultats, du passage en année supérieure, de l'assiduité aux cours et examens, et de la césure.

Sources :
- [Règlements et chartes étudiantes](https://www.inalco.fr/reglements-et-chartes-etudiantes)

**Sources recuperees :**

- [1] Règlements et chartes étudiantes / Modalités de contrôle des connaissances (pages=n/a-n/a, score=0.8557, semantic=0.8557, dans_contexte=oui)  https://www.inalco.fr/reglements-et-chartes-etudiantes
- [2] Règlements et chartes étudiantes / Annexes aux MCC (pages=n/a-n/a, score=0.8456, semantic=0.8456, dans_contexte=oui)  https://www.inalco.fr/reglements-et-chartes-etudiantes
- [3] Règlements et chartes étudiantes / Charte de bon usage des outils de visioconférence (pages=n/a-n/a, score=0.8363, semantic=0.8363, dans_contexte=oui)  https://www.inalco.fr/reglements-et-chartes-etudiantes
- [4] Règlements et chartes étudiantes / Charte des examens (pages=n/a-n/a, score=0.8339, semantic=0.8339, dans_contexte=oui)  https://www.inalco.fr/reglements-et-chartes-etudiantes
- [5] Etudier à l'étranger / Responsables des Relations Internationales (RRI) des départements : (pages=n/a-n/a, score=0.8329, semantic=0.8329, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger.html

**Faits de référence (non transmis au modèle) :**

- Les modalités de contrôle des connaissances sont publiées dans la rubrique Règlements et chartes étudiantes
- Elles couvrent les modes d'évaluation, le calcul des résultats, la compensation et la capitalisation
- Elles précisent aussi le passage en année supérieure et les règles d'assiduité
- Des annexes spécifiques sont publiées pour certains dispositifs ou formations

## q074. Comment demander un aménagement d'études ou d'examens en raison d'un handicap ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5004 caractères`

**Reponse :**

Pour demander un aménagement d'études ou d'examens en raison d'un handicap à l'Inalco, vous devez suivre les étapes suivantes :

1. **Prendre rendez-vous avec la Mission Handicap** :
   - Vous pouvez prendre rendez-vous par mail à [handicap@inalco.fr](mailto:handicap@inalco.fr) en donnant plusieurs disponibilités pour des propositions de rendez-vous aux horaires d'ouverture : du lundi au vendredi de 9h30 à 16h30.
   - Les étudiantes et étudiants souhaitant renouveler leur PAEH ou nouvellement inscrits peuvent prendre rendez-vous par mail jusqu’au jeudi 18 juillet 2025, puis à partir du 20 août 2025.

2. **Remplir le formulaire en ligne** :
   - Pour toute demande d’aménagement d’examen, seules les étudiantes et étudiants disposant d’un PAEH validé peuvent compléter et envoyer le formulaire en ligne.
   - Le formulaire est disponible à partir du 20/11/25 et doit être rempli avant le 16/12/25 à minuit.
   - Les examens terminaux pour le semestre 1 pour les filières auront lieu la semaine du 15 décembre au 19 décembre 2025.
   - Les examens terminaux pour le semestre 1 pour les autres départements auront lieu du 6 janvier au 17 janvier 2026.

3. **Contacter la Mission Handicap pour des aménagements exceptionnels** :
   - Les étudiantes et étudiants ne disposant pas d’un PAEH validé, mais victimes d’un accident quelques jours avant ou pendant la période des examens et susceptibles de rencontrer des difficultés lors des épreuves, peuvent demander des aménagements.
   - Ils doivent contacter par mail la Mission Handicap avant le début des examens et transmettre un justificatif médical établi par un médecin.

Sources :
- [Mission Handicap - Procédure de la mise en place du plan d'accompagnement (PAEH)](https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html)
- [Mission Handicap - Dem

**Sources recuperees :**

- [1] Mission Handicap / Procédure de la mise en place du plan d'accompagnement (PAEH) (pages=n/a-n/a, score=0.8667, semantic=0.8607, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [2] Mission Handicap / Demande d'aménagement d'examen (pages=n/a-n/a, score=0.8653, semantic=0.8593, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [3] Mission Handicap / Etudiants sans PAEH (pages=n/a-n/a, score=0.8641, semantic=0.8581, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [4] Mission Handicap / Procédure de la mise en place du plan d'accompagnement (PAEH) (pages=n/a-n/a, score=0.8578, semantic=0.8518, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [5] Mission Handicap / Mission Handicap (pages=n/a-n/a, score=0.8564, semantic=0.8504, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html

**Faits de référence (non transmis au modèle) :**

- Une demande d'aménagement d'examen nécessite un PAEH validé par la Mission Handicap
- Le formulaire doit être rempli pour chaque semestre et chaque session d'examen, y compris les rattrapages
- Les aménagements demandés doivent correspondre à ceux notifiés dans le PAEH
- Le formulaire doit être envoyé après la publication des dates d'examen

## q075. À qui m'adresser en cas de difficulté personnelle ou de mal-être ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5395 caractères`

**Reponse :**

Pour toute difficulté personnelle ou de mal-être, vous pouvez vous adresser à plusieurs services à l'Inalco :

1. **Psychologue de l'Inalco** : Vous pouvez envoyer un email à soutien-psy@inalco.fr pour prendre rendez-vous avec un psychologue. Les consultations sont disponibles à tout moment de l'année universitaire et en toute confidentialité.

2. **SOS suicide** : Si vous ou un proche ressentez une détresse psychologique ou des idées suicidaires, contactez le 3114 (numéro national de prévention du suicide, 24h/24) ou composez le 15 (SAMU) pour une prise en charge médicale urgente.

3. **Consultation au centre de santé étudiante** : Plusieurs psychologues sont disponibles pour des consultations d’aide, d’écoute et de suivi psychologique. Vous pouvez également consulter des médecins psychiatres pour des problèmes spécifiques comme la dépression, les troubles obsessionnels compulsifs (TOC), les troubles du comportement alimentaire, ou l’anxiété.

4. **Mission Handicap** : Si vous êtes en situation de handicap ou rencontrez des difficultés de santé, vous pouvez bénéficier des services d’aménagement proposés par l’Inalco. Contactez la mission Handicap pour plus d’informations.

5. **Acca : la ligne d’écoute et soutien psychologique** : Anonyme, gratuit et disponible 24h/24, 7j/7, la ligne d’écoute du Crous met à votre disposition un numéro d’appel : 0800 73 08 15. Les psychologues vous écoutent à tout moment pour comprendre votre situation.

Sources :
- [Psychologue de l'Inalco](https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/sante.html)
- [SOS suicide](https://portail-etudiant.inalco.fr/fr/autres/urgences.html)
- [Consultation au centre de santé étudiante](https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/suivi-par-des-professionnels/psychologue.html)
- [Mission Handicap](https://portail-etudiant.inalco.fr/fr/a

**Sources recuperees :**

- [1] Santé / Psychologue de l'Inalco (pages=n/a-n/a, score=0.8323, semantic=0.8323, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/sante.html
- [2] Urgences / **SOS suicide** (pages=n/a-n/a, score=0.8316, semantic=0.8316, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/urgences.html
- [3] Psychologue / **Consultation au centre de santé étudiante** (pages=n/a-n/a, score=0.8241, semantic=0.8241, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/suivi-par-des-professionnels/psychologue.html
- [4] Mission Handicap / Mission Handicap (pages=n/a-n/a, score=0.8237, semantic=0.8237, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/etudiant-a-statut-particulier/mission-handicap.html
- [5] Santé / Acca : la ligne d’écoute et soutien psychologique (pages=n/a-n/a, score=0.8203, semantic=0.8203, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/sante.html

**Faits de référence (non transmis au modèle) :**

- Un rendez-vous avec la psychologue de l'Inalco peut être demandé à soutien-psy@inalco.fr
- Les consultations peuvent concerner notamment le stress, la dépression, les difficultés relationnelles, l'alimentation ou les addictions
- Les consultations psychologiques sont confidentielles
- En cas d'idées suicidaires, le 3114 est disponible 24 heures sur 24 et le 15 doit être appelé en cas d'urgence médicale

## q076. Quels services de santé sont accessibles aux étudiantes et étudiants ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5722 caractères`

**Reponse :**

Les services de santé accessibles aux étudiantes et étudiants à l'Inalco incluent :

1. **Consultations médicales** : Le Service de Santé Étudiant (SSE) propose des consultations gratuites avec des professionnels de santé, notamment des médecins spécialisés en tabacologie, santé sexuelle, nutrition et médecine du sport, ainsi que des psychologues et des infirmières.

2. **Confidentialité** : Les consultations sont réalisées en toute confidentialité.

3. **Accès aux soins** : Les soins sont accessibles sur présentation de la carte étudiante, de la carte Vitale à jour (ou de son attestation) et, si nécessaire, de l’attestation de mutuelle. Les centres pratiquent le tiers payant intégral, ce qui signifie que vous n'aurez aucune avance de frais.

4. **Actions de proximité** : Le SSE organise des actions de proximité sur différentes thématiques de santé tout au long de l’année universitaire, en s’appuyant sur un réseau de partenaires.

5. **Étudiants Relais Santé (ERS)** : Les ERS assurent le lien entre les étudiantes et étudiants et les services de santé étudiante, les professionnelles et professionnels de santé, ainsi que les structures associatives, de prévention ou de soins. Ils facilitent le quotidien des étudiantes et étudiants en les informant et en les accompagnant sur les questions de santé.

Sources :
- [Service de Santé Étudiant (SSE)](https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/etudiants-relais-sante-ers.html)
- [Santé](https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/sante.html)
- [Etudiants Relais Santé (ERS)](https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/etudiants-relais-sante-ers.html)

**Sources recuperees :**

- [1] Etudiants Relais Santé (ERS) / Le Service de Santé Étudiant (SSE) (pages=n/a-n/a, score=0.8572, semantic=0.8572, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/etudiants-relais-sante-ers.html
- [2] Santé / Consultation médicale et médecine préventive (pages=n/a-n/a, score=0.856, semantic=0.856, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/sante.html
- [3] Etudiants Relais Santé (ERS) / Leurs missions (pages=n/a-n/a, score=0.8545, semantic=0.8545, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/etudiants-relais-sante-ers.html
- [4] Etudiants Relais Santé (ERS) / Présentation (pages=n/a-n/a, score=0.8492, semantic=0.8492, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/entraide-etudiante/etudiants-relais-sante-ers.html
- [5] Santé, sport et bien-être / Santé, sport et bien-être (pages=n/a-n/a, score=0.8448, semantic=0.8448, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre.html

**Faits de référence (non transmis au modèle) :**

- Le Service de Santé Étudiante propose des consultations aux étudiants
- Son équipe comprend notamment des médecins, psychologues, infirmières, sages-femmes et professionnels de la nutrition
- Les consultations sont confidentielles
- Le tiers payant intégral est appliqué sur présentation des justificatifs nécessaires selon la page collectée

## q078. Comment prendre rendez-vous avec l'assistante sociale de l'Inalco ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
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

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `3727 caractères`

**Reponse :**

Pour toute urgence concernant la sécurité ou la santé (malaise, accident, etc.), vous pouvez contacter immédiatement :

- **Ligne dédiée** : 01 81 69 18 19 ou 3000 depuis un poste interne.
- **Ou présentez-vous au rez-de-chaussée au Poste de Contrôle Sécurité** pour alerter le personnel.

En cas de malaise, blessure ou autre urgence médicale, alertez immédiatement le personnel de sécurité de l’établissement en composant le 01 81 69 18 19 ou 3000 depuis un poste interne. Si vous êtes en dehors de l'établissement, composez le 15 (SAMU) ou le 112 (urgence européenne).

Sources :
- [Urgences](https://portail-etudiant.inalco.fr/fr/autres/urgences.html)

**Sources recuperees :**

- [1] Urgences / Reporter un incident au sein de l’établissement (pages=n/a-n/a, score=0.8578, semantic=0.8578, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/urgences.html
- [2] Urgences / **Reporter un incident au sein de l’établissement** (pages=n/a-n/a, score=0.8549, semantic=0.8549, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/urgences.html
- [3] Urgences / Urgences médicales (pages=n/a-n/a, score=0.8488, semantic=0.8488, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/urgences.html
- [4] Urgences / **Urgences médicales** (pages=n/a-n/a, score=0.8455, semantic=0.8455, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/urgences.html
- [5] Urgences / **SOS suicide** (pages=n/a-n/a, score=0.8426, semantic=0.8426, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/autres/urgences.html

**Faits de référence (non transmis au modèle) :**

- Pour une urgence de sécurité ou de santé dans l'établissement, la ligne dédiée est le 01 81 69 18 19
- Depuis un poste interne, le numéro est le 3000
- Le Poste de Contrôle Sécurité se trouve au rez-de-chaussée
- En dehors de l'établissement, une urgence médicale peut être signalée au 15 ou au 112
- Une personne blessée ne doit pas être déplacée sauf en cas de danger immédiat

## q080. Quelles bourses et aides financières sont accessibles aux étudiants inscrits ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4275 caractères`

**Reponse :**

Réponse :
Les étudiants inscrits à l'Inalco peuvent bénéficier de plusieurs bourses et aides financières. Voici les principales aides disponibles :

1. **Bourses et aides sociales** : L'Inalco propose différentes aides sociales et bourses pour soutenir les étudiants en difficulté. Pour plus d'informations, consultez la page dédiée : [Bourses et aides sociales](https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-aides-sociales.html).

2. **Aides exceptionnelles du CROUS** : Des aides spécifiques existent pour répondre à des situations critiques. Pour en savoir plus, cliquez ici : [Aides exceptionnels du CROUS](https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-aides-sociales.html).

3. **Aide contre la précarité** : Un numéro d’urgence est dédié aux étudiants en situation de précarité. Vous pouvez appeler le 09 72 59 65 65 (prix d’un appel local, non surtaxé) du lundi au vendredi, de 9 h à 17 h.

4. **Bourses et aides pour l'année 2026-2027** : Les étudiants boursiers bénéficient de plusieurs avantages, notamment :
   - Priorité dans l’attribution des logements
   - Exonération des droits d’inscriptions
   - Exonération de la CVEC
   - Aide au mérite
   - Pass’Sport
   - Réduction dans les transports en commun en fonction des territoires
   - Action gratuite de nos partenaires

Pour déposer votre dossier de bourse avant le 31 mai 2026, consultez la page dédiée : [Lancement de la campagne de bourse et de logement étudiant 2026-2027](https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html).

Sources :
- [Bourses et aides sociales](https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-a

**Sources recuperees :**

- [1] Bourses et aides sociales / Bourses et aides sociales (pages=n/a-n/a, score=0.8741, semantic=0.8561, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-aides-sociales.html
- [2] Lancement de la campagne de bourse et de logement étudiant 2026-2027 / Quels sont les avantages d'être boursier ou boursière ? (pages=n/a-n/a, score=0.8727, semantic=0.8547, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html
- [3] Lancement de la campagne de bourse et de logement étudiant 2026-2027 / Quels sont les avantages d'être boursier ou boursière ? (pages=n/a-n/a, score=0.8717, semantic=0.8537, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html
- [4] Bourses et aides sociales / Aides exceptionnels du CROUS (pages=n/a-n/a, score=0.8693, semantic=0.8513, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-aides-sociales.html
- [5] Bourses et aides sociales / Aide contre la précarité (pages=n/a-n/a, score=0.868, semantic=0.85, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/bourses-et-aides-sociales.html

**Faits de référence (non transmis au modèle) :**

- L'Inalco présente différentes aides sociales et bourses destinées aux étudiants
- Les étudiants boursiers peuvent bénéficier d'une priorité pour l'attribution de logements
- Ils peuvent être exonérés des droits d'inscription et de la CVEC
- L'aide au mérite et le Pass'Sport figurent parmi les avantages mentionnés

## q082. Comment demander l'aide au voyage proposée par l'Inalco ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4994 caractères`

**Reponse :**

Pour demander l'aide au voyage proposée par l'Inalco, vous pouvez suivre les étapes suivantes :

1. **Réunion d'information** : Une réunion d'information aura lieu le jeudi 27 novembre 2025 à 18h15 en amphi 1. Cette réunion vous fournira tous les détails nécessaires sur les modalités, le montant, les critères de sélection et le calendrier.

2. **Exposition photo** : Vous pouvez également vous rendre dans le hall 2 pour découvrir l’exposition photo des camarades partis l’été dernier grâce à l’aide au voyage. L’exposition se tiendra les 27 et 28 novembre 2025.

3. **Documents utiles** : Si vous avez raté la réunion d'information, vous pouvez retrouver tous les détails dans les documents de présentation disponibles à la section "Documents utiles" sur la page officielle.

Pour plus d'informations, vous pouvez consulter la page dédiée à l'aide au voyage sur le portail étudiant de l'Inalco : [Aide au voyage](https://portail-etudiant.inalco.fr/fr/aide-et-accompagnements/aide-au-voyage.html).

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

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5908 caractères`

**Reponse :**

Pour candidater à une mobilité Erasmus+, il est nécessaire de suivre plusieurs étapes :

1. **Prendre connaissance de la Charte de l'étudiant Erasmus+** et consulter la liste des partenariats Erasmus+ de l'Inalco.
2. **Prendre contact avec l’enseignant responsable des relations internationales de votre département, avec un enseignant de votre cursus et avec votre responsable filière (le cas échéant)** pour discuter de votre projet de mobilité.
3. **Contacter la Direction des relations internationales** pour vous informer de la procédure de candidature et assister aux réunions d'informations organisées avant chaque campagne.
4. **Déposer votre dossier de candidature** via un formulaire en ligne. Ce dossier doit comporter :
   - Un CV et une lettre de motivation en français, adressée au responsable de votre département d'études et au responsable filière (le cas échéant).
   - Votre projet de mobilité, complété (30 ECTS par semestre) et signé par vos enseignants référents (département et filière, le cas échéant).
   - Votre certificat de scolarité de l’année en cours.
   - Vos relevés de notes obtenus depuis votre arrivée à l'Inalco.

Deux campagnes de candidature sont organisées chaque année :
- **Campagne principale** (octobre - février) pour des départs prévus l’année suivante.
- **Campagne complémentaire** (septembre) pour des départs au second semestre.

Les réunions d'informations sont systématiquement organisées avant l'ouverture des campagnes de mobilité. Des informations sont communiquées régulièrement par mail, sur les écrans d'affichage et sur le fil d'actualité.

Sources :
- [Mobilités Erasmus+](https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-erasmus.html)

**Sources recuperees :**

- [1] Mobilités Erasmus+ / Comment candidater ? (pages=n/a-n/a, score=0.9103, semantic=0.8923, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-erasmus.html
- [2] Mobilités Erasmus+ / Quel sera le montant de ma bourse Erasmus+ ? (pages=n/a-n/a, score=0.8999, semantic=0.8939, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-erasmus.html
- [3] Mobilités Erasmus+ / Comment candidater ? (pages=n/a-n/a, score=0.8987, semantic=0.8807, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-erasmus.html
- [4] Mobilités Erasmus+ / Mobilités Erasmus+ (pages=n/a-n/a, score=0.8961, semantic=0.8901, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-erasmus.html
- [5] Mobilités hors Erasmus+ / Déroulement de la candidature auprès de l'université partenaire (pages=n/a-n/a, score=0.8954, semantic=0.8774, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-hors-erasmus.html

**Faits de référence (non transmis au modèle) :**

- Le candidat doit consulter la charte Erasmus+ et la liste des partenariats
- Il doit discuter de son projet avec le responsable des relations internationales de son département et les responsables pédagogiques concernés
- Le dossier est déposé au moyen d'un formulaire en ligne
- Il comprend notamment un CV, une lettre de motivation, un projet de mobilité de 30 ECTS par semestre, un certificat de scolarité et les relevés de notes
- Une campagne principale et une campagne complémentaire sont organisées selon les calendriers annoncés

## q084. Quelles possibilités de mobilité hors Erasmus+ sont proposées ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
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

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `4615 caractères`

**Reponse :**

Pour trouver un stage et faire établir une convention de stage à l'Inalco, suivez ces étapes :

1. **Vérifiez les critères de votre cursus** : Assurez-vous que votre formation ouvre droit à une convention de stage. Le cursus doit représenter un volume horaire totalisant au minimum 200 heures de cours sur l’année. Consultez la brochure de votre formation ou contactez votre secrétariat pédagogique.

2. **Recherchez des offres de stages** :
   - Vous pouvez consulter le classeur des offres de stages, CDD, CDI, disponible dans le hall du 2e étage au point d’accueil et d’information du SIO-IP.
   - Vous pouvez également utiliser la plateforme Jobteaser, à venir.

3. **Constituez votre dossier de demande de convention de stage** :
   - La convention de stage doit être bien remplie et comporter une signature de l’ensemble des parties (à l’exception de celle de la Direction Générale des Services).
   - La signature de l’étudiante ou de l'étudiant.
   - La signature et/ou le cachet de l’organisme d’accueil.
   - La signature de la tutrice ou du tuteur de stage.
   - La signature d’une enseignante ou d'un enseignant.

4. **Déposez votre dossier** : Vous devez impérativement déposer votre dossier au maximum quatre jours ouvrés avant le début de votre stage pour recevoir votre convention signée en temps et en heure.

5. **Fiche d'évaluation de stage** : À l'issue de votre stage, n'oubliez pas de faire compléter une fiche d'évaluation de stage et de la transmettre au secrétariat pédagogique de votre filière ou département d'études.

Sources :
- [Conventions de stage](https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html)

**Sources recuperees :**

- [1] Conventions de stage / **DÉLAIS** (pages=n/a-n/a, score=0.8689, semantic=0.8689, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html
- [2] Conventions de stage / Où puis-je trouver des offres de stages à l’Inalco ? (pages=n/a-n/a, score=0.8689, semantic=0.8689, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html
- [3] Conventions de stage / **CRITÈRES ET DÉMARCHES** (pages=n/a-n/a, score=0.8659, semantic=0.8659, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html
- [4] Conventions de stage / CRITÈRES ET DÉMARCHES (pages=n/a-n/a, score=0.8622, semantic=0.8622, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html
- [5] Conventions de stage / **CRITÈRES ET DÉMARCHES** (pages=n/a-n/a, score=0.8609, semantic=0.8609, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/stages-et-alternance/convention-de-stage.html

**Faits de référence (non transmis au modèle) :**

- Les offres de stage sont consultables auprès du SIO-IP et sur la plateforme JobTeaser
- Le cursus doit comporter au moins 200 heures de cours dans l'année pour ouvrir droit à une convention de stage
- Certains diplômes d'établissement et les Passeports Langues O' ne donnent pas droit à une convention
- Le dossier de convention doit être complet et signé par les parties requises
- Le dossier doit être déposé au plus tard quatre jours ouvrés avant le début du stage

## q086. Comment bénéficier d'un accompagnement pour l'orientation et l'insertion professionnelle ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5678 caractères`

**Reponse :**

Pour bénéficier d'un accompagnement pour l'orientation et l'insertion professionnelle à l'Inalco, vous pouvez suivre plusieurs démarches :

1. **Fiche de Réorientation** : La fiche de réorientation est facultative mais peut être obligatoire pour certaines universités. Elle se délivre uniquement sur entretien avec la PsyEN ou l'équipe du SIO-IP. Vous pouvez prendre rendez-vous via Jobteaser : [rubrique "Prendre RDV avec un conseiller"](https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/prendre-rdv-avec-un-conseiller.html).

2. **JobTeaser** : Le JobTeaser de l'Inalco propose des offres de stage, CDD, CDI, job étudiant, vacation ou service civique. Vous pouvez également y prendre rendez-vous le jeudi avec la psychologue de l'éducation nationale (PsyEN) ou le mardi avec l'équipe du SIO-IP. Vous y trouverez également des ressources documentaires et des événements liés à l'insertion professionnelle.

3. **Rendez-vous avec un Conseiller** : Des rendez-vous individuels sont organisés le jeudi avec la psychologue de l’éducation nationale (PsyEN) et le mardi avec l’équipe du SIO-IP. Ces rendez-vous peuvent vous aider à construire votre parcours, faire le point sur votre poursuite d’études, vous accompagner dans votre réorientation, élargir vos perspectives d’avenir, vous remotiver et préparer votre insertion professionnelle.

4. **SIO-IP** : Le SIO-IP est situé au 2e étage du Pôle des langues et civilisations (PLC) et propose des permanences toute la semaine dans le hall d'accueil du 2e étage. Il est organisé autour de trois grandes missions : information et orientation, accompagnement à l’insertion professionnelle, gestion des conventions de stage, et diffusion-réception des offres de stage et d’emploi.

Sources :
- [Se réorienter](https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/information-et-orientation/se-reorienter.html)
- [Inalco Career Center Job Teaser](https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/construire-son

**Sources recuperees :**

- [1] Se réorienter / **LA FICHE DE REORIENTATION** (pages=n/a-n/a, score=0.8543, semantic=0.8543, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/information-et-orientation/se-reorienter.html
- [2] Inalco Career Center Job Teaser / **CE QUE VOUS Y TROUVEREZ** (pages=n/a-n/a, score=0.8536, semantic=0.8536, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/construire-son-projet-pro/inalco-career-center-job-teaser.html
- [3] Prendre RDV avec un conseiller / PRENDRE RENDEZ-VOUS (pages=n/a-n/a, score=0.8525, semantic=0.8525, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/prendre-rdv-avec-un-conseiller.html
- [4] Prendre RDV avec un conseiller / LE SERVICE DU SIO-IP (pages=n/a-n/a, score=0.8494, semantic=0.8494, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/prendre-rdv-avec-un-conseiller.html
- [5] Construire son projet pro / Construire son projet pro (pages=n/a-n/a, score=0.8479, semantic=0.8479, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/insertion-professionnelle/construire-son-projet-pro.html

**Faits de référence (non transmis au modèle) :**

- Le SIO-IP accompagne les étudiants dans l'orientation et l'insertion professionnelle
- Des rendez-vous individuels sont proposés avec la PsyEN et l'équipe du SIO-IP
- Le Career Center JobTeaser diffuse des offres de stage, d'emploi, de job étudiant, de vacation et de service civique
- Le SIO-IP gère également les conventions de stage et diffuse des offres
- Le service est situé au deuxième étage du Pôle des langues et civilisations

## q088. Comment payer mes repas avec Izly et que faire si mon compte ne fonctionne pas ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5922 caractères`

**Reponse :**

Pour payer vos repas avec Izly, vous devez utiliser votre carte étudiante multiservice. Cette carte contient un compte en ligne Izly, que vous pouvez recharger directement depuis votre compte bancaire via le site izly.fr ou l'application IZLY disponible sur les principaux stores de téléchargement.

Si votre compte ne fonctionne pas, vérifiez l'adresse de courriel que vous avez donnée au service de la scolarité ainsi que vos SPAM. Vous pouvez également réinitialiser votre carte en début d'année universitaire sur les bornes prévues à cet effet au premier étage de l'Inalco.

Sources :
- [Se nourrir](https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html)
- [Services et ressources numériques](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html)

**Sources recuperees :**

- [1] Se nourrir / Comment payer ? (pages=n/a-n/a, score=0.8992, semantic=0.8812, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html
- [2] Services et ressources numériques / Scolarité (pages=n/a-n/a, score=0.8737, semantic=0.8677, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [3] Services et ressources numériques / Carte multi-services étudiante (pages=n/a-n/a, score=0.8569, semantic=0.8509, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [4] Se nourrir / Restaurant Universitaire de la Halle aux farines (pages=n/a-n/a, score=0.8568, semantic=0.8388, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/sante-sport-et-bien-etre/se-nourrir.html
- [5] Services et ressources numériques / Scolarité (pages=n/a-n/a, score=0.8541, semantic=0.8481, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html

## q089. Comment demander un logement en résidence universitaire auprès du Crous ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `3940 caractères`

**Reponse :**

Pour demander un logement en résidence universitaire auprès du Crous, vous devez suivre les étapes suivantes :

1. **Vérifiez votre éligibilité** : Les logements du Crous de Paris sont réservés en priorité aux personnes étudiantes boursières selon des critères sociaux.

2. **Déposez votre candidature** : Consultez le site du Crous de Paris pour découvrir comment effectuer une demande de logement dans une résidence du Crous. Vous pouvez également contacter le Crous par téléphone au 09 72 59 65 65 pour obtenir des informations supplémentaires.

3. **Date limite de dépôt** : La demande de DSE (Dossier Social Étudiant) doit être faite sur le site [messervices.étudiant.gouv.fr](https://messervices.étudiant.gouv.fr) avant le 31 mai 2026 pour permettre un traitement du dossier dans les meilleurs délais et bénéficier de la mise en paiement de la bourse dès la rentrée.

Sources :
- [Se loger](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html)
- [Lancement de la campagne de bourse et de logement étudiant 2026-2027](https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html)

**Sources recuperees :**

- [1] Se loger / Comment obtenir un logement en résidence universitaire ? (pages=n/a-n/a, score=0.9223, semantic=0.9043, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html
- [2] Se loger / A qui sont réservés les logements en résidence universitaire parisienne ? (pages=n/a-n/a, score=0.9066, semantic=0.8886, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html
- [3] Se loger / Comment contacter le CROUS ? (pages=n/a-n/a, score=0.888, semantic=0.87, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html
- [4] Lancement de la campagne de bourse et de logement étudiant 2026-2027 / Où et quand faire sa demande ? (pages=n/a-n/a, score=0.8792, semantic=0.8612, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html
- [5] Se loger / Informations et documentations sur les logements (pages=n/a-n/a, score=0.8716, semantic=0.8536, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-loger.html

**Faits de référence (non transmis au modèle) :**

- La demande de logement en résidence universitaire passe par le Crous
- Les résidences du Crous sont attribuées en priorité aux étudiants boursiers selon des critères sociaux
- Le nombre de places est limité et la candidature doit être déposée dès l'ouverture de la procédure
- Le numéro d'information Crous indiqué est le 09 72 59 65 65

## q090. Comment accéder à distance aux ressources numériques de la bibliothèque ou de la médiathèque ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5360 caractères`

**Reponse :**

Pour accéder à distance aux ressources numériques de la bibliothèque ou de la médiathèque de l'Inalco, vous pouvez utiliser la plateforme Moodle et la plateforme VàD de l'Inalco.

1. **Plateforme Moodle** : L'Inalco vous accompagne dans la réussite de vos études avec l'accès à de nombreux outils pédagogiques à distance via la plateforme Moodle. N'oubliez pas d'activer votre compte numérique.

2. **Plateforme VàD de l'Inalco** : L'Inalco propose une plateforme VàD (Vidéo à la demande) consacrée à ses collections en ligne : fictions, films d'animation, documentaires, productions Inalco. Pour l'inscription, elle s'effectue sur place (en salle 6.02) avec votre carte d'étudiant ou professionnelle, en cours de validité.

Sources :
- [Services et ressources numériques](https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html)

**Sources recuperees :**

- [1] Services et ressources numériques / Services et ressources numériques (pages=n/a-n/a, score=0.8465, semantic=0.8465, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [2] Services et ressources numériques / Outils collaboratifs et services proposés (pages=n/a-n/a, score=0.8414, semantic=0.8414, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [3] Services et ressources numériques / Wi-Fi (pages=n/a-n/a, score=0.8393, semantic=0.8393, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [4] Services et ressources numériques / Fonds documentaire (pages=n/a-n/a, score=0.8378, semantic=0.8378, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [5] Services et ressources numériques / Outils collaboratifs et services proposés (pages=n/a-n/a, score=0.8373, semantic=0.8373, dans_contexte=non)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html

## q092. Comment rejoindre une association étudiante de l'Inalco ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `5222 caractères`

**Reponse :**

Pour rejoindre une association étudiante de l'Inalco, vous pouvez suivre les étapes suivantes :

1. **Visitez les pages des associations** : Consultez la page dédiée aux associations étudiantes de l'Inalco pour découvrir les différentes associations disponibles. Vous pouvez accéder à cette page via le lien suivant : [Associations étudiantes](https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations.html).

2. **Contactez les associations** : Une fois que vous avez identifié l'association qui vous intéresse, n'hésitez pas à les contacter directement via leurs pages respectives pour obtenir des informations sur les modalités d'adhésion et les activités proposées.

3. **Participez aux événements de rentrée** : Lors des journées de rentrée organisées du 14 au 18 septembre 2026, vous pourrez rencontrer les responsables des associations et obtenir des informations supplémentaires. Ces journées sont également l'occasion de découvrir votre nouvel environnement d'études et de vous familiariser avec le fonctionnement de l'université.

Sources :
- [Associations étudiantes](https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations.html)
- [Faire sa rentrée à l'Inalco](https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juillet-2026/faire-sa-rentree.html)

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

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4794 caractères`

**Reponse :**

Pour créer et faire reconnaître une nouvelle association étudiante à l'Inalco, suivez ces étapes :

1. **Rédiger des statuts** : Les membres fondateurs doivent rédiger des statuts détaillant les objectifs, la structure, les règles de fonctionnement et les modalités de gestion de l'association.

2. **Se réunir en assemblée constitutive** : Les membres fondateurs se réunissent en Assemblée constitutive pour adopter le projet de statuts et désigner les membres du bureau. Les décisions prises lors de cette réunion sont consignées dans un procès-verbal (PV) de l'assemblée constitutive.

3. **Déposer les statuts** : Une fois les statuts rédigés et adoptés, ils doivent être déposés auprès de la Direction des études et de la vie étudiante (DEVE) de l'Inalco.

4. **Obtenir la reconnaissance** : Après dépôt des statuts, l'association doit être reconnue par l'Inalco. Cette reconnaissance permet à l'association de bénéficier d'aides financières et de participer pleinement à la vie étudiante.

Pour plus de détails, consultez la page officielle sur la création et la gestion des associations étudiantes à l'Inalco : [Créer et gérer une association](https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/creer-et-gerer-une-association.html).

Sources :
- [Association étudiante : mode d'emploi](https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/creer-et-gerer-une-association/association-etudiante-mode-d-emploi.html)
- [Créer et gérer une association](https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/creer-et-gerer-une-association.html)

**Sources recuperees :**

- [1] Association étudiante : mode d'emploi / **I/Rédiger des statuts** (pages=n/a-n/a, score=0.8578, semantic=0.8578, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/creer-et-gerer-une-association/association-etudiante-mode-d-emploi.html
- [2] Créer et gérer une association / Créer et gérer une association (pages=n/a-n/a, score=0.8571, semantic=0.8571, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/creer-et-gerer-une-association.html
- [3] Association étudiante : mode d'emploi / Association étudiante : mode d'emploi (pages=n/a-n/a, score=0.8532, semantic=0.8532, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/creer-et-gerer-une-association/association-etudiante-mode-d-emploi.html
- [4] Association étudiante : mode d'emploi / Aides financières (pages=n/a-n/a, score=0.8526, semantic=0.8526, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations/creer-et-gerer-une-association/association-etudiante-mode-d-emploi.html
- [5] Associations étudiantes / Associations étudiantes (pages=n/a-n/a, score=0.8515, semantic=0.8515, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/associations.html

**Faits de référence (non transmis au modèle) :**

- Une association étudiante peut demander à être reconnue par l'Inalco
- Les membres fondateurs doivent notamment préparer des statuts et se réunir en assemblée constitutive
- L'assemblée constitutive adopte les statuts et désigne les membres du bureau
- Les décisions de l'assemblée constitutive sont consignées dans un procès-verbal

## q094. Comment faire reconnaître et valoriser mon engagement étudiant dans mon cursus ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `answer`  
**Abstention produite :** `False`
**Clarification produite :** `False`  
**Sources dans le contexte :** `5`  
**Taille du contexte :** `4628 caractères`

**Reponse :**

Pour faire reconnaître et valoriser votre engagement étudiant dans votre cursus à l'Inalco, vous pouvez suivre les étapes suivantes :

1. **Qui est concerné ?** : Vous pouvez faire reconnaître et valoriser votre engagement si vous êtes inscrite ou inscrit en Licence (L1, L2, L3), en Master 1, ou en diplôme d'établissement (à l’exclusion des diplômes d’établissement à distance et des diplômes intensifs).

2. **Comment faire valider votre action ?** : En fonction de votre formation, la scolarité saisira sur votre relevé soit la validation de l’EC « Engagement étudiant » affecté de trois crédits ECTS, soit la proposition de bonification de la CV2E qui sera intégrée à votre moyenne annuelle générale.

3. **Comment votre engagement est-il valorisé ?** :
   - **Pour les étudiantes et étudiants inscrits en Licence ou en diplôme d’établissement dans un niveau comportant une UE libre**, la reconnaissance pédagogique de l’engagement étudiant s’inscrit dans le cadre de cette UE Libre sous la forme d’un EC « Engagement étudiant » affecté de 3 ECTS. L’EC est validé, sans note, au second semestre de l’année universitaire.
   - **Pour les étudiantes et étudiants inscrits en Licence ou en diplôme d’établissement dans un niveau ne comportant pas d’UE libre, ainsi que pour les étudiants inscrits en Master 1**, l’engagement étudiant est valorisé par l’obtention d’une bonification accordée par la Commission de validation de l’engagement étudiant (CV2E) que le jury d’admission de chaque formation peut intégrer à la moyenne annuelle générale de l’étudiant, pour un maximum de 0.5 points /20. La bonification est accordée...

4. **Quelles sont les activités éligibles ?** : L’engagement doit être volontaire, bénévole et laïque. Il doit servir un intérêt général et véhiculer des valeurs de solidarité, d’entraide et de citoyenneté. Il doit représenter un minimum de 30 heures d’activité durant l’année universitaire au cours de laquelle la valorisation est demandée.

Sources :
- [Valorisation de l'engagement](https://portail-etudiant.inalco.fr/fr/vie-de-campus/s-engager/valor

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

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5420 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Services et ressources numériques / Scolarité (pages=n/a-n/a, score=0.8462, semantic=0.8402, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/services-et-ressources-numeriques.html
- [2] Lancement de la campagne de bourse et de logement étudiant 2026-2027 / Quels sont les avantages d'être boursier ou boursière ? (pages=n/a-n/a, score=0.8434, semantic=0.8254, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/mars-2026/dossier-social-etudiant-26-27.html
- [3] Mobilités hors Erasmus+ / Comment préparer une mobilité internationale hors Europe ? (pages=n/a-n/a, score=0.8428, semantic=0.8368, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-hors-erasmus.html
- [4] Mobilités Erasmus+ / Mobilités Erasmus+ (pages=n/a-n/a, score=0.8421, semantic=0.8361, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/international/etudier-a-l-etranger/mobilites-erasmus.html
- [5] Droits de scolarité : tarifs, exonération, annulation, remboursement / Autres exonérations pouvant être accordées par le Président (pages=n/a-n/a, score=0.8418, semantic=0.8238, dans_contexte=non)  https://www.inalco.fr/droits-de-scolarite-tarifs-exoneration-annulation-remboursement

## q098. Où se trouvent les fontaines ou distributeurs d'eau dans les bâtiments de l'Inalco ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5223 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Schéma Directeur DD&RSE 2025-2030 / Page 21 - Annexe 1. La Convention Environnementale (pages=21-21, score=0.8385, semantic=0.8205, dans_contexte=oui)  https://www.inalco.fr/sites/default/files/2025-06/Sch%C3%A9ma%20Directeur%20DD%26RSE%202025.pdf
- [2] Schéma Directeur DD&RSE 2025-2030 / Page 27 - REMERCIEMENTS (pages=27-27, score=0.8322, semantic=0.8142, dans_contexte=oui)  https://www.inalco.fr/sites/default/files/2025-06/Sch%C3%A9ma%20Directeur%20DD%26RSE%202025.pdf
- [3] Vigilance canicule / 1 - Buvez régulièrement de l’eau (pages=n/a-n/a, score=0.8281, semantic=0.8281, dans_contexte=oui)  https://portail-etudiant.inalco.fr/fr/actualites/actualites-2026/juin-2026/vigilance-canicule.html
- [4] Schéma Directeur DD&RSE 2025-2030 / Page 20 - Annexe 1. La Convention Environnementale (pages=20-20, score=0.8278, semantic=0.8098, dans_contexte=oui)  https://www.inalco.fr/sites/default/files/2025-06/Sch%C3%A9ma%20Directeur%20DD%26RSE%202025.pdf
- [5] Schéma Directeur Développement Durable et Responsabilité Sociale et Environnementale (SD DD&RSE) / Schéma Directeur Développement Durable et Responsabilité Sociale et Environnementale (SD DD&RSE) (pages=n/a-n/a, score=0.8277, semantic=0.8097, dans_contexte=non)  https://www.inalco.fr/ddrse

## q100. Quand aura lieu la prochaine réunion du Vivier environnemental ?

**Methode :** `m2_rag_rerank`  
**Experience :** `m2_rag_rerank_test_frozen_v1`  
**Mode de recuperation :** `heuristic_rerank`  
**Mode de prompt :** `standard`
**Split :** `test`  
**Comportement attendu :** `abstain`  
**Abstention produite :** `True`
**Clarification produite :** `False`  
**Sources dans le contexte :** `4`  
**Taille du contexte :** `5986 caractères`

**Reponse :**

Je n'ai pas trouvé cette information dans la documentation collectée.

**Sources recuperees :**

- [1] Schéma Directeur DD&RSE 2025-2030 / Page 7 - IV. Le plan d’actions et sa méthode (pages=7-7, score=0.8372, semantic=0.8192, dans_contexte=oui)  https://www.inalco.fr/sites/default/files/2025-06/Sch%C3%A9ma%20Directeur%20DD%26RSE%202025.pdf
- [2] Schéma Directeur DD&RSE 2025-2030 / Page 4 - I. Les enjeux environnementaux et sociaux (pages=4-4, score=0.8354, semantic=0.8174, dans_contexte=oui)  https://www.inalco.fr/sites/default/files/2025-06/Sch%C3%A9ma%20Directeur%20DD%26RSE%202025.pdf
- [3] Schéma Directeur DD&RSE 2025-2030 / Page 21 - Annexe 1. La Convention Environnementale (pages=21-21, score=0.8348, semantic=0.8168, dans_contexte=oui)  https://www.inalco.fr/sites/default/files/2025-06/Sch%C3%A9ma%20Directeur%20DD%26RSE%202025.pdf
- [4] Schéma Directeur DD&RSE 2025-2030 / Page 20 - Annexe 1. La Convention Environnementale (pages=20-20, score=0.8341, semantic=0.8161, dans_contexte=oui)  https://www.inalco.fr/sites/default/files/2025-06/Sch%C3%A9ma%20Directeur%20DD%26RSE%202025.pdf
- [5] Schéma Directeur DD&RSE 2025-2030 / Page 4 - I. Les enjeux environnementaux et sociaux (pages=4-4, score=0.8331, semantic=0.8151, dans_contexte=non)  https://www.inalco.fr/sites/default/files/2025-06/Sch%C3%A9ma%20Directeur%20DD%26RSE%202025.pdf

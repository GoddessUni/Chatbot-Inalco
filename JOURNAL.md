# Journal du projet
## Semaine 1 (01/06/2026-07/06/2026)
Des recherches antérieures ont montré que les performances insuffisantes des chatbots ne sont pas uniquement dues au modèle choisi ; un problème important réside dans le manque de sources de connaissances appropriées et de contrôle sur les réponses.

Par exemple, le chatbot conçu avec la méthode Prompting-only a généré beaucoup de fausses informations, le surapprentissage à cause du corpus qui a contenu très peu de données, des informations importantes qui ont été coupées dans le processus de segmentation, et le manque de mécanisme de filtration.

Afin d’améliorer les performances du chatbot, je pense que le corpus des données utilisées pour l'entraînement ou pour la construction de la base de connaissances sont très importantes. 

Comme des recherches antérieures ont montré que les chatbots utilisant la méthode de RAG sont plus performants, j'ai d'abord essayé de construire une base de connaissances pour cette méthode. 

Et pour réaliser ces fonctionnalités, j'ai conçu un pipeline qui comprend le crawling, l’extraction des données, le nettoyage et la normalisation du texte, la segmentation de connaissances consultables et l'augmentation des données.

Dans le premier prototype du pipeline, j’ai utilisé principalement les techniques classiques, avec Trafilatura dans le script d’extraction pour obtenir les textes propres.

J’utilise aussi l’expression régulière pour enlevé les espaces non-ASCII ou doublés, et les lignes vides. Et puis j’ai effectué la segmentation par les nombres de caractères pour que chaque segment contienne idéalement un seul thème. 

Afin de diminuer l’hallucination au premier étape, j’ai ajouté les niveaux de risque pour les mots-clés. L’inscription, l’admission, les droits de scolarités, le calendrier, les examens, etc. sont très importants et le chatbot doit générer les réponses qui correspondent exactement aux ressources sur le site de l’université. Je les ai catégorisés dans le script de métadonnées par des mots-clés extraits.

Comme le site de l’université contient tellement d’informations utiles pour les étudiants, j’ai stocké les données dans un fichier Jsonl au lieu de Json pour faciliter le traitement ultérieur.

Après avoir testé ces scripts, j'ai constaté que certaines pages Web extraites contenaient le même contenu, que certaines balises de lien HTML étaient toujours présentes et 160/307 des chunks étaient classés comme générals, ce qui affectera le traitement ultérieur.

Pour améliorer ses performances, j'ai ajouté le plan du site comme l’entrée supplémentaire dans la configuration, et les connaissances du site sont maintenant classées selon leur actualité.

J’ai corrigé aussi la fonction de crawling et enregistré les pages qui ne sont pas récupérées. Et j’ai ajouté les scripts de filtrage et de déduplication.

Comme le contenu d'une page web n'est pas toujours valide, la simple vérification de la correspondance des données extraites avec la page ne suffit pas. J'ai donc modifié la fonction de vérification et ajouté un indicateur de validation humaine. Si nécessaire, le chatbot ne pourra répondre qu'aux informations vérifiées manuellement.

Une fois la base de connaissances créée, le script d'audit examinera chaque segment.

La version v0.2 est plus performante, mais certains problèmes persistent : mon script ne reconnaît pas les niveaux de titres comme h1, h2, etc., ne sait pas si des paragraphes sont du même sujet et peut diviser ou fusionner incorrectement.

Ma prochaine étape consiste à extraire les page web par titre et sous-titre, à générer des segments, et à diviser des paragraphes très longs en phrases. J'utiliserai ensuite le titre de la page, les titres des segments et le corps du texte pour évaluer le niveau de risque et ainsi améliorer la qualité du texte.

## Semaine 2 (08/06/2026-14/06/2026)
Avant la segmentation sémantique, les limites des segments générés par différentes pages ne sont pas les même, et les segments ne sont pas identiques. 

J'ai donc décidé de modifier la stratégie de déduplication, de marquer les pages dupliquées, de fusionner les segments dupliqués et de conserver toutes les URL sources.

Et les résultats de cette version est le suivant:

Discovered URLs: 206
Extracted pages: 163
Unique chunks: 429
Failures: 43
Duplicate pages marked: 15
Duplicate chunks removed: 49

Dans cette version, la taille maximale des segments est de 1496 caractères, ce qui ne dépasse pas la limite. Il n’y a pas de JavaScript, de cookies ni de substitution. Et les pages principales, telles que l'emploi du temps, les frais de scolarité, et le VSS, sont bien segmentées.

Par exemple, les droits de scolarité sont séparés comme "Droits de scolarité", "Exonération", et "Annulation et remboursement d'inscription"

Cependant, certains problèmes existe encore, tels que: 

Le script a trouvé une "Direction d'études" incorrecte, la page contient toujours des instructions de modification du site web.

Il y a des segments invalides et extrêmement courts comme "-", "En cours de construction", etc.

La section Services et Ressources ne comporte que quatre sous-sections, la majeure partie du contenu relevant des "Outils collaboratifs et services proposés".

La classification par sujet reste peu fiable ; le système identifie par erreur les Services numériques comme étant liés à la bibliothèque.

J'ai donc décidé de modifier le mécanisme de pipeline.

- Supprimer les segments qui contiennent seulement des symboles tel que "-".
- Exclure "En courses de construction".
- Exclure les pages d'erreur détectées comme "direction d’études".
- Supprimer les espaces vides et le Markdown invalide.
- Fusionner le contenu dupliqué et conserver la source.
- Marquer les segments trop courts.
- Catégorisation des sujets à l’aide d'URL.
- Détecter l'adresse e-mail, le numéro de téléphone, la date et le montant. 
- Détecter les titres ou sections manquants. 
- Afficher la liste des éléments en attente de vérification.

J'ai ajouté quality.py pour résoudre les problèmes ci-dessus et améliorer la qualité des données. Et j’ai classé les éléments nécessitant une vérification manuelle par ordre d'importance, afin de pouvoir la mettre en place ultérieurement. On utilise pas cette partie pour le moment.

Après le test, le nouveau résultat est :

Discovered URLs: 205
Extracted pages: 162
Unique chunks before quality filtering: 428
Indexable chunks: 424
Failures: 43
Duplicate pages marked: 15
Duplicate chunks removed: 49
Rejected pages: 0
Rejected chunks: 4
Review queue: 303

Et mon script d'audit évalue automatiquement les résultats extraits :

Pages: 162
Chunks: 424
Unique page URLs: 162
Unique chunk IDs: 424
Duplicate pages marked: 15
Chunks with multiple sources: 39

Knowledge types: Counter({'stable': 134, 'temporal': 22, 'portal_help': 6})
Themes: Counter({'Général': 126, 'Associations et vie de campus': 67, 'International': 47, 'Inscriptions': 41, 'Santé et bien-être': 35, 'Orientation et insertion': 32, 'Handicap': 22, 'Numérique et outils': 16, 'Bourses et aides': 15, 'Harcèlement et VSS': 7, 'Examens': 6, 'Scolarité': 6, 'Emplois du temps': 4})
Risk levels: Counter({'low': 197, 'high': 145, 'medium': 82})

Missing page titles: 5
Missing chunk titles: 15
Missing section titles: 3
Short chunks (<200 chars): 58
Long chunks (>1800 chars): 0
JavaScript noise: 0
Unverified high-risk chunks: 145
Quality statuses: Counter({'review': 265, 'ready': 159})
Quality flags: Counter({'generic_theme': 126, 'contains_date': 87, 'contains_email': 60, 'short_chunk': 58, 'multiple_sources': 39, 'temporal_content': 38, 'missing_title': 15, 'contains_amount': 14, 'contains_phone': 6, 'missing_section_title': 3, 'construction_notice': 1})
Review priorities: Counter({'P2': 158, 'P1': 85, 'P0': 60})

On constate que "Général" représente près d’un tiers du thèmes, et le poids de la recherche pour les 58 segments courts a été réduit.

Une vérification humaine peut être effectuée après confirmation du fonctionnement du système. Lors de la phase de test la semaine prochaine, je vais les considérer comme valides et constituer un jeu de données à partir de questions et réponses réelles afin de tester si ces segments marche bien pour le RAG.

## Semaine 3 (15/06/2026-21/06/2026)
Comme je l'ai mentionné dans ma présentation, les informations qui intéressent les étudiants ne sont pas uniquement disponibles sur Portail ; des sites web comme Inalco.fr et Moodle contiennent aussi des contenus importants. Si on donne les étiquettes aux sources d'information dans la base de connaissances, RAG peut récupérer des données depuis plusieurs sites web. 

Afin d'éviter toute confusion, j'ai ajouté des métadonnées à chaque segment. Cela permet à RAG de rechercher simultanément sur plusieurs sites lors de la récupération des données, et de savoir d'où proviennent les informations quand il répond aux questions.

Je vais concevoir le processus comme cela : premièrement, le système recherche tous les segments officiels, puis fusionner les résultats (tels que le portail et inalco.fr), les trie par l’importance de la source, supprime le contenu dupliqué et similaire, et enfin sélectionne les sources les plus pertinentes (top-k) pour générer des réponses.

Par exemple, lorsqu'un étudiant consulte les frais de scolarité, le RAG doit rechercher la page « droits de scolarité » sur inalco.fr et « inscription » sur portal-etudiant. Si les deux résultats sont les même, ils peuvent être fusionnés. Sinon l'utilisateur doit être invité à consulter la page officielle la plus récente.

La priorité des stratégies de requête peut varier selon le type de question. Par exemple, les questions sur la vie étudiante pourraient présenter principalement sur portail, tandis que les questions sur la formation et l'administration pourraient principalement sur inalco.fr. Cependant, lors de la conception du code, j'ai constaté que cela mène à une logique de requête complexe et réduirait la fiabilité.

J'ai modifié le crawler pour qu'il parcoure plusieurs URL simultanément et j'ai ajouté des étiquettes de domaine pour les traiter séparément.

Mais j'ai découvert que  le processus de scraper l'intégralité du site inalco.fr mène à un résultat chaotique, j'ai donc décidé de le compléter avec quelques sujets basés sur les questions clés des étudiants : frais de scolarité, inscription administrative, maître d'admission, candidatures, contacts scolarité, bibliothèque / ressources numériques, handicap, harcèlement / VSS, calendrier universitaire.

J'ai aussi ajouté source_utils.py pour une gestion unifiée des sources. Et j’ai légèrement augmenté le poids d'inalco.fr pour des informations administratives.

Cette fois-ci, le pipeline retourne le résultat suivant : 

Pages: 252 
Chunks: 706 
Unique page URLs: 252 
Unique chunk IDs: 706 
Duplicate pages marked: 53 
Chunks with multiple sources: 211 

Source domains: Counter({'portail-etudiant.inalco.fr': 162, 'www.inalco.fr': 90}) 
Source scopes: Counter({'official_student_portal': 162, 'official_institutional_site': 90}) 

Knowledge types: Counter({'stable': 199, 'temporal': 47, 'portal_help': 6}) 
Themes: Counter({'Général': 245, 'Inscriptions': 92, 'International': 91, 'Associations et vie de campus': 73, 'Santé et bien-être': 51, 'Orientation et insertion': 49, 'Bourses et aides': 28, 'Handicap': 23, 'Numérique et outils': 18, 'Examens': 14, 'Emplois du temps': 8, 'Harcèlement et VSS': 7, 'Scolarité': 6, 'Bibliothèque': 1})
Risk levels: Counter({'low': 365, 'high': 239, 'medium': 102}) 

Missing page titles: 5 
Missing chunk titles: 14 
Missing section titles: 2 
Short chunks (<200 chars): 81 
Long chunks (>1800 chars): 0 
JavaScript noise: 0 
Unverified high-risk chunks: 239 
Quality statuses: Counter({'review': 528, 'ready': 178}) 
Quality flags: Counter({'generic_theme': 245, 'multiple_sources': 211, 'contains_date': 180, 'temporal_content': 129, 'short_chunk': 81, 'contains_email': 61, 'contains_amount': 17, 'missing_title': 14, 'contains_phone': 10, 'missing_section_title': 2, 'construction_notice': 1}) 
Review priorities: Counter({'P2': 346, 'P1': 150, 'P0': 89}) 

Après avoir vérifier les segments, j’ai constaté que cette version récupère correctement les informations d'inalco.fr, mais qu'elle contenait également de nombreuses données peu important avec le service aux étudiants, ce qui risque de nuire à la précision des réponses générées par RAG.

Par conséquent, j'ajouterai des restrictions supplémentaires afin que les informations collectées correspondent davantage aux questions essentielles des étudiants.

## Semaine 4 (22/06/2026-28/06/2026)
Comme mon script récupérait du contenu non pertinent et sans importance, j'ai décidé d'utiliser un mécanisme de liste blanche pour limiter la portée de la collecte : pour inalco.fr, je ne récupérerais que les URL de départ, sans explorer les liens suivants. Par conséquent, j'ai ajouté une fonction pour vérifier les paths exacts.

Le site inalco.fr/formations/... compte un grand nombre de pages, dont une grande partie présente des descriptions de programmes spécialisés peu adaptés à un chatbot de services aux étudiants généraliste ; j'ai donc choisi de ne conserver que les pages de programmes pertinentes au regard des objectifs du chatbot.

Le résultat indique que le contenu utilisé pour la base de connaissances principale est strictement limité : 

Knowledge types: Counter({'stable': 139, 'temporal': 24, 'portal_help': 6}) 
Themes: Counter({'Général': 129, 'Inscriptions': 73, 'Associations et vie de campus': 67, 'International': 47, 'Santé et bien-être': 35, 'Orientation et insertion': 32, 'Bourses et aides': 27, 'Handicap': 23, 'Numérique et outils': 16, 'Examens': 15, 'Harcèlement et VSS': 7, 'Scolarité': 6, 'Emplois du temps': 4}) 
Risk levels: Counter({'high': 199, 'low': 199, 'medium': 83}) 

Missing page titles: 5 
Missing chunk titles: 15 
Missing section titles: 3 
Short chunks (<200 chars): 67 
Long chunks (>1800 chars): 0 
JavaScript noise: 0 
Unverified high-risk chunks: 199 
Quality statuses: Counter({'review': 295, 'ready': 186}) 
Quality flags: Counter({'generic_theme': 129, 'contains_date': 106, 'short_chunk': 67, 'contains_email': 60, 'multiple_sources': 45, 'temporal_content': 44, 'missing_title': 15, 'contains_amount': 14, 'contains_phone': 7, 'missing_section_title': 3, 'construction_notice': 1}) 
Review priorities: Counter({'P2': 161, 'P1': 120, 'P0': 79}) 

Le script applique des étiquettes de partition, mais ne génère pas encore concrètement plusieurs fichiers de partition ou plusieurs index. Afin d'améliorer la précision des recherches RAG, je tente d'organiser les segments récupérés en plusieurs modules distincts lors de la constitution de la base de connaissances.

Après avoir essayé diverses stratégies de partition, j'ai réparti les segments acquis en quatre catégories : stable, temporal, portal_help et review. Ensuite, j'ai préparé le texte d'embedding pour chaque segment, et j’ai ajouté des éléments tels que les titres, les sujets et les sources afin d'assurer une meilleure correspondance avec les questions des étudiants lors de la phase de recherche.

Et j’ai obtenu les segments avec les partitions différentes:

total_chunks: 481 
main_ready: 186 
stable_ready: 185 
portal_help_ready: 1 
temporal_separate: 44 
review_all: 295 
review_p0: 79 
review_p1: 120 
review_p2_candidate: 161 

J'ai conçu la fonction build_embedding_text pour générer le texte adapté à l’embedding pour chaque segments.

Mon objectif actuel est d'abord d'établir un baseline RAG standard , et je peux donc commencer par utiliser BM25 pour valider les segments récupérés, puis générer des embeddings pour ceux-ci.

## Semaine 5 (29/06/2026-05/07/2026)
Cette semaine, j'ai commencé à concevoir la partie d’embedding. Dans le prototype de chatbot, j'ai ajouté tous les segments au prototype de base de connaissances.

J'ai d'abord essayé d'utiliser un embedding de hashing local pour valider le pipeline. Comme il ne s'agit pas d'un véritable embedding sémantique, il n'a pas pu trouver avec précision le segment correspondant à la question « Quels sont les jours et horaires d’ouverture de l’Inalco ? ». Si la question et les mots de la page Web ne sont pas les mêmes, la priorité de recherche sera plus faible. De plus, le thème de Général est trop vaste et mélangé à de nombreuses pages, ce qui entraîne un ordre instable dans les résultats de recherche.

Cette version prouvant que le pipeline est utilisable, j'ai décidé de  le modifier avec un modèle d’embedding sémantique pour améliorer le problème et d'utiliser un routeur pour faciliter la recherche. Le routeur n’est pas utilisé comme un classifieur bloquant, la recherche s’effectue toujours sur l’ensemble de la base documentaire, et certains thèmes reçoivent un léger bonus lorsque la question contient des indices lexicaux pertinents. Cela permet de conserver la capacité de généralisation de la recherche sémantique et d’améliorer la robustesse sur les questions fréquentes. 

J'ai essayé d'utiliser le modèle multilingue e5-base pour tester localement les performances d’embedding et de recherche. Lors de l'utilisation du nouveau système pour interroger les options de transport pour les deux campus, j'ai rencontré un problème : certaines pages n'étaient pas indexées ou étaient exclues. Après vérification des scripts de scraping, j'ai modifié le fichier config.py pour ajouter des URL spécifiques à la liste blanche. J'ai ensuite modifié le fichier build_e5_index.py pour conserver les métadonnées, ce qui facilite la distinction ultérieure du contenu des pages Web. Et j’ai ajouté les routeurs pour la formation, la scolarité, et le campus.

J'ai constaté que la version actuelle a un problème avec le tri des 5 premiers segments trouvés pour la question “Comment se rendre sur les différents sites de l'Inalco ?". Les mots « se rendre / site / accès » du question provoque le rappel de pages telles que « accéder à Evento / services numériques ». J'ai modifié les scripts retrieve.py et retrieve_e5.py pour augmenter l'importance des mots-clés pertinents, et maintenant le système peut trouver le bon segment.

Maintenant pour cette question, le système retrouve les 5 meilleurs segments suivants: 

[1] score=2.1012
semantic_score: 0.8412
title: La Maison de la recherche
section: Accès
theme: Général
quality: review / P2
source: https://www.inalco.fr/la-maison-de-la-recherche
text: **En métro :** - M1 - station Palais-Royal - Musée du Louvre - M4 - station Saint-Germain-des-Prés - M7 - station Palais-Royal - Musée du Louvre - M12 - station rue du Bac **En bus : **lignes 27, 39, 68, 69, 87, 95 - arrêt Pont du Carrousel - Quai Voltaire **En RER** : RER C - station Musée d’Orsay

[2] score=1.9068
semantic_score: 0.8268
title: Le Pôle des langues et civilisations
section: En bus :
theme: Bibliothèque
quality: review / P2
source: https://www.inalco.fr/le-pole-des-langues-et-civilisations
text: Ligne 83 : arrêt Olympiades Ligne 89 : arrêt bibliothèque François Mitterrand Lignes 27, 62, 64, 132, N31 : arrêt Patay-Tolbiac

[3] score=1.8956
semantic_score: 0.8156
title: Le Pôle des langues et civilisations
section: En métro :
theme: Bibliothèque
quality: review / P2
source: https://www.inalco.fr/le-pole-des-langues-et-civilisations
text: Ligne 14, station bibliothèque François Mitterrand

[4] score=1.892
semantic_score: 0.812
title: Le Pôle des langues et civilisations
section: En RER :
theme: Bibliothèque
quality: review / P2
source: https://www.inalco.fr/le-pole-des-langues-et-civilisations
text: RER C, station bibliothèque François Mitterrand

[5] score=1.6498
semantic_score: 0.8498
title: Se rendre à l'Inalco
section: La Maison de la recherche
theme: Général
quality: review / P2
source: https://portail-etudiant.inalco.fr/fr/vie-de-campus/accueil-et-integration/se-rendre-a-l-inalco.html
text: Le site historique de la Maison de la recherche héberge les unités de recherche, la direction de la recherche et des études doctorales, les publications de l'Inalco mais aussi l'ingénierie administrative et financière de la recherche. *Maison de la recherche (Paris 7e) © Inalco* - **Adresse** Inalco - 2 rue de Lille, 75007 Paris Téléphone (accueil) : +33 (0)1 81 70 10 22 **Horaires d'ouverture :** de 8h30 à 20h00 du lundi au vendredi

Le système peut désormais identifier avec précision les segments correspondant aux certaines questions clés. La prochaine étape consiste à l'adapter aux questions courantes et à concevoir la partie de génération des réponses.

## Semaine 6 (06/07/2026-12/07/2026)
Cette semaine, j’ai avancé sur la partie génération de réponses du prototype de chatbot RAG.

Après la construction de l’index vectoriel avec le modèle d’embedding multilingue, j’ai ajouté une étape de génération fondée sur les passages retrouvés dans la base documentaire. L’objectif est que le chatbot ne réponde pas directement à partir des connaissances générales du modèle, mais uniquement à partir des extraits récupérés par le système RAG.

J’ai donc conçu un script de construction de prompt. Celui-ci assemble la question de l’étudiant, les passages les plus pertinents retrouvés dans l’index, leurs métadonnées, ainsi que les URLs sources. Le prompt contient des consignes explicites, et il demande au modèle de ne pas inventer d’informations absentes du contexte, notamment les dates, horaires, montants, adresses, contacts ou procédures administratives. Il demande aussi de citer les sources utilisées et de signaler lorsque l’information n’est pas présente dans la documentation collectée.

C'est un prompt avec la méthode standard, qui permet au modèle de synthétiser plusieurs extraits lorsque ceux-ci se complètent.

Pour la génération, j’ai commencé à tester une intégration locale avec Ollama. Le prototype appelle un modèle de génération local via l’API d’Ollama après l’étape de récupération des passages. Cela permet de conserver une architecture locale pour les premiers essais : la question est traitée par le pipeline RAG, les extraits sont intégrés au prompt, puis le modèle génère une réponse accompagnée des sources.

J’ai d’abord utilisé le modèle Mistral disponible dans Ollama pour valider la chaîne complète : question d’utilisateur → récupération des segments → construction du prompt → génération locale → réponse avec sources.

Les premiers tests montrent que le système retrouve correctement les pages pertinentes lorsque les informations sont présentes dans la base. Par exemple, pour les questions sur l’accès aux différents sites de l’Inalco, les extraits concernant le Pôle des langues et civilisations et la Maison de la recherche sont bien récupérés. J’ai aussi identifié certains cas où la base documentaire était incomplète. par exemple, la page « Se nourrir » contenait des informations plus détaillées sur les cafétérias et restaurants Crous, mais ces éléments n’étaient pas présents dans l’ancien index. J’ai donc modifié le script d’extraction afin de mieux conserver les contenus structurés, notamment les blocs de cartes ou de listes, qui peuvent contenir des adresses et horaires.

Maintenant ce prototype de chatbot est capable de fournir des réponses en fonction des questions saisies par les utilisateurs. Ma prochaine étape vise à la préparation d’une première grille d’évaluation portant sur la pertinence des sources, la fidélité de la réponse et les cas d’abstention. Et je comparerai les réponses générées avec le prompt standard et le prompt plus strict.

## Semaine 7 (13/07/2026-19/07/2026)
Cette semaine, j’ai commencé à concevoir une procédure de test plus systématique pour le prototype local. Les essais portaient surtout sur quelques questions vérifiées manuellement pour le moment. J’ai donc constitué une première liste de questions probables d’étudiants, couvrant notamment les inscriptions, les bourses, le logement, la restauration, les emplois du temps, les examens, les services numériques et l’accès aux différents sites de l’Inalco.

J’ai aussi préparé un script de traitement par lots qui permet de poser automatiquement ces questions au chatbot et d’enregistrer, pour chaque exemple, la réponse générée, les passages retrouvés, leurs scores et les URLs sources. Cette sortie doit permettre de distinguer les erreurs provenant de la récupération documentaire de celles provenant de la génération. Par exemple, lorsqu’une réponse confond l’inscription administrative et l’inscription pédagogique, il faut d’abord vérifier si le passage administratif est présent dans la base et correctement classé avant d’attribuer l’erreur au modèle de génération.

J’ai défini plusieurs dimensions d’évaluation : la pertinence des passages retrouvés, la fidélité de la réponse aux sources, la complétude, la qualité des citations et la capacité d’abstention lorsque la documentation ne suffit pas. Pour la récupération, des mesures telles que Recall@k, MRR ou nDCG pourront être calculées à partir d’un petit jeu de questions annotées. Pour la génération, une évaluation humaine reste nécessaire, car une simple comparaison lexicale avec une réponse de référence ne mesure pas correctement les hallucinations factuelles.

Les premiers essais avec Mistral avec Ollama ont montré que le prompt limite une partie des inventions, mais qu’il ne peut pas compenser une source absente ou un mauvais classement des passages. L’augmentation de top-k n’améliore pas les réponses : elle peut ajouter des documents peu pertinents et augmenter le bruit dans le contexte. J’ai donc commencé à envisager une comparaison entre plusieurs configurations : modèle seul, RAG simple, RAG avec réordonnancement, RAG avec seuil de confiance et RAG avec abstention.

## Semaine 8 (20/07/2026-26/07/2026)
Cette semaine, j’ai poursuivi l’amélioration du prototype local à partir des erreurs observées pendant les tests. J’ai vérifié plusieurs pages importantes et constaté que certains contenus affichés dans des blocs repliables n’étaient pas conservés dans les anciens segments. C’était notamment le cas de la page « Se nourrir », où les noms, adresses et horaires des cafétérias et restaurants universitaires apparaissent dans des blocs structurés. J’ai donc modifié l’extracteur afin de préserver ces éléments et de produire un segment autonome pour chaque lieu, avec son titre, son adresse et ses horaires.

J’ai reconstruit l’index avec multilingual-e5-base et vérifié que les informations ajoutées étaient effectivement présentes dans la base. J’ai aussi comparé plusieurs formulations de questions afin d’observer la robustesse de la recherche sémantique. Ces tests ont confirmé qu’un bon résultat dépend de la qualité des segments, de l’embedding et du réordonnancement. Le modèle de génération ne doit intervenir qu’après cette vérification.

Le prototype local reste cependant limité par les ressources de mon ordinateur. L’exécution de Mistral avec Ollama repose principalement sur la machine locale, ce qui entraîne des temps de réponse élevés et parfois des délais d’expiration. Cette contrainte rend difficiles les tests par lots et la comparaison de plusieurs configurations. J’ai donc étudié la possibilité de déployer la partie génération sur un serveur du laboratoire équipé d’un GPU plus puissant.

Pour cette migration, j’ai retenu une architecture dans laquelle l’index E5 et les scripts RAG restent indépendants du serveur de génération. Le modèle Ministral-8B-Instruct-2410 pourra être servi par vLLM à travers une API compatible avec le format OpenAI, tandis que le script du chatbot continuera à construire le prompt et à envoyer les requêtes. Cette séparation facilite le remplacement du modèle sans modifier le reste du pipeline. J’ai également préparé des chemins configurables et un fichier de dépendances pour éviter d’inscrire dans le code des chemins propres à mon ordinateur.

## Semaine 9 (20/08/2026-30/08/2026)
Après l’interruption estivale, j’ai repris le projet en mettant en place la version serveur. Un espace de travail a été créé dans le répertoire de données du laboratoire, afin d’éviter le manque d’espace du répertoire personnel. J’ai configuré un environnement Python séparé et les dépendances nécessaires à sentence-transformers et vLLM.

J’ai ensuite déployé Ministral-8B-Instruct-2410 sur le GPU NVIDIA L40S avec vLLM. Le modèle est exposé localement sur le serveur par une API HTTP. Les scripts de génération ont été adaptés pour appeler cette API, tandis que l’encodage de la requête E5 peut rester sur CPU afin d’éviter une concurrence inutile avec le modèle de génération. L’utilisation de tmux permet de maintenir le serveur vLLM actif indépendamment de la connexion SSH.

J’ai également transféré le pipeline de collecte et relancé le scraping afin d’obtenir une version actualisée de la base documentaire. Après préparation de la base prototype, 1 004 segments ont été conservés et un nouvel index de 1 004 embeddings a été construit avec intfloat/multilingual-e5-base. La nouvelle extraction conserve correctement les blocs repliables de la page « Se nourrir » : la Cafétéria de l’Inalco, le Restaurant universitaire La Barge et la Cafétéria des Grands Moulins disposent maintenant de segments distincts contenant leurs informations pratiques.

Les tests ont toutefois révélé plusieurs erreurs de classement. Le terme « Crous » déclenchait à la fois les routes « restauration » et « bourses », ce qui faisait remonter des pages d’aides sociales pour une question sur les restaurants. De plus, la détection par simple sous-chaîne associait « cafétéria » au déclencheur « CAF » de la route logement. J’ai corrigé le routeur en utilisant des limites de mots, en supprimant « Crous » comme déclencheur isolé des bourses et en ajoutant des expressions explicites telles que « aide financière ». J’ai aussi donné un poids plus important aux correspondances dans le titre, la section et le thème qu’aux mots rencontrés seulement dans le corps du texte.

Après cette correction, les résultats relatifs aux restaurants proviennent principalement de la page « Se nourrir » et les pages de bourses ne figurent plus parmi les premiers résultats. Il reste néanmoins des doublons proches, par exemple deux versions du passage consacré à Plan Libre, qui occupent inutilement plusieurs positions. De plus, une question demandant une liste complète peut nécessiter plusieurs sections d’une même page, alors qu’un top-k fixe ne garantit pas leur présence dans le contexte final.

La prochaine étape sera donc d’ajouter une suppression des quasi-doublons au moment de la récupération, un réordonnancement des candidats et une expansion contrôlée vers les sections voisines d’une même page pour les questions de type liste. Je pourrai ensuite relancer le jeu de tests et comparer le RAG simple, le RAG avec réordonnancement, le seuil de confiance et l’abstention.

## Semaine 10 (31/08/2026-06/09/2026)

Cette semaine, j’ai réexaminé le périmètre fonctionnel du chatbot. Les premières versions étaient principalement conçues pour les étudiants déjà inscrits, alors que le chatbot doit également pouvoir répondre aux personnes qui souhaitent découvrir les formations ou candidater à l’Inalco.

J’ai donc élargi la liste blanche utilisée pour le site institutionnel. En plus des informations concernant la vie étudiante, la scolarité et les services numériques, le pipeline peut maintenant collecter des pages relatives aux formations, aux candidatures, aux conditions d’admission et aux inscriptions administratives. Cette extension reste contrôlée afin d’éviter de réintroduire un trop grand nombre de pages institutionnelles sans rapport direct avec les besoins des utilisateurs.

Afin de distinguer les situations des utilisateurs sans leur imposer une classification préalable, j’ai ajouté des métadonnées d’audience et d’étape du parcours. Les segments peuvent notamment concerner les candidats, les étudiants admis mais pas encore inscrits, les étudiants inscrits ou l’ensemble des publics. Les étapes comprennent le choix d’une formation, la candidature, l’inscription administrative, l’inscription pédagogique et le déroulement des études.

Cette représentation permet au système de rechercher dans une base commune tout en conservant le contexte administratif de chaque information. Elle doit notamment réduire les confusions entre candidature, admission, inscription administrative et inscription pédagogique.

J’ai également revu les règles de génération. Lorsque la question dépend d’une formation, d’un niveau ou du profil du candidat, le chatbot ne doit pas sélectionner arbitrairement une procédure. Pour certaines questions insuffisamment précisées, par exemple les dates de candidature ou le niveau de français requis, le système doit demander une clarification.

La prochaine étape consiste à construire un jeu d’évaluation qui couvre à la fois les candidats et les étudiants inscrits, puis à comparer plusieurs mécanismes de récupération et de contrôle des réponses.

## Semaine 11 (07/09/2026-13/09/2026)

J’ai conçu cette semaine un protocole expérimental pour comparer plusieurs variantes du chatbot dans les mêmes conditions.

J’ai préparé un jeu de 100 questions représentatives. Les questions couvrent les formations, les candidatures, les inscriptions, les bourses, le logement, la restauration, les emplois du temps, les examens, les services numériques, la mobilité internationale, la santé, le handicap et la vie associative.

Chaque question est associée à un comportement attendu : répondre, demander une clarification ou s’abstenir. Pour les questions auxquelles le système doit répondre, j’ai ajouté des faits de référence et les passages officiels qui permettent de les vérifier. Le jeu a été divisé en trois parties : 10 questions pilotes, 20 questions de validation et 70 questions de test.

J’ai défini cinq configurations expérimentales :

- M0 : modèle de langage sans récupération documentaire ;
- M1 : RAG avec recherche sémantique simple ;
- M2 : RAG avec réordonnancement heuristique ;
- M3 : RAG avec seuil de confiance et mécanisme de clarification ;
- M4 : RAG avec seuil, clarification et consigne stricte d’abstention.

Ces configurations utilisent le même modèle de génération, le même modèle d’embedding et le même index. Cette organisation permet d’attribuer les différences observées au mécanisme étudié plutôt qu’à un changement de modèle ou de corpus.

J’ai également développé des scripts pour mesurer la récupération documentaire à partir des preuves annotées. Les principales mesures sont Hit@k, MRR, rappel des preuves à Top-k, présence d’une preuve correcte dans le contexte final et rappel des preuves présentes dans ce contexte.

Pour le comportement du chatbot, j’évalue séparément les décisions de réponse, de clarification et d’abstention. Cette distinction est importante, car une accuracy élevée peut être trompeuse si une méthode répond systématiquement à toutes les questions.

Les essais pilotes ont montré qu’un bonus lexical trop important peut améliorer certains thèmes, mais aussi provoquer des erreurs de routage. Par exemple, le terme « sites » dans une question sur le Wi-Fi pouvait faire remonter des pages décrivant l’accès aux bâtiments. Le réordonnancement est donc conservé comme une configuration expérimentale, et non comme une amélioration supposée acquise.

## Semaine 12 (14/09/2026-20/09/2026)

Cette semaine, j’ai synchronisé les nouvelles versions des scripts avec le serveur du laboratoire et reconstruit la base documentaire et l’index d’embeddings.

Le pipeline prend désormais en compte les pages destinées aux candidats et aux étudiants inscrits. Il conserve les métadonnées d’audience, d’étape du parcours, d’année universitaire, de niveau de risque et de type de contenu. J’ai également ajouté la prise en charge de deux documents PDF institutionnels : le Schéma Directeur de la Vie Étudiante et le Schéma Directeur Développement Durable et Responsabilité Sociétale et Environnementale. Les passages extraits conservent le titre du document, l’URL source et le numéro de page.

Une nouvelle extraction a produit 217 pages et 1 126 segments web avant l’intégration finale des contenus PDF. Les pages du portail étudiant restent majoritaires, tandis que les pages institutionnelles sélectionnées apportent principalement les informations sur les candidatures, les formations et les inscriptions.

J’ai vérifié plusieurs cas importants, notamment les langues enseignées, les programmes d’échange, les procédures d’admission en master, les restaurants universitaires, les inscriptions pédagogiques et le statut AJAC. Ces essais ont permis de corriger certaines omissions dans la liste blanche et plusieurs erreurs d’appariement entre une question et une section documentaire.

J’ai ensuite exécuté les configurations M0 à M4 sur le jeu de validation. La recherche sémantique simple obtient une bonne couverture des preuves annotées. Le réordonnancement heuristique améliore certains classements, mais peut également dégrader des questions lorsque les indices lexicaux sont ambigus.

Le seuil sémantique a été calibré uniquement sur le jeu de validation. La valeur retenue pour l’expérience finale est 0,869201. Les premiers résultats montrent cependant un compromis important : le seuil réduit les réponses potentiellement dangereuses, mais provoque aussi des abstentions lorsque le contexte contient déjà une preuve correcte.

J’ai donc décidé de figer les paramètres, le modèle, l’index et le jeu de test avant l’évaluation finale. Le jeu de test ne sera pas utilisé pour modifier le seuil ou les règles de récupération. Les résultats obtenus après cette étape serviront à mesurer la capacité de généralisation des différentes méthodes.

La prochaine étape consiste à exécuter les cinq configurations sur les 70 questions de test, à produire les tableaux et visualisations, puis à réaliser une analyse qualitative des erreurs les plus représentatives.

## Semaine 13 (21/09/2026-27/09/2026)
J’ai terminé l’évaluation des 5 configurations M0 à M4 sur les 70 questions du jeu de test. Avant l’exécution, j’ai figé le jeu de questions, l’index documentaire et les principaux paramètres de génération pour comparer les méthodes dans des conditions identiques.

Pour les 53 questions annotées comme pouvant recevoir une réponse, M1 et M2 retrouvent au moins une preuve de référence dans les 5 premiers passages pour 50 questions. Le réordonnancement heuristique M2 améliore le rang des preuves retrouvées : le MRR passe de 0,843 pour M1 à 0,875 pour M2. Ce résultat porte sur la récupération documentaire et ne démontre pas une amélioration de la fidélité des réponses.

J’ai aussi évalué le comportement « répondre, demander une clarification ou s’abstenir ». M0, M1 et M2 obtiennent une accuracy de 0,757, 0,800 et 0,814. M3 et M4 atteignent chacun 0,486 : le seuil réduit certaines réponses insuffisamment étayées, mais entraîne aussi des abstentions excessives lorsque des informations utiles sont présentes dans le contexte. Cette mesure comportementale doit donc être interprétée avec les matrices de confusion et la couverture des réponses.

L’analyse des réponses montre qu’il faut distinguer 3 sources d’erreurs : l’absence d’une information dans la base, le mauvais classement d’un passage, et une génération qui ne respecte pas suffisamment les preuves fournies. Une évaluation qualitative de la fidélité factuelle reste nécessaire pour mesurer les hallucinations ; les métriques de récupération et de comportement ne suffisent pas à elles seules.

## Semaine 13 (28/09/2026-30/09/2026)
J’ai étudié une autre manière de réordonner les passages, et j’ai ajouté le modèle neuronal multilingue BGE-reranker-v2-m3 sans entraînement sur le corpus Inalco. La recherche E5 sélectionne d’abord 10 passages candidats, ensuite le BGE les reclasse, et les 5 premiers sont proposés pour la génération. Cette configuration constitue une méthode supplémentaire, distincte du réordonnancement heuristique M2 déjà évalué.

Sur le jeu de validation, BGE avec 10 candidats retrouve une preuve de référence dans le top 5 pour 14 des 15 questions qu’il faut répondre, contre 13 pour M1 et 12 pour le M2 heuristique testé dans cette comparaison. L’augmentation du nombre de candidats à 20 ou 30 n’améliore pas le résultat final. Avant le réordonnancement, plus de passages sont disponible, mais certains passages pertinents se retrouvent moins bien classés ou ne sont pas inclus dans le contexte transmis au modèle.

J’ai ensuite comparé cette configuration aux résultats du jeu de test avec le même index et les mêmes questions. BGE-10 obtient 50 questions avec une preuve dans le top 5 sur 53 questions qu’il faut répondre. Son MRR est toutefois inférieur : 0,792, contre 0,843 pour M1 et 0,875 pour M2. Il améliore certains cas, notamment une question sur les masters accessibles par Mon Master, mais les autres se sont dégradées. Dans une question sur les coordonnées du secrétariat pédagogique, le passage pertinent apparaît encore dans le top 5, mais n’entre pas dans le contexte final à cause de la limite de longueur.

Ces résultats montrent qu’un modèle de réordonnancement plus complexe n’est pas toujours meilleur pour ce corpus. Comme le jeu de test avait déjà été examiné lors des expériences précédentes, je présente BGE comme une analyse complémentaire, la prochaine étape est de générer les réponses avec BGE-10 dans les mêmes conditions que les méthodes précédentes, puis de comparer manuellement leur fidélité aux sources, leur complétude et leurs citations.
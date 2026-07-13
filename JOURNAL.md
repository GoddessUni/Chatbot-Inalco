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

J’ai donc conçu un script prompt.py avec la méthode standard, qui permet au modèle de synthétiser plusieurs extraits lorsque ceux-ci se complètent.

Pour la génération, j’ai commencé à tester une intégration locale avec Ollama. Le prototype appelle un modèle de génération local via l’API d’Ollama après l’étape de récupération des passages. Cela permet de conserver une architecture locale pour les premiers essais : la question est traitée par le pipeline RAG, les extraits sont intégrés au prompt, puis le modèle génère une réponse accompagnée des sources.

J’ai d’abord utilisé le modèle Mistral disponible dans Ollama pour valider la chaîne complète : question d’utilisateur → récupération des segments → construction du prompt → génération locale → réponse avec sources.

Les premiers tests montrent que le système retrouve correctement les pages pertinentes lorsque les informations sont présentes dans la base. Par exemple, pour les questions sur l’accès aux différents sites de l’Inalco, les extraits concernant le Pôle des langues et civilisations et la Maison de la recherche sont bien récupérés. J’ai aussi identifié certains cas où la base documentaire était incomplète. par exemple, la page « Se nourrir » contenait des informations plus détaillées sur les cafétérias et restaurants Crous, mais ces éléments n’étaient pas présents dans l’ancien index. J’ai donc modifié le script d’extraction afin de mieux conserver les contenus structurés, notamment les blocs de cartes ou de listes, qui peuvent contenir des adresses et horaires.

Maintenant ce prototype de chatbot est capable de fournir des réponses en fonction des questions saisies par les utilisateurs. Ma prochaine étape vise à la préparation d’une première grille d’évaluation portant sur la pertinence des sources, la fidélité de la réponse et les cas d’abstention. Et je comparerai les réponses générées avec le prompt standard et le prompt plus strict.

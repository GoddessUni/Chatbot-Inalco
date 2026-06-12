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
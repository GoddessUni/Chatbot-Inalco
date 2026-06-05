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
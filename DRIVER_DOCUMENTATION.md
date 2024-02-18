# Script de Gestion des Projets Git : generate_project_files_list.py

[generate_project_files_list.py](./driver/generate_project_files_list.py) : Ce script automatise la création d'un dossier `result` contenant la liste des fichiers présents dans plusieurs projets Git. Pour chaque projet, un sous-dossier est créé dans `result`, contenant un fichier `all_project_files.txt` qui liste tous les fichiers du projet.

## Fonctionnement du Script

1. Utilisez les 8 projets Git.

# Script d'Étiquetage des Fichiers bogues : process_bug_data.py

[process_bug_data.py](./driver/process_bug_data.py) : Ce script est conçu pour analyser et étiqueter les fichiers d'un ensemble de projets en fonction de leur association avec des bugs. Il utilise les données extraites par l'outil SZZ, pour déterminer quels fichiers ont été affectés par des bugs.

## Fonctionnement du Script

1. Les données nécessaires sont (`commits.json`, `fix_and_introducers_pairs.json`) et (`all_project_files.txt`) pour chaque projet.

2. À partir des données de (`commits.json`, `fix_and_introducers_pairs.json`), le script identifie les fichiers qui ont été modifiés dans un commit de correction de bug.

3. Pour chaque fichier dans le projet, un indicateur est enregistré dans un fichier CSV (`file_bug_indicators.csv`), marquant le fichier comme bogué (1) ou non-bogué (0).

4. Les résultats sont organisés dans le dossier bug_reports, avec un sous-dossier pour chaque projet. Chaque sous-dossier contient son propre fichier `file_bug_indicators.csv`.

# Script d'Analyse le Code des Projets : project_code_analyzer.py

[project_code_analyzer.py](./driver/project_code_analyzer.py) : Ce script est conçu pour traiter les données extraites à partir du modèle, en identifiant les classes et en les associant à leurs fichiers respectifs. Ce processus aboutit à la création d'un fichier CSV `output.csv`  pour chaque projet.

## Fonctionnement du Script

1. Chargement et Filtrage des Données : Le script charge les données depuis des fichiers JSON ( les fichiers des modèles) et filtre les éléments correspondant à des classes TypeScript (FamixTypeScript.Class).

2. Extraction et Nettoyage des Chemins : À partir des chemins qualifiés complets, le script extrait les parties spécifiques des chemins en utilisant des expressions régulières et nettoie les résultats (tu dois changer selon ton chemin)

3. Sauvegarde des Résultats dans CSV : Les données filtrées sont enregistrées dans un fichier `output.csv` pour chaque projet, indiquant le nom du fichier et le nom de la classe associée.

# Script : project_metrics_analyzer.py

[project_metrics_analyzer.py](./driver/project_metrics_analyzer.py) : Ce script a pour but d'associer les informations relatives aux bugs, aux classes et méthodes, et aux métriques de code (comme LOC et CC) pour chaque fichier de projet. Il produit un fichier CSV global contenant ces données.

## Fonctionnement du Script

1. Chargez les indicateurs de bugs et les associations de classes à partir des fichiers CSV générés précédemment : `output.csv` et `file_bug_indicators.csv`
2. Fusionne les données chargées et extrait les métriques de code pour chaque classe ou méthode en utilisant les fichiers CSV contenant ces métriques (generés pa pharo).
3. Les données traitées pour tous les projets sont enregistrées dans un fichier CSV global `final_data.csv`.

# project_metrics_correlation_analysis.py

[project_metrics_correlation_analysis.py](./driver/project_metrics_correlation_analysis.py) : Ce script effectue une analyse de corrélation pour déterminer la relation entre les métriques de code (comme LOC et CC) et la présence de bugs (indicateur de bug).

## Fonctionnement du Script

1. Utilisez `final_data.csv`

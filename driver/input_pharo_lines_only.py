import json
import csv
import os

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:  
        data = json.load(file)
    return data

def analyze_project(projectPath):
    # Assurez-vous que projectPath se termine par '/'
    if not projectPath.endswith('/'):
        projectPath += '/'

    # Charger les données depuis les fichiers JSON spécifiques au projet
    try:
        fix_and_introducers_pairs = load_json(f'{projectPath}fix_and_introducers_pairs.json')
        commits = load_json(f'{projectPath}commits.json')
    except FileNotFoundError as e:
        print(f"Erreur : {e}")
        return
    
    # Extraire les identifiants des commits de fix_and_introducers_pairs
    fix_commit_ids = set(pair[0] for pair in fix_and_introducers_pairs)


   # Préparer une liste pour stocker les données du CSV
    csv_data = []

    # Parcourir les commits dans commits.json et vérifier leur présence dans fix_commit_ids
    for commit_id, commit_data in commits.items():
        if commit_id in fix_commit_ids:
            for src in commit_data["changes"]:
                fixer_commit_id = commit_id
                change_type = commit_data["changes"][src]
                bug_intro_lines = []
                bug_fix_lines = []
                if "delete" in commit_data["diff"][src][0]:
                    bug_intro_lines = [int(elem)+1 for i, elem in enumerate(commit_data["diff"][src][0]["delete"]) if i % 2 == 0]
                if "add" in commit_data["diff"][src][0]:
                    bug_fix_lines = [int(elem)+1 for i, elem in enumerate(commit_data["diff"][src][0]["add"]) if i % 2 == 0]

                # Ajouter les données au CSV seulement si bug_intro_lines n'est pas vide, car sinon y a pas de bogues
                if bug_intro_lines:
                    csv_data.append([fixer_commit_id, src, change_type, bug_intro_lines, bug_fix_lines])
                    
    #-----------------------------------------------------------------------------------------
    # Préparer un dictionnaire pour stocker le nombre de lignes introductrices de bogues par fichier source
    bug_intro_lines_by_source = {}

    # Parcourir les commits dans commits.json et vérifier leur présence dans fix_commit_ids
    for commit_id, commit_data in commits.items():
        if commit_id in fix_commit_ids:
            for src in commit_data["changes"]:
                bug_intro_lines = []
                if "delete" in commit_data["diff"][src][0]:
                    bug_intro_lines = [int(elem)+1 for i, elem in enumerate(commit_data["diff"][src][0]["delete"]) if i % 2 == 0]

                # Ajouter les données au dictionnaire seulement si bug_intro_lines n'est pas vide, car sinon il n'y a pas de bogues
                if bug_intro_lines:
                    if src not in bug_intro_lines_by_source:
                        bug_intro_lines_by_source[src] = 0
                    bug_intro_lines_by_source[src] += len(bug_intro_lines)
    #-----------------------------------------------------------------------------------------
    # Ajustez cette partie pour écrire dans un fichier CSV unique pour chaque projet
    with open(f'{projectPath}input_pharo_lines_only.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(['fixer_commit_id', 'source_file', 'change_type', 'bug_intro_lines', 'bug_fix_lines'])
        csv_writer.writerows(csv_data)

def main(relativePath):
    projects = os.listdir(relativePath)
    for project in projects:
        projectPath = os.path.join(relativePath, project)
        if os.path.isdir(projectPath):
            print(f"Analyse du projet : {project}")
            analyze_project(projectPath)

if __name__ == "__main__":
    relativePath = "sortie/results"
    main(relativePath)





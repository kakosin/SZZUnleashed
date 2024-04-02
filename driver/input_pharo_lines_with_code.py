import json
import csv
import os 

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:  
        data = json.load(file)
    return data

def analyze_project(projectPath):
    if not projectPath.endswith('/'):
        projectPath += '/'
    
    try:
        fix_and_introducers_pairs = load_json(f'{projectPath}fix_and_introducers_pairs.json')
        commits = load_json(f'{projectPath}commits.json')
    except FileNotFoundError as e:
        print(f"Erreur : {e}")
        return
    
    fix_commit_ids = set(pair[0] for pair in fix_and_introducers_pairs)
    csv_data = []
    for commit_id, commit_data in commits.items():
        if commit_id in fix_commit_ids:
            for src in commit_data["changes"]:
                fixer_commit_id = commit_id
                change_type = commit_data["changes"][src]
                bug_intro_lines = []
                bug_fix_lines = []
                if "delete" in commit_data["diff"][src][0]:
                    for i, elem in enumerate(commit_data["diff"][src][0]["delete"]):
                        if i % 2 == 0:
                            bug_intro_lines.append(int(elem)+1)
                        else:
                            bug_intro_lines.append(elem)
                if "add" in commit_data["diff"][src][0]:
                    for i, elem in enumerate(commit_data["diff"][src][0]["add"]):
                        if i % 2 == 0:
                            bug_fix_lines.append(int(elem)+1)
                        else:
                            bug_fix_lines.append(elem)

                # Ajouter les données au CSV seulement si bug_intro_lines n'est pas vide, car sinon y a pas de bogues
                if bug_intro_lines:
                    csv_data.append([fixer_commit_id, src, change_type, bug_intro_lines, bug_fix_lines])

    with open(f'{projectPath}input_pharo_lines_with_code.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        # Écrire l'en-tête
        csv_writer.writerow(['fixer_commit_id', 'source_file', 'change_type', 'bug_intro_lines', 'bug_fix_lines'])
        # Écrire les données
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
import json
import csv

relativePath = "entree/Input_Pharo_Bugged_LOC/Examples/jacomyal__sigma/"

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def main():
    # Charger les données depuis les fichiers JSON
    fix_and_introducers_pairs = load_json(f'{relativePath}fix_and_introducers_pairs.json')
    commits = load_json(f'{relativePath}commits.json')

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

    # Écrire les données dans un fichier CSV
    with open(f'{relativePath}input_pharo_lines_with_code.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        # Écrire l'en-tête
        csv_writer.writerow(['fixer_commit_id', 'source_file', 'change_type', 'bug_intro_lines', 'bug_fix_lines'])
        # Écrire les données
        csv_writer.writerows(csv_data)

if __name__ == "__main__":
    main()

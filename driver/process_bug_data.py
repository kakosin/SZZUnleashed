import os
import json
import csv

def charger_json(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        return json.load(fichier)

def charger_tous_les_fichiers(nom_fichier):
    with open(nom_fichier, 'r', encoding='utf-16') as fichier:
        return set(fichier.read().splitlines())

def identifier_paires_uniques(donnees_paires):
    return {tuple(paire) for paire in donnees_paires}

def identifier_fichiers_bugges(donnees_commits, paires_uniques):
    fichiers_bugges = set()
    for commit, details in donnees_commits.items():
        if commit in {paire[1] for paire in paires_uniques}:
            fichiers_bugges.update(details['changes'])
    return fichiers_bugges

def sauvegarder_indicateurs_de_bugs(fichiers_bugges, fichiers_non_bugges, chemin_csv):
    with open(chemin_csv, 'w', newline='', encoding='utf-8') as csvfile:
        champs = ['file_name', 'bug_indicator']
        ecrivain = csv.DictWriter(csvfile, fieldnames=champs, delimiter=';') 
        ecrivain.writeheader()
        for fichier in sorted(fichiers_bugges):
            ecrivain.writerow({'file_name': fichier, 'bug_indicator': 1})
        for fichier in sorted(fichiers_non_bugges):
            ecrivain.writerow({'file_name': fichier, 'bug_indicator': 0})

def traiter_projet(chemin_projet):
    donnees_commits = charger_json(os.path.join(chemin_projet, 'commits.json'))
    donnees_paires = charger_json(os.path.join(chemin_projet, 'fix_and_introducers_pairs.json'))
    tous_les_fichiers = charger_tous_les_fichiers(os.path.join(chemin_projet, 'all_project_files.txt'))
    
    paires_uniques = identifier_paires_uniques(donnees_paires)
    fichiers_bugges = identifier_fichiers_bugges(donnees_commits, paires_uniques)
    fichiers_non_bugges = tous_les_fichiers - fichiers_bugges
    
    nom_projet = os.path.basename(chemin_projet)
    dossier_rapports = os.path.join('bug_reports', nom_projet)
    os.makedirs(dossier_rapports, exist_ok=True)
    
    chemin_csv = os.path.join(dossier_rapports, 'file_bug_indicators.csv')
    sauvegarder_indicateurs_de_bugs(fichiers_bugges, fichiers_non_bugges, chemin_csv)

if __name__ == "__main__":
    dossier_racine = 'modeled_results'
    for nom_projet in os.listdir(dossier_racine):
        chemin_projet = os.path.join(dossier_racine, nom_projet)
        if os.path.isdir(chemin_projet):
            traiter_projet(chemin_projet)

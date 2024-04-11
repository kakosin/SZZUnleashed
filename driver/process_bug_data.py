import os
import csv

def lire_csv_dict(chemin_csv):
    try:
        with open(chemin_csv, mode='r', encoding='utf-8') as fichier:
            lecteur = csv.DictReader(fichier)
            return [ligne for ligne in lecteur]
    except FileNotFoundError:
        print(f"Le fichier {chemin_csv} n'existe pas.")
        return []

def sauvegarder_indicateurs_de_bugs(fichiers_bugges, chemin_csv):
    with open(chemin_csv, 'w', newline='', encoding='utf-8') as csvfile:
        champs = ['file_name', 'bug_indicator']
        ecrivain = csv.DictWriter(csvfile, fieldnames=champs, delimiter=';')
        ecrivain.writeheader()
        for fichier in fichiers_bugges:
            ecrivain.writerow({'file_name': fichier, 'bug_indicator': fichiers_bugges[fichier]})

def traiter_projet(chemin_projet):
    liste_fichiers = lire_csv_dict(os.path.join(chemin_projet, 'liste_fichiers.csv'))
    fichiers_bugges_infos = lire_csv_dict(os.path.join(chemin_projet, 'input_pharo_lines_only.csv'))

    fichiers_bugges = {ligne['source_file'] for ligne in fichiers_bugges_infos}

    indicateurs_bugs = {ligne['Nom du fichier']: 0 for ligne in liste_fichiers}
    for fichier in indicateurs_bugs:
        if fichier in fichiers_bugges:
            indicateurs_bugs[fichier] = 1

    chemin_csv = os.path.join(chemin_projet, 'file_bug_indicators.csv')
    sauvegarder_indicateurs_de_bugs(indicateurs_bugs, chemin_csv)

def main(dossier_racine):
    for nom_projet in os.listdir(dossier_racine):
        chemin_projet = os.path.join(dossier_racine, nom_projet)
        if os.path.isdir(chemin_projet):
            print(f"Traitement du projet : {nom_projet}")
            traiter_projet(chemin_projet)

if __name__ == "__main__":
    dossier_racine = 'sortie/results'
    main(dossier_racine)

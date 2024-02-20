import os
import json
import csv
import re

def charger_et_filtrer_donnees_json(chemin_fichier_json):
    try:
        with open(chemin_fichier_json, 'r', encoding='utf-8') as fichier_json:
            donnees = json.load(fichier_json)
    except FileNotFoundError:
        print(f"Le fichier {chemin_fichier_json} n'a pas été trouvé.")
        return []  
    
    donnees_filtrees = [
        item for item in donnees 
        if item.get('FM3') == 'FamixTypeScript.Class'
    ]
    return donnees_filtrees

def extraire_chemin_specifique(chemin_complet, pattern_recherche):
    match = re.search(pattern_recherche, chemin_complet)
    if match:
        return match.group(1) #chemin_complet[match.end():]  
    return chemin_complet  

def sauvegarder_donnees_csv(donnees, nom_projet, chemin_fichier_csv):
    champs = ['file_name', 'nameClass']
    # motif_projet = re.compile(r'Project/[^/]+/')
    motif_projet = re.compile(r".*"+nom_projet+r"/(.*)")
    with open(chemin_fichier_csv, 'w', newline='') as fichier_csv:
        ecrivain = csv.writer(fichier_csv, delimiter=';')
        ecrivain.writerow(champs)
        
        for item in donnees:
            chemin_complet = item.get('fullyQualifiedName', '').split('"')[-2]
            partie_chemin = extraire_chemin_specifique(chemin_complet, motif_projet)
            partie_chemin = partie_chemin.replace('"', '').strip()  # Nettoie le chemin de tout guillemet et espace blanc
            
            ligne = [partie_chemin, item.get('name', '')]
            ecrivain.writerow(ligne)

def traiter_fichier_json(chemin_fichier_json, nom_projet, dossier_sortie='processed_projects'):
    print("Analysing model: "+chemin_fichier_json)
    donnees_filtrees = charger_et_filtrer_donnees_json(chemin_fichier_json)
    
    # nom_projet = os.path.splitext(os.path.basename(chemin_fichier_json))[0]
    dossier_projet_sortie = os.path.join(dossier_sortie, nom_projet)
    os.makedirs(dossier_projet_sortie, exist_ok=True)
    
    chemin_fichier_csv = os.path.join(dossier_projet_sortie, 'output.csv')
    sauvegarder_donnees_csv(donnees_filtrees, nom_projet, chemin_fichier_csv)

def traiter_dossiers(dossier_racine, dossier_sortie):
    for racine, dossiers, fichiers in os.walk(dossier_racine):
        for fichier in fichiers:
            if fichier.endswith('.json') and os.path.splitext(fichier)[0] == os.path.basename(racine):
                chemin_fichier_json = os.path.join(racine, fichier)
                traiter_fichier_json(chemin_fichier_json, dossier_sortie)

def main(dossier_racine, dossier_sortie='processed_projects'):
    traiter_dossiers(dossier_racine, dossier_sortie)

if __name__ == "__main__":
    dossier_racine = 'sortie/backup_results'
    dossier_sortie = 'processed_projects'
    main(dossier_racine, dossier_sortie)

import pandas as pd
import numpy as np
import os


def lister_projets(dossier):
    return [nom for nom in os.listdir(dossier) if os.path.isdir(os.path.join(dossier, nom))]

def charger_donnees(nom_projet):
    chemin_bug_indicators = f'bug_reports/{nom_projet}/file_bug_indicators.csv'
    chemin_output = f'processed_projects/{nom_projet}/output.csv'
    file_bug_indicators = pd.read_csv(chemin_bug_indicators, delimiter=';')
    output = pd.read_csv(chemin_output, delimiter=';')
    merged = pd.merge(output, file_bug_indicators, on='file_name')
    return merged

def creer_enregistrement(loc, cc, bug_indicator):
    return {'LOC': loc, 'CC': cc, 'indicator_bug': bug_indicator}

def traiter_donnees(merged, nom_projet):
    data = []
    for _, row in merged.iterrows():
        file_name = row['file_name']
        class_name = row['nameClass']
        bug_indicator = row['bug_indicator']
        metrics_file_path = f'metrics/{nom_projet}/{class_name}_metrics.csv'
        try:
            metrics = pd.read_csv(metrics_file_path)
            for _, metric_row in metrics.iterrows():
                loc = metric_row['LOC']
                cc = 0 if metric_row['ClassOrMethod'] == 'C' else metric_row['CC'] if metric_row['CC'] != '-' else np.nan
                data.append(creer_enregistrement(loc, cc, bug_indicator))
        except FileNotFoundError:
            pass
    return data

def enregistrer_donnees(data, nom_projet, global_data):
    for row in data:
        global_data.append(row)

def main(dossier_projets):
    projets = lister_projets(dossier_projets)
    global_data = []
    for nom_projet in projets:
        print("Producing metrics for "+nom_projet)
        merged = charger_donnees(nom_projet)
        data = traiter_donnees(merged, nom_projet)
        enregistrer_donnees(data, nom_projet, global_data)
    
    dossier_global = 'project_processing_results/'
    if not os.path.exists(dossier_global):
        os.makedirs(dossier_global)
    final_data = pd.DataFrame(global_data)
    final_data.to_csv(f'{dossier_global}final_data.csv', index=False, sep=';')

if __name__ == "__main__":
    dossier_projets = 'bug_reports'
    main(dossier_projets)

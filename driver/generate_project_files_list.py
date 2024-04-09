import subprocess
import os
import csv

# Définition du dictionnaire de blacklist
blacklist = {
    'commence_par_point': lambda f: f.startswith('.'),
    'un_seul_mot': lambda f: '/' not in f and '.' not in f,
    'commence_par_tests': lambda f: f.startswith('__tests__/'),
}

extensions_autorisees = ['.ts', '.js', '.tsx']

def lister_fichiers_git(chemin_projet):
    """
    Exécute git ls-files dans le répertoire du projet pour obtenir la liste des fichiers.
    """
    try:
        result = subprocess.run(['git', 'ls-files'], cwd=chemin_projet, check=True, capture_output=True, text=True)
        return result.stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de git ls-files dans {chemin_projet}: {e}")
        return []

def fichier_valide(nom_fichier):
    """
    Vérifie si le fichier ne correspond à aucun critère de la blacklist et
    appartient à la liste des extensions autorisées.
    """
    # Vérifier d'abord la blacklist
    for condition in blacklist.values():
        if condition(nom_fichier):
            return False
    # Puis vérifier si l'extension est autorisée
    return any(nom_fichier.endswith(ext) for ext in extensions_autorisees)

def main(chemin_projet_source,chemin_projet_cible):
    # Parcourir chaque sous-dossier (projet) dans le chemin source
    for projet in os.listdir(chemin_projet_source):
        chemin_complet_source = os.path.join(chemin_projet_source, projet)
        if os.path.isdir(chemin_complet_source):
            fichiers = lister_fichiers_git(chemin_complet_source)
            fichiers_valides = [f for f in fichiers if fichier_valide(f)]
            
            # Préparer le chemin cible pour le fichier CSV du projet
            chemin_complet_cible = os.path.join(chemin_projet_cible, projet)
            os.makedirs(chemin_complet_cible, exist_ok=True)
            fichier_csv_projet = os.path.join(chemin_complet_cible, 'liste_fichiers.csv')
            
            # Écriture des fichiers valides dans le fichier CSV
            with open(fichier_csv_projet, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Nom du fichier'])  # En-tête du CSV
                for fichier in fichiers_valides:
                    writer.writerow([fichier])
            
            print(f"Liste des fichiers valides enregistrée dans '{fichier_csv_projet}'.")

if __name__ == '__main__':
    chemin_projet_source = 'sortie/git'
    chemin_projet_cible = 'sortie/results'
    main(chemin_projet_source,chemin_projet_cible)

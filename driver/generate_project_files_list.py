import subprocess
import os

def creer_dossier_cible(dossier_base, nom_dossier_cible='result'):
    chemin_dossier_cible = os.path.join(os.path.dirname(dossier_base), nom_dossier_cible)
    os.makedirs(chemin_dossier_cible, exist_ok=True)
    return chemin_dossier_cible

def lister_fichiers_git(chemin_projet):
    try:
        result = subprocess.run(['git', 'ls-files'], cwd=chemin_projet, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de git dans {chemin_projet}: {e}")
        return None

def ecrire_fichiers_git(dossier_cible, projet, contenu):
    """
    Écrit le contenu dans un fichier spécifique au projet dans le dossier cible.
    """
    chemin_sous_dossier_cible = os.path.join(dossier_cible, projet)
    os.makedirs(chemin_sous_dossier_cible, exist_ok=True)
    fichier_sortie = os.path.join(chemin_sous_dossier_cible, 'all_project_files.txt')
    
    with open(fichier_sortie, 'w') as f:
        f.write(contenu)

def main():
    # Chemin du dossier contenant les projets
    dossier_projets = 'Project'
    
    dossier_cible = creer_dossier_cible(dossier_projets)
    
    for projet in os.listdir(dossier_projets):
        chemin_projet = os.path.join(dossier_projets, projet)
        
        if os.path.isdir(chemin_projet):
            contenu = lister_fichiers_git(chemin_projet)
            if contenu is not None:
                ecrire_fichiers_git(dossier_cible, projet, contenu)

if __name__ == '__main__':
    main()

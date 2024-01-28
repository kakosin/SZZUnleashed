# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 21:07:53 2023

@author: CYTech Student
"""


from dotenv import load_dotenv
import csv  
import os
import subprocess
import shutil
import sys 

parent_folder = '/root/projet_tests' ## changer en '/output/git'

root_git = '/output/git'

load_dotenv('token.env')
token = os.getenv('GITHUB_TOKEN')

if token is None:
    print("GITHUB_TOKEN is not set in the environment", file = sys.stderr)
    raise SystemExit(1)
else: 
    print("GITHUB_TOKEN=",token)
os.makedirs(root_git, exist_ok=True)

with open('/input/Projects.csv', newline="") as csvfile:
    # Parcourir chaque ligne du DataFrame
    for row in csv.reader(csvfile):
        url, Commit = row
        print(f"URL: {url}, Commit: {Commit}")
        # Extraire le premier mot de l'URL GitHub
        github_owner, github_repo = url.split('/')[3:5]  # Assumant que l'URL suit le format "https://github.com/premier-mot/..."

        ## Préparation d'analyse du répo
        clone_folder= '__'.join([github_owner,github_repo])
        clone_folder_path = os.path.join(parent_folder, clone_folder)
        if not os.path.exists(clone_folder_path):
            os.makedirs(clone_folder_path, exist_ok=True)
            print(f"Dossier cree : {clone_folder_path}") 
        os.chdir(clone_folder_path)
        print("Current working directory is:", clone_folder_path)  

        ## Préparation du clonage du répo
        local_path = os.path.join(clone_folder_path,github_repo)
        destination_path = os.path.join(root_git, github_repo)        
        url_git = f"https://github.com/{github_owner}/{github_repo}.git"                               
        
        # Clonâge local du répo s'il n'existe pas (docker mapping volume)
        print("Check existence of local git repo:", local_path)
        try:
            if not os.path.exists(local_path) or len(os.listdir(local_path)) == 0:
                try:
                    result = subprocess.run(["git", "clone", url_git], timeout=300)
                    if result.returncode != 0:
                        print("Error:", result.returncode)
                        raise SystemExit(result.returncode)
                except (SystemExit, subprocess.TimeoutExpired) as e:
                    print(e)
            else:
                print("Repo already exists")
        except (Exception, UnicodeDecodeError) as e:
            print(e)
            continue
        # Copier le contenu du dossier cloné directement dans root_git
        # We assume if no local output folder, then we need to analyse repo
        if not os.path.exists(local_path) or len(os.listdir(local_path)) == 0:
            if not os.path.exists(destination_path) or len(os.listdir(destination_path)) == 0:
                print("copiage du dépôt en cours...")
                shutil.copytree(local_path, destination_path)
                print("Le clonage du dépôt est fini")
        else:
            print("The git repository already exists, skipping cloning!")

        ## Copiage des résultats d'analyse        
        project_output = os.path.join("/output/results", clone_folder )
        if not os.path.exists(project_output) or len(os.listdir(project_output)) == 0:
            os.makedirs(project_output, exist_ok=True)
            print("le dossier results est crée:",project_output)
        else:
            print("le dossier: "+project_output+" existe déjà, skipping..") 
            continue
        try:
            ## Analyse du projet git
            print("fetch_github.py...")                                                                     
            result = subprocess.run(["python3", "/root/fetch_github_bugs/fetch_github.py", github_owner, github_repo], timeout=300)
            if result.returncode != 0:
                print("Error:", result.returncode)
                raise SystemExit(result.returncode)
            
            print("git_log_to_array.py...")                                                                    
            result = subprocess.run(["python3", "/root/fetch_github_bugs/git_log_to_array.py", "--repo-path", github_repo, "--from-commit", Commit], timeout=300)
            if result.returncode != 0:
                print("Error:", result.returncode)
                raise SystemExit(result.returncode)
            
            print("find_bug_fixes.py...")                    
            result = subprocess.run(["python3", "/root/fetch_github_bugs/find_bug_fixes.py", "--gitlog", "./gitlog.json", "--issue-list", "./fetch_issues", "--gitlog-pattern", '"[Cc]loses #{nbr}\D|#{nbr}\D|[Ff]ixes #{nbr}\D"'], timeout=300)
            if result.returncode != 0:
                print("Error:", result.returncode)
                raise SystemExit(result.returncode)
            
            print("szz_find_bug_introducers-0.1.jar...")
            result = subprocess.run(["java", "-jar", "/root/szz/build/libs/szz_find_bug_introducers-0.1.jar", "-i", "./issue_list.json", "-r", github_repo], timeout=300)
            if result.returncode != 0:
                print("Error:", result.returncode)
                raise SystemExit(result.returncode)
        except (Exception, subprocess.TimeoutExpired, UnicodeDecodeError) as e:
            print(e)
            continue

        try:
            result = subprocess.run(["cp", "./results/annotations.json", project_output], timeout=60)
            if result.returncode != 0:
                print("Error copying annotations.json:", result.returncode)
                raise SystemExit(result.returncode)
            
            result = subprocess.run(["cp", "./results/commits.json", project_output], timeout=60)
            if result.returncode != 0:
                print("Error copying commits.json:", result.returncode)
                raise SystemExit(result.returncode)
            
            result = subprocess.run(["cp", "./results/fix_and_introducers_pairs.json", project_output], timeout=60)
            if result.returncode != 0:
                print("Error copying fix_and_introducers_pairs.json:", result.returncode)
                raise SystemExit(result.returncode)
        except (Exception, subprocess.TimeoutExpired) as e:
            print(e)

import os
import csv
import shutil

local_root = r"D:/dev/ETS/mgl843/SZZUnleashed"
results_path = os.path.join(local_root,"sortie/results/")
backup_results_path = os.path.join(local_root,"sortie/backup_results/")
modeled_results_path = os.path.join(local_root,"sortie/modeled_results/")

def cleanup_results():
    for root, dirs, files in os.walk(results_path):
        for dir in dirs:
            repo_name = dir.split("__")[1]
            project_path = os.path.join(root, dir)
            csv_model_path = os.path.join(project_path, "modele_"+repo_name+".csv")
            if not os.path.exists(csv_model_path):
                continue
            with open(csv_model_path, newline="") as csvmodel:
                count = 0
                for row in csv.reader(csvmodel):
                    count+=1
                if count > 1:
                    try:
                        shutil.copytree(project_path, os.path.join(backup_results_path, dir))
                    except (PermissionError,FileExistsError) as e:
                        print(e)

def prepare_results():
    for root, dirs, files in os.walk(backup_results_path):
        for dir in dirs:
            repo_name = dir.split("__")[1]
            project_path = os.path.join(backup_results_path, dir)
            json_model_path = os.path.join(project_path, dir+".json")
            if not os.path.exists(json_model_path):
                print(f'Model json does not exist: {json_model_path}')
                continue
            try:
                shutil.copytree(project_path, os.path.join(modeled_results_path, dir))
            except (PermissionError,FileExistsError) as e:
                print(e)

import os
import csv
import shutil

local_root = r"D:/dev/ETS/mgl843/SZZUnleashed"
results_path = os.path.join(local_root,"sortie/results/")
backup_results_path = os.path.join(local_root,"sortie/backup_results/")

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

import os
import csv
import shutil

local_root = r"D:/dev/ETS/mgl843/SZZUnleashed"
results_path = os.path.join(local_root,"sortie/results/")
backup_results_path = os.path.join(local_root,"sortie/backup_results/")
empty_results_path = os.path.join(local_root,"sortie/empty_results/")

def cleanup_results():
    if not os.path.exists(empty_results_path):
        os.makedirs(empty_results_path)

    for root, dirs, files in os.walk(results_path):
        for dir in dirs:
            repo_name = dir.split("__")[1]
            project_path = os.path.join(root, dir)
            csv_model_path = os.path.join(project_path, "modele_"+repo_name+".csv")
            empty_project_path = os.path.join(empty_results_path, project_path)
            if not os.path.exists(csv_model_path):
                shutil.move(project_path, empty_results_path)
            elif os.path.exists(empty_project_path):
                shutil.rmtree(empty_project_path)
            else:
                with open(csv_model_path, newline="") as csvmodel:
                    count = 0
                    for row in csv.reader(csvmodel):
                        count+=1
                if count < 2:
                    shutil.move(project_path, empty_results_path)
            shutil.copytree(project_path, backup_results_path)

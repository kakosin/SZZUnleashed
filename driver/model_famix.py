import os
import subprocess

local_root = r"D:/dev/ETS/mgl843/SZZUnleashed"
backup_results_path = os.path.join(local_root, "sortie/backup_results/")
git_folder_path = os.path.join(local_root, "sortie/git/")
BLACKLIST = ['redis__ioredis']

def produce_model():
    for root, dirs, files in os.walk(backup_results_path):
        for dir in dirs:
            if dir in BLACKLIST:
                continue
            owner_name = dir.split("__")[0]
            repo_name = dir.split("__")[1]
            url_git = f"https://github.com/{owner_name}/{repo_name}.git"
            git_project_path = os.path.join(git_folder_path, dir)
            try:
                if not os.path.exists(git_project_path) or len(os.listdir(git_project_path)) == 0:
                    try:
                        result = subprocess.run(
                            ["git", "clone", url_git, git_project_path], timeout=300)
                        if result.returncode != 0:
                            print("Error:", result.returncode)
                            raise SystemExit(result.returncode)
                    except (SystemExit, subprocess.TimeoutExpired) as e:
                        print(e)
                        continue
                else:
                    print("Repo already exists")
                    continue
            except (Exception, UnicodeDecodeError) as e:
                print(e)
                continue
            model_filepath = os.path.join(backup_results_path, dir, dir+"_ts2famix.json")
            tsconfig_filepath = os.path.join(git_project_path, "tsconfig.json")
            if os.path.exists(model_filepath):
                continue
            if os.path.exists(tsconfig_filepath):
                try:
                    print("Beginning ts2famix...")
                    subprocess.check_call(f"ts2famix -i {tsconfig_filepath} -o {model_filepath}", shell=True, stdout=subprocess.DEVNULL, timeout=600)
                    print("Ended ts2famix...")
                except subprocess.CalledProcessError as e:
                    print(e)
            else:
                print("No tsconfig available for repo: "+dir)
                continue
            if os.path.exists(model_filepath):
                print("Produced ts-morph model for repo: "+dir)
            else:
                print("No ts-morph model available")


produce_model()

import importlib
import os
import shutil
import sys
sys.path.append('D:/dev/ETS/mgl843/SZZUnleashed/')
from entree import project_crawler, project_cleanup
from driver import pipeline, model_famix, pharo_analysis, project_code_analyzer, process_bug_data
import time

ACTUAL_RESULTS_COUNT = 0
NEEDED_RESULTS_COUNT = 1
BLACKLIST = ["apollo-client","lobe-chat", "kibana", "vee-validate","misskey", "keystone"]

page = 1
per_page = 5

from dotenv import load_dotenv 

load_dotenv('dev.env')
local_run = os.environ.get("LOCAL")
# Run this section in a Docker environment
if local_run == '1':
    while ACTUAL_RESULTS_COUNT < NEEDED_RESULTS_COUNT+1:
        # Crawl projects to throw in pipeline
        print("Looking for repositories...")
        repositories = project_crawler.search_github_repositories(project_crawler.QUERY, page=page, per_page=per_page)
        project_crawler.write_to_csv(repositories, BLACKLIST)
        print("Added repositories!")

    # #     # Run pipeline for batch of projects
    # #     # print("Running bug analysis + Pharo pipeline...")
    # #     # pipeline.run_pipeline()
    # #     # print("done running bug analysis + Pharo pipeline...")

        # Prepare results
        time.sleep(2.5)
        print("Cleaning up results...")
        project_cleanup.cleanup_results()
        ACTUAL_RESULTS_COUNT = len(next(os.walk(project_cleanup.backup_results_path))[1])
        page+=1
        print(f"Found {ACTUAL_RESULTS_COUNT} coherent results...")

print("Producing ts2famix models...")
model_filepaths = model_famix.produce_model()

# Pharo analysis
print("Loading model in Pharo")
if local_run == '1':
    local_root = r"D:/dev/ETS/mgl843/SZZUnleashed"
    root_folder = os.path.join(local_root, "sortie/backup_results/")
    if not os.path.exists("metrics/"):
        os.mkdir("metrics")
    for subdir, dirs, files in os.walk(root_folder):
        for dir in dirs:
            project_dir = os.path.join(root_folder, dir)
            model_filepath = os.path.join(project_dir, dir+"_ts2famix.json")
            if os.path.exists(model_filepath):
                metrics_folder = f"metrics/{dir}/"
                if not os.path.exists(metrics_folder):
                    os.mkdir(metrics_folder)
                print("Producing pharo analysis for: "+model_filepath)
                pharo_analysis.analyse_model(model_filepath, metrics_folder)

# Analyze SZZ JSON files
print("Analysing SZZ JSON files")
local_root = r"D:/dev/ETS/mgl843/SZZUnleashed"
root_folder = os.path.join(local_root, "sortie/backup_results/")
filenames = ['annotations.json','fix_and_introducers_pairs.json','commits.json']
output_dir = os.path.join(local_root, "analysis/")
for subdir, dirs, files in os.walk(root_folder):
    for dir in dirs:
        project_dir = os.path.join(root_folder, dir)
        model_filepath = os.path.join(project_dir, dir+"_ts2famix.json")
        if os.path.exists(model_filepath):
            print("Analysing model: "+model_filepath)
            project_code_analyzer.process_json_file(model_filepath, output_dir)

# Process bug data
print("Processing bug data")
bug_dir = os.path.join(local_root, "bug_reports/")
for subdir, dirs, files in os.walk(root_folder):
    for dir in dirs:
        project_dir = os.path.join(root_folder, dir)
        print("Processing bug data from : "+project_dir)
        process_bug_data.process_folders(project_dir, bug_dir)

# if os.path.exists("results.zip"):
#     shutil.rmtree("results.zip")
# shutil.make_archive("results", 'zip', project_cleanup.backup_results_path)
# if os.path.exists("G:/My Drive/Education/ETS/Master's/Courses/MGL843/Collab/results.zip"):
#     shutil.rmtree("G:/My Drive/Education/ETS/Master's/Courses/MGL843/Collab/results.zip")
# shutil.copy("results.zip", "G:/My Drive/Education/ETS/Master's/Courses/MGL843/Collab")

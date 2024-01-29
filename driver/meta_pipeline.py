import importlib
import os
import shutil
import sys
sys.path.append('D:/dev/ETS/mgl843/SZZUnleashed/')
from entree import project_crawler
from entree import project_cleanup
from driver import pipeline
import time

ACTUAL_RESULTS_COUNT = 0
NEEDED_RESULTS_COUNT = 100
BLACKLIST = ["apollo-client","lobe-chat", "kibana", "vee-validate"]

page = 11
while ACTUAL_RESULTS_COUNT < NEEDED_RESULTS_COUNT+1:
    # Crawl projects to throw in pipeline
    print("Looking for repositories...")
    repositories = project_crawler.search_github_repositories(project_crawler.QUERY, page=page)
    project_crawler.write_to_csv(repositories, BLACKLIST)
    print("Added repositories!")

    # Run pipeline for batch of projects
    print("Running bug analysis + Pharo pipeline...")
    pipeline.run_pipeline()
    print("done running bug analysis + Pharo pipeline...")

    # Prepare results
    time.sleep(2.5)
    print("Cleaning up results...")
    project_cleanup.cleanup_results()
    ACTUAL_RESULTS_COUNT = len(next(os.walk(project_cleanup.backup_results_path))[1])
    page+=1
    print(f"Found {ACTUAL_RESULTS_COUNT} coherent results...")

if os.path.exists("results.zip"):
    shutil.rmtree("results.zip")
shutil.make_archive("results", 'zip', project_cleanup.backup_results_path)
if os.path.exists("G:/My Drive/Education/ETS/Master's/Courses/MGL843/Collab/results.zip"):
    shutil.rmtree("G:/My Drive/Education/ETS/Master's/Courses/MGL843/Collab/results.zip")
shutil.copy("results.zip", "G:/My Drive/Education/ETS/Master's/Courses/MGL843/Collab")

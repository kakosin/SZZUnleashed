import importlib
import os
import shutil
import sys
import time
sys.path.append('.')
from entree import project_crawler, project_cleanup

ACTUAL_RESULTS_COUNT = 0
NEEDED_RESULTS_COUNT = 1
BLACKLIST = ["apollo-client","lobe-chat", "kibana", "vee-validate","misskey", "keystone"]

page = 1
per_page = 5

def setup_data():
    # Run this section in a Docker environment
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

import importlib
import os
import shutil
import sys
import time
sys.path.append('.')
from entree import project_crawler, project_cleanup
import pipeline
from dotenv import load_dotenv
load_dotenv('token.env')

def setup_data():
    BLACKLIST = ["apollo-client","lobe-chat", "kibana", "vee-validate","misskey", "keystone", "BuilderIO", "wechaty", "web3.js"]
    ACTUAL_RESULTS_COUNT = 0
    NEEDED_RESULTS_COUNT = int(os.getenv('NEEDED_RESULTS'))
    page = 1
    per_page = int(os.getenv('RESULTS_PER_PAGE'))
    root_folder = "sortie/results"

    # Run this section in a Docker environment
    while ACTUAL_RESULTS_COUNT < NEEDED_RESULTS_COUNT:
        # Crawl projects to throw in pipeline
        print("Looking for repositories...")
        repositories = project_crawler.search_github_repositories(project_crawler.QUERY, page=page, per_page=per_page)
        project_crawler.write_to_csv('./entree/Projects.csv', repositories, BLACKLIST)
        project_crawler.write_to_csv('./entree/AllProjects.csv', repositories, BLACKLIST, 'a')
        print("Added repositories!")

        # Run pipeline for batch of projects
        print("Running bug analysis + Pharo pipeline...")
        pipeline.run_szz_pipeline()
        print("done running bug analysis + Pharo pipeline...")

        # Prepare results
        time.sleep(10)

        # project_cleanup.cleanup_results(root_folder, sortie_results)
        ACTUAL_RESULTS_COUNT = len(os.listdir(root_folder)) 
        print(os.listdir(root_folder))
        #len(next(os.walk(project_cleanup.backup_results_path))[1])
        page+=1
        print(f"Found {ACTUAL_RESULTS_COUNT} coherent results...")

setup_data()

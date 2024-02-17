import os
import json
import csv

def process_bug_pairs(commits_file_path, bug_pairs_file_path):
    with open(bug_pairs_file_path, 'r', encoding='utf-8') as f:
        bug_pairs = json.load(f)

    with open(commits_file_path, 'r', encoding='utf-8') as f:
        commits = json.load(f)

    bug_introducing_commits = {pair[0] for pair in bug_pairs}

    bug_files = {}
    non_bug_files = {}

    for commit_id, commit_data in commits.items():
        for file_path in commit_data['changes']:
            file_name = os.path.basename(file_path)  
            if commit_id in bug_introducing_commits:
                bug_files[file_name] = 1
            else:
                non_bug_files[file_name] = 0

    all_files = {**bug_files, **non_bug_files}

    return all_files

def save_to_csv(file_data, csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['file_name', 'bug_indicator'])  
        for file_name, bug_indicator in file_data.items():
            writer.writerow([file_name, bug_indicator])

def process_folders(root_folder, bug_reports_dir):
    if not os.path.exists(bug_reports_dir):
        os.makedirs(bug_reports_dir)
        
    for subdir, dirs, files in os.walk(root_folder):
        commits_file_path = None
        bug_pairs_file_path = None

        for file in files:
            if file == 'commits.json':
                commits_file_path = os.path.join(subdir, file)
            elif file == 'fix_and_introducers_pairs.json':
                bug_pairs_file_path = os.path.join(subdir, file)

        if commits_file_path and bug_pairs_file_path:
            all_files = process_bug_pairs(commits_file_path, bug_pairs_file_path)
            
            project_name = os.path.basename(subdir)
            
            project_dir = os.path.join(bug_reports_dir, project_name)
            if not os.path.exists(project_dir):
                os.makedirs(project_dir)
            
            csv_file_path = os.path.join(project_dir, 'file_bug_indicators.csv')
            save_to_csv(all_files, csv_file_path)

# root_folder = 'modeled_results'
# process_folders(root_folder)

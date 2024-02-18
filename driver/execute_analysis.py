import os
import sys
sys.path.append('.')
from driver import model_famix, pharo_analysis, project_code_analyzer, process_bug_data

def run():
    if not os.path.exists("artifacts/"):
        os.mkdir("artifacts")
    print("Producing ts2famix models...")
    model_filepaths = model_famix.produce_model()

    # Pharo analysis
    print("Loading model in Pharo")
    # root_folder = "sortie/backup_results/"
    # if not os.path.exists("artifacts/metrics/"):
    #     os.mkdir("artifacts/metrics/")
    # for subdir, dirs, files in os.walk(root_folder):
    #     for dir in dirs:
    #         project_dir = os.path.join(root_folder, dir)
    #         model_filepath = os.path.join(project_dir, dir+"_ts2famix.json")
    #         if os.path.exists(model_filepath):
    #             metrics_folder = f"metrics/{dir}/"
    #             if not os.path.exists(metrics_folder):
    #                 os.mkdir(metrics_folder)
    #             print("Producing pharo analysis for: "+model_filepath)
    #             pharo_analysis.analyse_model(model_filepath, metrics_folder)

    # Analyze SZZ JSON files
    print("Analysing SZZ JSON files")
    root_folder = "sortie/backup_results/"
    filenames = ['annotations.json','fix_and_introducers_pairs.json','commits.json']
    output_dir = "artifacts/analysis/"
    for subdir, dirs, files in os.walk(root_folder):
        for dir in dirs:
            project_dir = os.path.join(root_folder, dir)
            model_filepath = os.path.join(project_dir, dir+"_ts2famix.json")
            if os.path.exists(model_filepath):
                print("Analysing model: "+model_filepath)
                project_code_analyzer.process_json_file(model_filepath, output_dir)

    # Process bug data
    print("Processing bug data")
    bug_dir = "artifacts/bug_reports/"
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

run()
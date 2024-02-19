import os
import sys
sys.path.append('.')
sys.path.append("D:\dev\ETS\mgl843\SZZUnleashed")
from driver import model_famix, pharo_analysis, project_code_analyzer, process_bug_data, generate_project_files_list, project_metrics_analyzer, project_metrics_correlation_analysis

root_folder = "sortie/backup_results/"
git_folder_path = "sortie/git/"
artifacts_folder = "artifacts/"

def run():
    if not os.path.exists(artifacts_folder):
        os.mkdir(artifacts_folder)
    print("Producing ts2famix models...")
    model_famix.produce_model(root_folder, git_folder_path)

    # PHASE 1
    # Generate project files
    print("Generate project files")
    generate_project_files_list.main(git_folder_path, root_folder)

    # Process bug data
    print("Processing bug data")
    process_bug_data.main(root_folder)
    # bug_dir = os.path.join(artifacts_folder,"bug_reports/")
    # for subdir, dirs, files in os.walk(root_folder):
    #     for dir in dirs:
    #         project_dir = os.path.join(root_folder, dir)
    #         print("Processing bug data from : "+project_dir)
    #         process_bug_data.main(project_dir, bug_dir)

    # Analyze SZZ JSON files
    print("Analysing SZZ JSON files")
    # output_dir =  os.path.join(artifacts_folder,"analysis/")
    for subdir, dirs, files in os.walk(root_folder):
        for dir in dirs:
            project_dir = os.path.join(root_folder, dir)
            model_filepath = os.path.join(project_dir, dir+"_ts2famix.json")
            if os.path.exists(model_filepath):
                project_code_analyzer.traiter_fichier_json(model_filepath, dir)

    # PHASE 2
    # Pharo analysis
    # This is needed
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

    # Produce metrics
    print("Produce metrics files")
    project_metrics_analyzer.main(root_folder)

    # PHASE 3
    # Produce correlation
    print("Produce correlation")
    project_metrics_correlation_analysis.run()

    # if os.path.exists("results.zip"):
    #     shutil.rmtree("results.zip")
    # shutil.make_archive("results", 'zip', project_cleanup.backup_results_path)
    # if os.path.exists("G:/My Drive/Education/ETS/Master's/Courses/MGL843/Collab/results.zip"):
    #     shutil.rmtree("G:/My Drive/Education/ETS/Master's/Courses/MGL843/Collab/results.zip")
    # shutil.copy("results.zip", "G:/My Drive/Education/ETS/Master's/Courses/MGL843/Collab")

run()
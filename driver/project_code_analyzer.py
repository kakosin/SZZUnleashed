import os
import json
import csv

def process_json_file(json_file_path, output_dir):
    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    filtered_data = [item for item in json_data if item.get('FM3') == 'FamixTypeScript.Class']
    fields = ['fileName', 'name', 'methods']
    project_name = os.path.splitext(os.path.basename(json_file_path))[0]

    project_output_dir = os.path.join(output_dir, project_name)
    if not os.path.exists(project_output_dir):
        os.makedirs(project_output_dir)

    csv_file_path = os.path.join(project_output_dir, 'output.csv')
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()

        for item in filtered_data:
            row = {}
            for field in fields:
                if field == 'fileName' and 'fullyQualifiedName' in item:
                    fully_qualified_name = item['fullyQualifiedName']
                    filename_with_extension = fully_qualified_name.split('"')[-2]
                    filename = filename_with_extension.split('/')[-1].split('\\')[-1]
                    row[field] = filename
                elif field in item:
                    if isinstance(item[field], list):
                        row[field] = ', '.join([str(i) for i in item[field]])
                    else:
                        row[field] = item[field]
                else:
                    row[field] = ''
            writer.writerow(row)


def process_folders(root_folder, filenames, output_dir):
    for subdir, dirs, files in os.walk(root_folder):
        for file in files:
            if file in filenames:
                json_file_path = os.path.join(subdir, file)
                process_json_file(json_file_path, output_dir)


# root_folder = 'modeled_results'
# output_dir = 'processed_projects'
# process_folders(root_folder, filenames, output_dir)

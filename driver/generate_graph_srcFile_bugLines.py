import os
import pandas as pd
import matplotlib.pyplot as plt

def prepare_data_for_graph(projectPath, csv_file):
    df = pd.read_csv(os.path.join(projectPath, csv_file), delimiter=',')
    df['bug_fix_lines_count'] = df['bug_fix_lines'].apply(lambda x: len(eval(x)))
    data = df.groupby('source_file')['bug_fix_lines_count'].sum().to_dict()
    return data

def generate_graph(data, output_file):
    plt.figure(figsize=(10, 6))
    plt.barh(list(data.keys()), list(data.values()), color='skyblue')
    plt.xlabel('Nombre de lignes introductrices de bogues')
    plt.ylabel('Fichier source')
    plt.title('Nombre de lignes introductrices de bogues par fichier source')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()

def main(relativePath):
    projects = os.listdir(relativePath)
    for project in projects:
        projectPath = os.path.join(relativePath, project)
        if os.path.isdir(projectPath):
            csv_file = 'input_pharo_lines_only.csv'
            data = prepare_data_for_graph(projectPath, csv_file)
            output_file = os.path.join(projectPath, 'graph_srcFile_bugLines.png')
            generate_graph(data, output_file)

if __name__ == "__main__":
    relativePath= "sortie/results"
    main(relativePath)

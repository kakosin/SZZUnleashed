import matplotlib.pyplot as plt
def generate_graph(data, output_file):
    plt.figure(figsize=(10, 6))
    plt.barh(list(data.keys()), list(data.values()), color='skyblue')
    plt.xlabel('Nombre de lignes introductrices de bogues')
    plt.ylabel('Fichier source')
    plt.title('Nombre de lignes introductrices de bogues par fichier source')
    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()
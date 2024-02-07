import subprocess

vm_path = r"C:/Users/cjpin/Documents/Pharo/vms/100-x64/Pharo.exe"
Pharo_path = r"C:/Users/cjpin/Documents/Pharo/images/mgl843/mgl843.image"
# local_root = r"D:/dev/ETS/mgl843/SZZUnleashed"
# command_pharo_ro = f"SZZImporter findFilesChangedByBugfixesFrom: '{local_root}/sortie/results/DOSSIER_NAME/annotations.json' to: 'YOUR_CSV_VARIABLE_HERE'"

# command_pharo = command_pharo_ro.replace('YOUR_CSV_VARIABLE_HERE', csv_path).replace('DOSSIER_NAME', f"{github_owner}__{github_repo}")

# Création de la commande complète
# Pharo.exe path\to\your\Pharo.image eval --save "path\to\your\MyScript.st"

# Load metamodel: done manually on image, need to do once
# Load model: Pharo.exe C:\Pharo\Pharo.image eval --save "Metacello new baseline: 'MyProject'; repository: 'filetree://C:/Projects/MyProject/source'; load."



# Load Model
command_pharo_model = fr'Metacello new baseline: CC; repository: filetree://C:/Users/cjpin/dev/mgl843/SZZUnleashed/entree/antvis__G2.json"; load.'
command_load_model = fr'"{vm_path}" "{Pharo_path}" eval --save "{command_pharo_model}"'

# CC
# command_pharo_cc = "C:\Users\cjpin\dev\mgl843\SZZUnleashed\smalltak_scripts\cc.st"
# command_analyse_cc = fr'"{vm_path}" --headless "{Pharo_path}" eval --save"{command_pharo_cc}"'

# Exécution de la commande dans le terminal Windows ou PowerShell
print("modèle Pharo en cours...")
print("exécution de la commande pharo suivante",command_load_model)
subprocess.run(command_load_model, shell=True)
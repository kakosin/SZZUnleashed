import subprocess

vm_path = r"C:/Users/Carlos/Documents/Pharo/vms/100-x64/Pharo.exe"
Pharo_path = r"C:/Users/Carlos/Documents/Pharo/images/mgl843/mgl843.image"
model_load_st = r"D:/dev/ETS/mgl843/SZZUnleashed/driver/model_load.st"
model_analyse_st = r"D:/dev/ETS/mgl843/SZZUnleashed/driver/model_analyse.st"

# Load Model
def load_model(model_path):
    command_load_model = fr'"{vm_path}" "{Pharo_path}" st {model_load_st} "{model_path}"'
    subprocess.run(command_load_model, shell=True)

def analyse_model(model_path, metrics_folder):
    command_analyse_model = fr'"{vm_path}" "{Pharo_path}" st {model_analyse_st} "{model_path}" "{metrics_folder}"'
    subprocess.run(command_analyse_model, shell=True)

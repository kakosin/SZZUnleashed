import subprocess

vm_path = r"C:/Users/cjpin/Documents/Pharo/vms/100-x64/Pharo.exe"
Pharo_path = r"C:/Users/cjpin/Documents/Pharo/images/mgl843/mgl843.image"
model_load_st = r"C:/Users/cjpin/dev/mgl843/SZZUnleashed/driver/model_load.st"

# Load Model
def load_model(model_path):
    command_load_model = fr'"{vm_path}" "{Pharo_path}" st "C:/Users/cjpin/dev/mgl843/SZZUnleashed/driver/model_load.st" {model_path}'
    subprocess.run(command_load_model, shell=True)

load_model('C:/Users/cjpin/dev/mgl843/SZZUnleashed/model_g2.json')
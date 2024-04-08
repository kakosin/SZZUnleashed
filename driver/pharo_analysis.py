import subprocess
import os
from dotenv import load_dotenv
load_dotenv('dev.env')
PHARO_PATH = os.getenv('PHARO_PATH')
PHARO_IMAGE = os.getenv('PHARO_IMAGE')
PROJECT_PATH = os.getenv('PROJECT_PATH')

vm_path = PHARO_PATH
Pharo_path = PHARO_IMAGE
model_load_st = os.path.join(PROJECT_PATH, "driver/model_load.st")
model_analyse_st = os.path.join(PROJECT_PATH, "driver/model_analyse.st")

# Load Model
def load_model(model_path):
    command_load_model = fr'"{vm_path}" "{Pharo_path}" st {model_load_st} "{model_path}"'
    subprocess.run(command_load_model, shell=True)

def analyse_model(model_path, metrics_folder):
    command_analyse_model = fr'"{vm_path}" "{Pharo_path}" st {model_analyse_st} "{model_path}" "{metrics_folder}"'
    try:
        subprocess.run(command_analyse_model, shell=True)
    except subprocess.TimeoutExpired as e:
        return

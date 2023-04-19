import os
from  pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name = "signLanguage"

list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    "docs/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/traning_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/traning_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "template/index.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for file in list_of_files:
    filepath = Path(file)

    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info(f"Creating empty file {filename}")

    else:
        logging.info(f"{filename} already exist")
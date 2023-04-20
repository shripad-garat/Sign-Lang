import os,sys
from dataclasses import dataclass
from datetime import datetime
from  signLanguage.constant.traning_pipeline  import *
from signLanguage.exception import SignException

TIMESTAMP:str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACT_DIR = "artifacts"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_DIR_NAME= "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"

DATA_DOWNLOAD_URL = "https://github.com/entbappy/Branching-tutorial/blob/master/Sign_language_data.zip?raw=true"

"""
Data Validation related constant """
DATA_VALIDATION_DIR:str = "data_validation"
VALIDATION_STATUS_FILE_PATH:str = "status.txt"
REQUIRE_FILE_LIST:str = ["train","test","data.yaml"]




@dataclass
class TraningPipelineConfig:
    try:
        artifact_dir:str = os.path.join(ARTIFACT_DIR,TIMESTAMP)

    except Exception as e:
        raise SignException(error_message=e,error_detail=sys)

traning_pipeline_config:TraningPipelineConfig = TraningPipelineConfig()

@dataclass
class DataIngestionConfig:
    try:
        data_ingestion_dir:str = os.path.join(
            traning_pipeline_config.artifact_dir,DATA_INGESTION_DIR_NAME
        )        
        feature_store_file_path:str = os.path.join(
            data_ingestion_dir,DATA_INGESTION_FEATURE_STORE_DIR
        )  
        data_download_url:str = DATA_DOWNLOAD_URL
    except Exception as e:
        raise SignException(error_message=e,error_detail=sys)

@dataclass
class DataValidationConfig:
    try:
        data_validation_dir:str = os.path.join(
            traning_pipeline_config.artifact_dir,DATA_VALIDATION_DIR
        )

        validation_status_file_path = os.path.join(
            data_validation_dir,VALIDATION_STATUS_FILE_PATH
        )

        reuired_file_list = REQUIRE_FILE_LIST

    except Exception as e:
        raise SignException(e,sys)
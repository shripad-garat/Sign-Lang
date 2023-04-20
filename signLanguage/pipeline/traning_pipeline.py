import os,sys
from signLanguage.logger import logging
from signLanguage.exception import SignException
from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.entity.config_entity import DataIngestionConfig,DataValidationConfig
from signLanguage.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from signLanguage.components.data_validation import DataValidation

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()

    
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestrion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestrion_artifact = data_ingestrion.initiate_data_ingestion()
            return data_ingestrion_artifact

        except Exception as e: 
            raise SignException(e,sys)
        
    
    def start_data_validation(self,data_ingestion_artifact)->DataValidationArtifact:
        try:
            data_validation = DataValidation(data_ingestion_artifact= data_ingestion_artifact,data_validation_config=self.data_validation_config)
            data_validation_artifact = data_validation.inicated_data_validation()
            logging.info("Performing the data validation")
            return data_validation_artifact
        except Exception as e:
            raise SignException(e,sys)
    

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            print(data_validation_artifact)

        except Exception as e:
            raise SignException(e,sys)    
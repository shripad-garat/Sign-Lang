from signLanguage.logger import logging
from signLanguage.exception import SignException
import os,sys
import shutil
from signLanguage.entity.config_entity import DataValidationConfig
from signLanguage.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact

class DataValidation:
    def __init__(
            self,
            data_ingestion_artifact:DataIngestionArtifact,
            data_validation_config:DataValidationConfig
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config

        except Exception as e:
            raise SignException(e,sys)
        
    def validate_all_files_exist(self)->bool:
        try:
            validation_status = None

            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)

            for f in all_files:
                if f not in self.data_validation_config.reuired_file_list:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir,exist_ok=True)
                    with open(self.data_validation_config.validation_status_file_path,'w') as file:
                        file.write(f"Validation status: {validation_status} for file {f}")

                else:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir,exist_ok=True)
                    with open(self.data_validation_config.validation_status_file_path,'w') as file:
                        file.write(f"Validation status: {validation_status} for file {f}")

            return validation_status
        except Exception as e:
            raise SignException(e,sys)


    def inicated_data_validation(self):
        try:
            validation_status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(
                validation_status=validation_status
            )
            logging.info(f"The data validation is completed and returning the data validation artiofact")

            return data_validation_artifact

        except Exception as e:
            raise SignException(e,sys)
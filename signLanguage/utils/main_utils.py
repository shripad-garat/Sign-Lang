import os
import sys
import yaml
import base64

from signLanguage.logger import logging
from signLanguage.exception import SignException

def read_yaml_report(file_path:str)->dict:
    try:
        with open(file_path,"rb") as file_read:
            logging.info("Reading the ymail file")
            return yaml.safe_load(file_read)

    except Exception as e:
        raise SignException(e,sys)
    
def write_yaml_report(file_path,data):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,"w") as file_writer:
            yaml.dump(data,file_writer)

    except Exception as e:
        raise SignException(e,sys)
    

def decodeImg(imgstring,fileName):
    imgdata = base64.b64decode(imgstring)
    with open("./data/"+fileName,"wb") as f:
        f.write(imgdata)
        f.close


def encodeImgIntoBase64(croppedImagePath):
    with open(croppedImagePath,"rb") as f:
        return base64.b64encode(f.read())
    

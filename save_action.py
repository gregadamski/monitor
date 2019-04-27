import cv2
import time
from time import gmtime, strftime


class SaveFileAction:
    
    def __init__(self, log_directory):
        self.log_directory = log_directory

    def log_action(self, context_img, detected_img, meta):
        file_name = time.strftime('%Y_%m_%d_%H_%M_%S')
        
        mm = "_".join([el[1] for el in detected_img])
        file_name = f"{file_name}_{meta}_{mm}.jpg" 
        
        cv2.imwrite(f"{self.log_directory}/{file_name}", context_img)

    
from darknet_detector import DarknetDetector

import cv2

from opencv_dnn_detector import OpenCvDnnDetector
from save_action import SaveFileAction

from util import *
 
darknetPath = "/Users/gregadamski/Documents/programming/darknet/darknet"
basePath = "/Users/gregadamski/Documents/programming/video"

dataPath = f"{basePath}/data"
cfgPath = f"{basePath}/cfg"
weightsPath = f"{basePath}/weights"
classesFile = f'{dataPath}/coco.names'
dataFile = f'{cfgPath}/coco.data'


weightsFile = f'{weightsPath}/yolov3-tiny.weights'
cfgFile = f'{cfgPath}/yolov3-tiny.cfg'

# weightsFile = f'{weightsPath}/yolov3.weights'
# cfgFile = f'{cfgPath}/yolov3.cfg'

# vcap = cv2.VideoCapture("rtsp://admin:12345@192.168.86.49/Streaming/Channels/101/")
# vcap = cv2.VideoCapture(0)
vcap = cv2.VideoCapture('samochody.mp4')

detector = OpenCvDnnDetector(weightsFile, cfgFile, classesFile)
logger = SaveFileAction('/Users/gregadamski/Documents/camera/')


# darknet detector is very bad on a CPU on a mac
# detector = DarknetDetector(weightsFile, cfgFile, dataFile)



print(f"Resolution : {vcap.get(3)} {vcap.get(4)}")
i = 0
while(True):
    ret, frame = vcap.read()
   
    if ret:
        i = i + 1

        imS = cv2.resize(frame, (640, 480))  
 
        if (i % 25 == 0):
            ret = detector.findObjects(imS)
            
            detected = []

            for pp in ret:
                print(f"{pp[0]}  -  {pp[2]}")
                rect = pp[2]
                box = get_bounding_box(rect)
                annotateImage(imS, box, str(pp[0]))
                cv2.imshow('VIDEO', imS)
                detected.append((get_detected_image(imS, box), str(pp[0])))

            
            if (len(detected) > 0):
                logger.log_action(imS,  detected, "")

            # print(ret)
            # cv2.imshow('VIDEO', imS)
            # cv2.imwrite(f'img_CV4_{i}.jpg', imS, [int(cv2.IMWRITE_JPEG_QUALITY), 90])


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vcap.release()
cv2.destroyAllWindows()

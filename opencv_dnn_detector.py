import cv2
import numpy as np

class OpenCvDnnDetector:

    def __init__(self, weightsFile, cfgFile, labelsFile):
        self.cv2net = cv2.dnn.readNet(weightsFile, cfgFile)
        with open(labelsFile, 'r') as f:
            self.classes = [line.strip() for line in f.readlines()]



    def get_output_layers(self):
        layer_names = self.cv2net.getLayerNames()
        output_layers = [layer_names[i[0] - 1] for i in self.cv2net.getUnconnectedOutLayers()]
        return output_layers

    def findObjects(self, img):
        Width = img.shape[1]
        Height = img.shape[0]
        scale = 0.00392
        blob = cv2.dnn.blobFromImage(img, scale, (640,480), (0,0,0), True, crop=False)

        self.cv2net.setInput(blob)

        outs = self.cv2net.forward(self.get_output_layers())

        class_ids = []
        confidences = []
        boxes = []
        conf_threshold = 0.5
        nms_threshold = 0.4
        combined = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # print(detection)
                    center_x = int(detection[0] * Width)
                    center_y = int(detection[1] * Height)
                    w = int(detection[2] * Width)
                    h = int(detection[3] * Height)
                    x = center_x - w / 2
                    y = center_y - h / 2
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])
                    cc = []
                    cc.append(str(self.classes[class_id]))
                    cc.append(confidence)
                    cc.append([center_x, center_y, w, h])
                    combined.append(cc)
        indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
        print(combined)
        return combined


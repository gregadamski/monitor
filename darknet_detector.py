from darknet import *

class DarknetDetector:

    def __init__(self, weightsFile, cfgFile, labelsFile):
        self.net = load_net(cfgFile.encode('utf-8'), weightsFile.encode('utf-8'), 0)
        self.meta = load_meta(labelsFile.encode('utf-8'))


    def findObjects(self, img):
        return detect2(self.net, self.meta, img)
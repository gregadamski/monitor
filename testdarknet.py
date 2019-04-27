from darknet import *

darknetPath = "/Users/gregadamski/Documents/programming/darknet/darknet"

net = load_net(f'{darknetPath}/cfg/yolov3.cfg'.encode('utf-8'), f'{darknetPath}/yolov3.weights'.encode('utf-8'), 0)
meta = load_meta(f'{darknetPath}/cfg/coco.data'.encode('utf-8'))

imgPath = "/Users/gregadamski/Documents/programming/video/img_CV3_1400.jpg"

r = detect(net, meta, imgPath.encode('utf-8'))
print(r)
darknetPath = "/Users/gregadamski/Documents/programming/darknet/darknet"


print("AA")
# detector = Detector(darknetPath,
#                     f'{darknetPath}/cfg/coco.data',
#                     f'{darknetPath}/cfg/yolov3.cfg',
#                     f'{darknetPath}/yolov3.weights')


print("BB")

# results = detector.detect(f'{darknetPath}/data/dog.jpg')

# print(results)

import cv2


def get_bounding_box(detected):
    # coordinates returned as center of the box + width and height
    x = int(detected[0])
    y = int(detected[1])
    w = int(detected[2])
    h = int(detected[3])
    return ((int(x - w / 2),int(y - h / 2)),(int(x + w/2), int(y + w/2)))
 

def get_detected_image(img, box):
    x = box[0][0]
    y = box[0][1]
    w = box[1][0] - x
    h = box[1][1] - y
    
    print(f"{x} {y} {w} {h}")
    return img[y:y+h, x:x+w]


def annotateImage(img, box, detected):
    cv2.rectangle(img, box[0], box[1] ,(0,255,0),3)

    font = cv2.FONT_HERSHEY_SIMPLEX
    print(box[0][0])
    print(box[0][1])
    cv2.putText(img,detected,box[0], font, 1,(255,255,255),2,cv2.LINE_AA)
import cv2
import time

vcap = cv2.VideoCapture("rtsp://admin:12345@192.168.86.49/Streaming/Channels/101/")

drawing = False # true if mouse is pressed
mode = True
ret, frame = vcap.read()

ix,iy = -1,-1
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    print("AAASSSSSSSS")
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(frame,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(frame,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(frame,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(frame,(x,y),5,(0,0,255),-1)
    #cv2.imshow('image', frame)

cv2.setMouseCallback('image',draw_circle)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

ret = False
while(True):
    ret, frame = vcap.read()
    if ret:
        cv2.imshow('image', frame)
        break

while(True):
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

time.sleep(100000)
import cv2
import img


def drawBox(img,bbox):
x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]),int(bbox[3])
cv2.rectangle(img, (x,y), ((x+w), (y+h)), (255,0,255), 3,1)
cv2.putText(img, "Rastreando", (75,98),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0),2)
import cv2
import numpy as np

# Function
               #event : right click , left click , double click
               # x,y : mouse position
               # flags and param additional filled automatically
            
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),thickness=-1)
        
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),thickness=-1)

 #
cv2.namedWindow(winname='drawing')
cv2.setMouseCallback('drawing',draw_circle)


# Showing Images in Open Cv window

img = np.zeros((512,512,3))

while True:
    
    cv2.imshow('drawing',img)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
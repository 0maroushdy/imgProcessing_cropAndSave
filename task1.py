import cv2
import numpy as np

cropping = False
start_point = (-1, -1)
end_point = (-1, -1)
image = cv2.imread('bunny.jpeg') 
clone = image.copy()

def crop_image(event, x, y, flags, param):
    global cropping, start_point, end_point, clone
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cropping = True
        start_point = (x, y)
    
    elif event == cv2.EVENT_MOUSEMOVE and cropping:
        end_point = (x, y)
        temp = clone.copy()
        cv2.rectangle(temp, start_point, end_point, (0, 255, 0), 2)
        cv2.imshow("Crop Image", temp)
    
    elif event == cv2.EVENT_LBUTTONUP:
        cropping = False
        end_point = (x, y)
        cv2.rectangle(clone, start_point, end_point, (0, 255, 0), 2)
        cv2.imshow("Crop Image", clone)
        
        x1, y1 = min(start_point[0], end_point[0]), min(start_point[1], end_point[1])
        x2, y2 = max(start_point[0], end_point[0]), max(start_point[1], end_point[1])
        cropped = image[y1:y2, x1:x2]
        cv2.imwrite("cropped_image.jpg", cropped)
        print("Cropped image saved as 'cropped_image.jpg'")

cv2.namedWindow("Crop Image")
cv2.setMouseCallback("Crop Image", crop_image())
cv2.imshow("Crop Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ----------------- <<< Task 1 >>> -----------------
point1 = None
point2 = None


def getPoints(event, x, y, flags, param):
    global point1, point2, image

    if event == cv2.EVENT_LBUTTONDOWN:
        if point1 is None:
            # 1st Point ----------------------------------
            point1 = (x, y)
            print(f"Point 1: {point1}")
        elif point2 is None:
            # 2nd Point ----------------------------------
            point2 = (x, y)
            print(f"Point 2: {point2}")

            # Drawing a rect containgin the cropped area ---
            cv2.rectangle(image, point1, point2, (255, 0, 0), 2)
            cv2.imshow('Image', image)

            # Crop and save --------------------------------
            x1, y1 = min(point1[0], point2[0]), min(point1[1], point2[1])
            x2, y2 = max(point1[0], point2[0]), max(point1[1], point2[1])
            croppedImage = theImg[y1:y2, x1:x2]
            cv2.imwrite("croppedImage.jpg", croppedImage)
            print("Cropped image saved as 'croppedImage.jpg'")

#-------- ** Load the image ** -----------------
imagePath = 'resrc/bunny.jpeg'  
theImg = cv2.imread(imagePath)
image = theImg.copy()

#-------- ** setting the prog window ** -----------------
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', getPoints)

#-------- ** Main running ** -----------------
while True:
    cv2.imshow('Image', image)
    key = cv2.waitKey(1)
    if key == 27:  # Exit when 'ESC' 
        break

cv2.destroyAllWindows()

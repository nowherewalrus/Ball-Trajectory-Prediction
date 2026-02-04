import cv2
import cvzone
from cvzone.ColorModule import ColorFinder
import numpy as np
import math

# Initialize video capture from a specified video file
cap = cv2.VideoCapture('vid (5).mp4')

# Initialize ColorFinder object to detect specific color ranges in the frame
myColorFinder = ColorFinder(False)

# HSV color range values to detect the target object (e.g., a ball)
hsvVals = {'hmin': 8, 'smin': 124, 'vmin': 13, 'hmax': 24, 'smax': 255, 'vmax': 255}

# Lists to store the X and Y positions of the detected object (e.g., ball)
posListX = []
posListY = []

# Generate a list of X values for curve prediction
listX = [item for item in range(0, 1300)]

# Flags to manage the state of the program
start = True
prediction = False

while True:

   if start:
       # Once 10 positions are recorded, stop the initial process
       if len(posListX) == 10: start = False

       # Capture a frame from the video
       success, img = cap.read()

       # Crop the frame to focus on the region of interest
       img = img[0:900, :]

       # Create copies of the original frame for different stages of processing
       imgPrediction = img.copy()
       imgResult = img.copy()

       # Detect the target object based on the HSV values
       imgBall, mask = myColorFinder.update(img, hsvVals)

       # Find contours of the detected object
       imgCon, contours = cvzone.findContours(img, mask, 200)

       # If a contour is detected, save its center position
       if contours:
           posListX.append(contours[0]['center'][0])
           posListY.append(contours[0]['center'][1])

       # If positions are recorded, perform curve fitting and draw the path
       if posListX:
           # Perform polynomial curve fitting on recorded positions
           if len(posListX) < 18:
               coff = np.polyfit(posListX, posListY, 2)

           # Draw circles on the detected object positions and connect them with lines
           for i, (posX, posY) in enumerate(zip(posListX, posListY)):
               pos = (posX, posY)
               cv2.circle(imgCon, pos, 10, (0, 255, 0), cv2.FILLED)
               cv2.circle(imgResult, pos, 10, (0, 255, 0), cv2.FILLED)

               # Draw lines connecting the detected positions
               if i == 0:
                   cv2.line(imgCon, pos, pos, (0, 255, 0), 2)
                   cv2.line(imgResult, pos, pos, (0, 255, 0), 2)
               else:
                   cv2.line(imgCon, (posListX[i - 1], posListY[i - 1]), pos, (0, 255, 0), 2)
                   cv2.line(imgResult, (posListX[i - 1], posListY[i - 1]), pos, (0, 255, 0), 2)

           # Draw the predicted trajectory using the fitted curve
           for x in listX:
               y = int(coff[0] * x ** 2 + coff[1] * x + coff[2])
               cv2.circle(imgPrediction, (x, y), 2, (255, 0, 255), cv2.FILLED)
               cv2.circle(imgResult, (x, y), 2, (255, 0, 255), cv2.FILLED)

           # Predict if the object (e.g., ball) will land in a basket
           if len(posListX) < 10:
               a, b, c = coff
               c = c - 593
               x = int((-b - math.sqrt(b ** 2 - (4 * a * c))) / (2 * a))
               prediction = 300 < x < 430

           # Display prediction result (Basket or No Basket)
           if prediction:
               cvzone.putTextRect(imgResult, "Basket", (50, 150), colorR=(0, 200, 0),
                                  scale=5, thickness=10, offset=20)
           else:
               cvzone.putTextRect(imgResult, "No Basket", (50, 150), colorR=(0, 0, 200),
                                  scale=5, thickness=10, offset=20)

       # Draw a reference line for the basket area
       cv2.line(imgCon, (330, 593), (430, 593), (255, 0, 255), 10)

       # Resize the result image for better display
       imgResult = cv2.resize(imgResult, (0, 0), None, 0.7, 0.7)

       # Show the result in a window
       cv2.imshow("imgCon", imgResult)

   # If the 's' key is pressed, restart the process
   key = cv2.waitKey(100)
   if key == ord("s") or key == ord('S'):
       start = True

   # Exit the loop if the ESC key is pressed
   if key == 27:
       break

# Release the video capture object and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()

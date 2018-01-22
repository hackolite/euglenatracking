import numpy as np
import cv2

params = cv2.SimpleBlobDetector_Params()
 
# Change thresholds
params.minThreshold = 10;
params.maxThreshold = 200;
 
# Filter by Area.
params.filterByArea = True
params.minArea = 150
 
# Filter by Circularity
#params.filterByCircularity = True
#params.minCircularity = 0.1
 
# Filter by Convexity
#params.filterByConvexity = True
params.minConvexity = 0.87
 
# Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.01





def detect(im):
    # Setup SimpleBlobDetector parameters.

    # Read image
    detector = cv2.SimpleBlobDetector_create(params)
    # Detect blobs.
    keypoints = detector.detect(im)
    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    
    try:
        print(keypoints[0].pt)
    except:
        pass

    # Show keypoints
    cv2.imshow("Keypoints", im_with_keypoints)


cap = cv2.VideoCapture('euglena.mp4')

# take first frame of the video
ret,frame = cap.read()

# setup initial location of window
# r,h,c,w - region of image
#           simply hardcoded the values
while(1):
    ret ,frame = cap.read()
    detect(frame)
    k = cv2.waitKey(60) & 0xff

cv2.destroyAllWindows()
cap.release()



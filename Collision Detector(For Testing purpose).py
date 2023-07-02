import cv2
import numpy as np
import time
import RPi.GPIO as GPIO
from picamera import PiCamera
from picamera.array import PiRGBArray

# Initialize the PiCamera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24
raw_capture = PiRGBArray(camera, size=camera.resolution)

# Initialize previous frame and collision flags
prev_frame = None
left_collision = False
right_collision = False
middle_collision = False

# Define the split areas for collision detection
height, width = camera.resolution
left_split = width // 3
right_split = width * 2 // 3

# Set up GPIO pins for left and right buzzers
GPIO.setmode(GPIO.BCM)
GPIO_LEFT_BUZZER = 17
GPIO_RIGHT_BUZZER = 22
GPIO.setup(GPIO_LEFT_BUZZER, GPIO.OUT)
GPIO.setup(GPIO_RIGHT_BUZZER, GPIO.OUT)

# Create windows for color and grayscale views

cv2.namedWindow("Grayscale View", cv2.WINDOW_NORMAL)

# Start capturing frames from the camera
for frame in camera.capture_continuous(raw_capture, format="bgr", use_video_port=True):
    # Convert the current frame to grayscale
    gray = cv2.cvtColor(frame.array, cv2.COLOR_BGR2GRAY)

    # Compute optical flow if previous frame exists
    if prev_frame is not None:
        flow = cv2.calcOpticalFlowFarneback(prev_frame, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        
        # Visualize the optical flow
        hsv = np.zeros_like(frame.array)
        hsv[..., 1] = 255
        mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
        hsv[..., 0] = ang * 180 / np.pi / 2
        hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
        cv2.imshow("Optical Flow", bgr)
        cv2.waitKey(1)
        
        # Calculate the magnitude of the optical flow for the split areas
        left_area = mag[:, :left_split]
        middle_area = mag[:, left_split:right_split]
        right_area = mag[:, right_split:]
        
        left_mag_mean = np.mean(left_area)
        middle_mag_mean = np.mean(middle_area)
        right_mag_mean = np.mean(right_area)
        
        # Check for collision based on the magnitude of the optical flow
        if left_mag_mean > 5:
            print("Collision detected at left area!")
            left_collision = True
        else:
            left_collision = False
        
        if middle_mag_mean > 5:
            print("Collision detected at middle area!")
            middle_collision = True
        else:
            middle_collision = False
        
        if right_mag_mean > 5:
            print("Collision detected at right area!")
            right_collision = True
        else:
            right_collision = False

        # Control the left and right buzzers based on collision flags
        GPIO.output(GPIO_LEFT_BUZZER, GPIO.HIGH if left_collision or middle_collision else GPIO.LOW)
        GPIO.output(GPIO_RIGHT_BUZZER, GPIO.HIGH if right_collision or middle_collision else GPIO.LOW)

    # Display the color and grayscale views
  
    cv2.imshow("Grayscale View", gray)

    # Wait for key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    # Set current frame as previous frame for next iteration
    prev_frame = gray
    
    # Clear the stream for the next frame
    raw_capture.truncate(0)

# Release the camera and close all windows
camera.close()
cv2.destroyAllWindows()

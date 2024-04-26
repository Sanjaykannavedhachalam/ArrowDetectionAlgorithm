'''import cv2
import numpy as np

# Function to detect arrow and show dimensions
def detect_arrow(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Thresholding
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Loop through contours
    for contour in contours:
        # Approximate polygonal curves
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # If contour has 7 vertices (assuming arrow shape)
        if len(approx) == 7:
            # Get bounding rectangle
            x, y, w, h = cv2.boundingRect(contour)
            
            # Draw bounding rectangle
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Show dimensions
            cv2.putText(image, f'Width: {w}px', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(image, f'Height: {h}px', (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Show image
            cv2.imshow('Detected Arrow', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

# Capture webcam feed
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    
    # Call function to detect arrow
    detect_arrow(frame)
    
    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()'''


'''
import cv2
import numpy as np

# Function to detect arrow and show dimensions
def detect_arrow(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Thresholding
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Loop through contours
    for contour in contours:
        # Approximate polygonal curves
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        
        # If contour has 7 vertices (assuming arrow shape)
        if len(approx) == 7:
            # Get bounding rectangle
            x, y, w, h = cv2.boundingRect(contour)
            
            # Draw bounding rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Show dimensions
            cv2.putText(frame, f'Width: {w}px', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(frame, f'Height: {h}px', (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Show frame with detected arrows
    cv2.imshow('Detected Arrows', frame)

# Capture webcam feed
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    
    # Call function to detect arrow
    detect_arrow(frame)
    
    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()

cv2.destroyAllWindows()
'''

'''
import cv2
import numpy as np

# Function to detect arrow and show dimensions
def detect_arrow(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Thresholding
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Loop through contours
    for contour in contours:
        # Approximate polygonal curves
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        
        # If contour has 3 vertices (triangle) and 4 vertices (rectangle)
        if len(approx) == 3 or len(approx) == 4:
            # Get bounding rectangle
            x, y, w, h = cv2.boundingRect(contour)
            
            # Draw bounding rectangle
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Show dimensions
            cv2.putText(frame, f'Width: {w}px', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.putText(frame, f'Height: {h}px', (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Show frame with detected arrows
    cv2.imshow('Detected Arrows', frame)

# Capture webcam feed
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()
    
    # Call function to detect arrow
    detect_arrow(frame)
    
    # Exit on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()
'''
'''
import cv2

# Open the default camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Find contours in the edge image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours
    for cnt in contours:
        # Approximate the contour to a polygon
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)

        # Check if the approximated polygon has 3 vertices (triangle) and 4 vertices (rectangle)
        if len(approx) == 3 or len(approx) == 4:
            # Draw the approximated polygon on the frame
            cv2.polylines(frame, [approx], True, (0, 255, 0), 2)

            # Calculate the dimensions of the approximated polygon
            x, y, w, h = cv2.boundingRect(approx)
            text = f"Width: {w} pixels, Height: {h} pixels"

            # Put the dimensions text on the frame
            cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 2)

    # Display the resulting frame
    cv2.imshow('Arrow Detection', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
'''


import cv2

# Function to detect arrow shape
def detect_arrow(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform edge detection
    edges = cv2.Canny(gray, 50, 150)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through the contours
    for contour in contours:
        # Approximate the contour to a polygon
        approx = cv2.approxPolyDP(contour, 0.03 * cv2.arcLength(contour, True), True)
        
        # If the contour has 7 vertices (combination of rectangle and triangle)
        if len(approx) == 7:
            # Calculate the area of the contour
            area = cv2.contourArea(contour)
            
            # If the area is large enough, consider it as an arrow
            if area > 1000:
                # Draw the contour and bounding rectangle
                cv2.drawContours(frame, [contour], 0, (0, 255, 0), 2)
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                
                # Show dimensions
                cv2.putText(frame, f'Width: {w}px', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                cv2.putText(frame, f'Height: {h}px', (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Display the frame with detected arrows
    cv2.imshow('Arrow Detection', frame)


# Open the default camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Call the function to detect arrow shape
    detect_arrow(frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()




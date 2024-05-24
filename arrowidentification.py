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

import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked

def draw_lines(img, lines):
    if lines is None:
        return
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 5)

def process_frame(frame):
    height, width = frame.shape[:2]
    
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Canny Edge Detection
    edges = cv2.Canny(blur, 50, 150)

    # Region of interest (only focus on bottom half of the image)
    roi_vertices = np.array([[
        (0, height),
        (width // 2 - 50, height // 2 + 60),
        (width // 2 + 50, height // 2 + 60),
        (width, height)
    ]], dtype=np.int32)

    cropped_edges = region_of_interest(edges, roi_vertices)

    # Hough Line Transform
    lines = cv2.HoughLinesP(
        cropped_edges,
        rho=2,
        theta=np.pi / 180,
        threshold=50,
        minLineLength=100,
        maxLineGap=50
    )

    # Draw the lines
    line_img = np.zeros_like(frame)
    draw_lines(line_img, lines)

    # Combine with original frame
    final_img = cv2.addWeighted(frame, 0.8, line_img, 1, 1)

    return final_img

# ---------- Main Program ----------

video_path = "road.mp4"  # Make sure road.mp4 is in the same folder

cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    final_frame = process_frame(frame)

    cv2.imshow("Lane Detection", final_frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


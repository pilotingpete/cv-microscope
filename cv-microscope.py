import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Video Feed Dimensions
    frame_height = frame.shape[0]
    frame_width = frame.shape[1]

    # BGR Color space
    blue = (255, 0, 0)
    white = (255, 255, 255)

    # Convert to grayscale.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Blur using 3 * 3 kernel.
    gray_blurred = cv2.blur(gray, (3, 3))

    # Apply Hough transform on the blurred image.
    detected_circles = cv2.HoughCircles(gray_blurred,
                                        cv2.HOUGH_GRADIENT, 1, minDist=600, param1=50,
                                        param2=30, minRadius=120, maxRadius=150)

    # Draw circles that are detected.
    if detected_circles is not None:

        # Convert the circle parameters a, b and r to integers.
        detected_circles = np.uint16(np.around(detected_circles))

        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]

            # Draw the circumference of the circle.
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2)

            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3)

            x_to_center = abs(a - int(frame_width/2))
            y_to_center = abs(b - int(frame_height/2))

            print(
                f'Center of detected circle is at x: {a}, y: {b} and is x: {x_to_center}, y: {x_to_center} from scope center.')

    # vertical line superimposed on microscope video feed.
    cv2.line(frame, pt1=(int(frame_width/2), 0),
             pt2=(int(frame_width/2), frame_height),
             color=blue, thickness=1, lineType=1)

    # horizontal line
    cv2.line(frame, pt1=(0, int(frame_height/2)),
             pt2=(frame_width, int(frame_height/2)),
             color=blue, thickness=1, lineType=1)

    # circle
    cv2.circle(frame, center=(int(frame_width/2), int(frame_height/2)),
               radius=25, color=blue, thickness=1, lineType=1)

    # circle
    cv2.circle(frame, center=(int(frame_width/2), int(frame_height/2)),
               radius=50, color=blue, thickness=1, lineType=1)

    # circle
    cv2.circle(frame, center=(int(frame_width/2), int(frame_height/2)),
               radius=100, color=blue, thickness=1, lineType=1)

    # Display the resulting frame
    cv2.imshow('frame', frame)
    # cv2.imshow('frame',gray_blurred)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

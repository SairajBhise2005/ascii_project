import cv2
import numpy as np

# ASCII characters from dark to light
ASCII_CHARS = "@$B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# Settings
FONT = cv2.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.4
THICKNESS = 1
CHAR_WIDTH = 10
CHAR_HEIGHT = 10


def resize_frame(frame, scale=0.2):
    height, width = frame.shape
    return cv2.resize(frame, (int(width * scale), int(height * scale)))


def frame_to_ascii(frame):
    ascii_image = []
    for row in frame:
        ascii_row = ""
        for pixel in row:
            index = int(pixel / 256 * len(ASCII_CHARS))
            ascii_row += ASCII_CHARS[index]
        ascii_image.append(ascii_row)
    return ascii_image


# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    small_frame = resize_frame(gray)

    ascii_frame = frame_to_ascii(small_frame)

    # Create black canvas
    canvas_height = len(ascii_frame) * CHAR_HEIGHT
    canvas_width = len(ascii_frame[0]) * CHAR_WIDTH
    ascii_canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

    # Draw ASCII text
    for i, row in enumerate(ascii_frame):
        for j, char in enumerate(row):
            cv2.putText(
                ascii_canvas,
                char,
                (j * CHAR_WIDTH, (i + 1) * CHAR_HEIGHT),
                FONT,
                FONT_SCALE,
                (255, 255, 255),
                THICKNESS,
                cv2.LINE_AA,
            )

    cv2.imshow("ASCII Camera", ascii_canvas)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# ASCII Art Webcam

## Description
This project is a real-time ASCII art generator that uses your webcam feed. It captures video frames, converts them to grayscale, and then maps pixel brightness to ASCII characters. The resulting ASCII art is rendered onto a canvas and displayed in a window.

## Tech Stack
- **Language**: Python 3
- **Libraries**:
    - **OpenCV (`opencv-python`)**: Used for capturing video from the webcam, image processing (grayscale conversion, resizing), and rendering text onto the image.
    - **NumPy (`numpy`)**: Used for efficient array manipulation and creating the blank canvas for the ASCII art.

## Installation

1.  **Clone or Download the Repository**:
    Ensure you have the `AsciiImage.py` and `requirements.txt` files in your project directory.

2.  **Install Dependencies**:
    Open your terminal or command prompt, navigate to the project directory, and run the following command to install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the Script**:
    Execute the Python script using the following command:

    ```bash
    python AsciiImage.py
    ```

2.  **Controls**:
    - The application will open a window titled "ASCII Camera".
    - Press **`t`** to toggle between the ASCII art view and the original webcam feed.
    - Press **`q`** on your keyboard to quit the application and close the window.

## How It Works
1.  **Capture**: The script captures a frame from the default webcam (index 0).
2.  **Grayscale**: The frame is converted to grayscale to simplify brightness calculations.
3.  **Resize**: The frame is resized to a smaller resolution to make the ASCII characters legible and fit on the screen.
4.  **ASCII Mapping**: Each pixel in the resized frame is mapped to an ASCII character based on its brightness value. Darker pixels get "denser" characters (like `@`, `$`), while lighter pixels get "lighter" characters (like `.`, ` `).
5.  **Rendering**: The characters are drawn onto a black canvas using OpenCV's `putText` function.
6.  **Display**: The final image is displayed in a window.

## Troubleshooting
-   **Webcam Not Found**: Ensure your webcam is connected and not being used by another application. If you have multiple cameras, you may need to change `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` or another index in the code.
-   **Missing Modules**: If you see an error like `ModuleNotFoundError: No module named 'cv2'`, make sure you have installed the dependencies using the `pip install` command mentioned above.

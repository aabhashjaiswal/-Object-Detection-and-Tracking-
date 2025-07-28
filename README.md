# Object-Detection-and-Tracking-

## Objective
Build a real-time object detection and tracking system with a simple graphical user interface (GUI) that uses a webcam to detect objects with YOLOv8 and track them uniquely using the SORT algorithm.

## Language
- Python 3.x

## Features
- Real-time object detection from webcam feed
- Object tracking with unique IDs using SORT algorithm
- Bounding boxes and tracking labels displayed on detected objects
- Simple GUI to start and stop detection
- Uses pre-trained YOLOv8 nano model (`yolov8n.pt`)
- Clean exit and resource release

## Folder Structure
```
Object-Detection-Tracking/
│
├── object_detection_gui.py # Main Python script with GUI and detection logic
├── sort.py # SORT tracking algorithm implementation
├── yolov8n.pt # Pre-trained YOLOv8 weights file
├── README.md # This documentation file
└── requirements.txt # Python dependencies (optional)
```


## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Webcam connected to your system

### Install dependencies
```bash
pip install ultralytics opencv-python numpy scikit-image filterpy

How to Run
Open terminal or command prompt and navigate to the project folder:

bash
Copy
Edit
cd "path_to_your_project_folder"
Run the GUI application:

bash
Copy
Edit
python object_detection_gui.py
Use the GUI:

Click Start Detection to begin real-time detection and tracking.

Click Stop Detection or close the windows to exit.

Sample Output
When running, a window displays the webcam video with:

Green bounding boxes around detected objects

Labels showing unique tracking IDs (e.g., "ID 1", "ID 2")

Smooth real-time tracking as objects move

Troubleshooting
Module not found errors: Make sure all dependencies are installed via pip.

Corrupted model file: Delete and re-download yolov8n.pt.

Camera issues: Check webcam connection and close other applications using it.

Performance: Running on CPU may be slow; GPU usage can improve speed.

References
Ultralytics YOLOv8

SORT Tracker

OpenCV

Tkinter

Future Improvements
Support video file input

Add more advanced tracking algorithms (e.g., Deep SORT)

Enhance GUI controls and features

GPU acceleration support

Add logging and analytics

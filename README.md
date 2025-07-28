# Object-Detection-and-Tracking-

## Objective
Build a real-time object detection and tracking system with a simple graphical user interface (GUI) that uses a webcam to detect objects with YOLOv8 and track them uniquely using the SORT algorithm.

## 🧑‍💻 Language & Libraries

- **Language**: Python 3.8+
- **Libraries**:
  - OpenCV
  - Ultralytics (YOLOv8)
  - NumPy
  - FilterPy (for SORT)
  - Tkinter (GUI)

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
├── object_detection_gui.py   #Main Python script with GUI and detection logic
├── sort.py   #SORT tracking algorithm implementation
├── yolov8n.pt   #Pre-trained YOLOv8 weights file
├── README.md   # This documentation file
└── requirements.txt   # Python dependencies (optional)
```

## How to Run
1. **Open terminal or command prompt and navigate to the project folder:**
```bash
cd "path_to_your_project_folder"
```
2. **Run the GUI application:**
```bash
python object_detection_gui.py
```
3. **Use the GUI:**

- Click Start Detection to begin real-time detection and tracking.

- Click Stop Detection or close the windows to exit.

**Sample Output:**
## Sample Output

When you run the program, a GUI window opens and your webcam feed appears with:

- Green bounding boxes drawn around detected objects
- Labels on each bounding box indicating the object class and a unique tracking ID, e.g., "person ID 1"
- Real-time tracking as objects move across frames, with IDs remaining consistent
- A console log might show detection counts or status messages (optional)


## ✅ Developed by:
  **Aabhash Jaiswal**

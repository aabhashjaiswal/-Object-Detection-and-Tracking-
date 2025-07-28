import tkinter as tk
from tkinter import messagebox
import threading
import cv2
from ultralytics import YOLO
from sort import Sort

import numpy as np

class ObjectDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Object Detection and Tracking")
        self.root.geometry("300x150")

        self.start_btn = tk.Button(root, text="Start Detection", command=self.start_detection)
        self.start_btn.pack(pady=20)

        self.stop_btn = tk.Button(root, text="Stop Detection", command=self.stop_detection, state=tk.DISABLED)
        self.stop_btn.pack(pady=10)

        self.running = False
        self.thread = None

    def start_detection(self):
        self.running = True
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)

        # Run detection in separate thread to avoid freezing UI
        self.thread = threading.Thread(target=self.run_detection)
        self.thread.start()

    def stop_detection(self):
        self.running = False
        self.stop_btn.config(state=tk.DISABLED)
        self.start_btn.config(state=tk.NORMAL)

    def run_detection(self):
        model = YOLO("yolov8n.pt")
        tracker = Sort()
        cap = cv2.VideoCapture(0)  # Webcam

        while self.running:
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame, verbose=False)[0]

            detections = []
            for r in results.boxes:
                x1, y1, x2, y2 = map(int, r.xyxy[0])
                conf = float(r.conf[0])
                detections.append([x1, y1, x2, y2, conf])

            if detections:
                detections_np = np.array(detections)
            else:
                detections_np = np.empty((0, 5))

            tracked_objects = tracker.update(detections_np)

            for obj in tracked_objects:
                x1, y1, x2, y2, track_id = map(int, obj)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 2)
                cv2.putText(frame, f"ID {track_id}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 200, 0), 2)

            cv2.imshow("Object Detection and Tracking", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.running = False
                break

        cap.release()
        cv2.destroyAllWindows()
        self.stop_detection()

if __name__ == "__main__":
    root = tk.Tk()
    app = ObjectDetectionApp(root)
    root.mainloop()

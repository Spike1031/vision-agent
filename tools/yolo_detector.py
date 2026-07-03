import json
import os

from ultralytics import YOLO


# =========================
# Configuration
# =========================
MODEL_PATH = "yolov8n.pt"

OUTPUT_DIR = "data"
DETECTION_JSON = os.path.join(OUTPUT_DIR, "detection.json")


class YOLODetector:

    def __init__(self):
        self.model = YOLO(MODEL_PATH)

    def detect(self, image_path):

        results = self.model(image_path)

        objects = []

        for result in results:
            for box in result.boxes:

                cls = int(box.cls[0])
                label = self.model.names[cls]

                objects.append({
                    "class": label
                })

        # Create output directory
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        # Save detection result
        with open(DETECTION_JSON, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "objects": objects
                },
                f,
                indent=4,
                ensure_ascii=False
            )
            
        os.makedirs("reports", exist_ok=True)
        results[0].save(filename="reports/detection_result.jpg")

        print(f"Detection JSON saved to {DETECTION_JSON}")

        return objects
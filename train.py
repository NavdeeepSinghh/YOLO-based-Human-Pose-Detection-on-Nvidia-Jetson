from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="data.yaml",
    epochs=15,   # ⭐ your choice
    imgsz=640,
    batch=4
)
from ultralytics import YOLO
import cv2

# Load model
model = YOLO("runs/detect/train2/weights/best.pt")

# Read image
img = cv2.imread("Screenshot.png")

# Run detection
results = model.predict(img, conf=0.4)

# Draw results
annotated = results[0].plot()

# ✅ SAVE RESULT (NOT SHOW)
cv2.imwrite("output.jpg", annotated)

print("✅ Detection complete. Saved as output.jpg")
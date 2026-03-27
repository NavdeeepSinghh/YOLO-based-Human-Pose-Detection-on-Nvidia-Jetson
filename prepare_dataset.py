import os
import random
import shutil

DATASET_PATH = "YOLO-HiVis-Data"

IMAGES_PATH = os.path.join(DATASET_PATH, "images")
LABELS_PATH = os.path.join(DATASET_PATH, "labels")

TRAIN_IMAGES = os.path.join(DATASET_PATH, "train/images")
TRAIN_LABELS = os.path.join(DATASET_PATH, "train/labels")

VAL_IMAGES = os.path.join(DATASET_PATH, "val/images")
VAL_LABELS = os.path.join(DATASET_PATH, "val/labels")

# create folders
for path in [TRAIN_IMAGES, TRAIN_LABELS, VAL_IMAGES, VAL_LABELS]:
    os.makedirs(path, exist_ok=True)

# get all images
all_images = [f for f in os.listdir(IMAGES_PATH) if f.endswith(".jpg")]

random.shuffle(all_images)

split_index = int(0.7 * len(all_images))   # ⭐ 70%

train_files = all_images[:split_index]
val_files = all_images[split_index:]

print(f"Train: {len(train_files)}")
print(f"Val: {len(val_files)}")

def copy_files(file_list, img_dest, label_dest):
    for file in file_list:
        img_src = os.path.join(IMAGES_PATH, file)
        label_file = file.replace(".jpg", ".txt")
        label_src = os.path.join(LABELS_PATH, label_file)

        shutil.copy(img_src, os.path.join(img_dest, file))

        if os.path.exists(label_src):
            shutil.copy(label_src, os.path.join(label_dest, label_file))

# copy instead of move (SAFE)
copy_files(train_files, TRAIN_IMAGES, TRAIN_LABELS)
copy_files(val_files, VAL_IMAGES, VAL_LABELS)

print("✅ Split Done (70-30)")
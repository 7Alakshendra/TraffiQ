from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # pretrained YOLO26n model

# Run batched inference on a list of images
results = model("cv/test_data/pexels-kimymoto-20100820.jpg",stream=False)  # return a list of Results objects
vechicle_classes=[2,3,5,7]
result=results[0]

# Process results list
count=0
boxes = result.boxes  # Boxes object for bounding box outputs
masks = result.masks  # Masks object for segmentation masks outputs
keypoints = result.keypoints  # Keypoints object for pose outputs
probs = result.probs  # Probs object for classification outputs
obb = result.obb  # Oriented boxes object for OBB outputs
result.show()  # display to screen

for box in boxes:
    if int(box.cls) in vechicle_classes:
        count+=1
print(f"Number of Vehicles in the frame:{count}")

    
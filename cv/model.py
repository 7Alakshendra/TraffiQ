from ultralytics import YOLO

# Load a model
model = YOLO("yolov8s.pt")  

def get_density(frame):
    results = model(frame,stream=False)  
    vechicle_classes=[2,3,5,7]
    result=results[0]

    count=0
    boxes = result.boxes  # Boxes object for bounding box outputs
    for box in boxes:   
        if int(box.cls) in vechicle_classes:            
            count+=1
    if count<10:       
        density="Light"
    elif count<=20:
        density="Moderate"
    else:
        density="High"
    return density


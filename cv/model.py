from ultralytics import YOLO
import cv2

# Load a model
model = YOLO("yolo26s.pt")  

def process_video(video):
    cap = cv2.VideoCapture(video)
    i = 0
    densities = []  
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(int(fps))
# Define how many seconds to skip
    frames_per_sample = int(5*fps)
   
    while cap.isOpened():
        
        ret, frame = cap.read()  
        if not ret:
            break
        if i % frames_per_sample == 0:
            density = get_density(frame)
            densities.append(density)
            print(f"second{i//int(fps)}: {density}")
        i += 1  

    cap.release()
    return densities
   

def get_density(frame):
    results = model(frame,stream=False)  
    vechicle_classes=[2,3,5,7]
    count=0
    boxes = results[0].boxes  # Boxes object for bounding box outputs
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

if __name__ == "__main__":
    densities = process_video("test_data/video.mp4")
    print(densities)

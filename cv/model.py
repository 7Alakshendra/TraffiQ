from ultralytics import YOLO
import cv2
import os

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
            density,count,_= get_density(frame)
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
    return density,count,results

def check_alert(densities):
    if len(densities)<60:
        return "Insufficient Data"
    
    if len(densities)>=60 and all(d=="High" for d in densities[-60:]):
        return "Heavy Congestion. Attention Required!"
    
    return"Normal Traffic"

def annotate_video(video_path):
    os.makedirs("cv/output", exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter("cv/output/annotated.mp4", cv2.VideoWriter_fourcc(*"avc1"), fps, (width, height))    # Add this debug line
    print(f"VideoWriter opened: {out.isOpened()}")
    print(f"FPS: {fps}, Width: {width}, Height: {height}")
    while cap.isOpened():
        ret,frame=cap.read()

        if not ret:
            break
        
        density, count, results = get_density(frame)
        annotated_frame = results[0].plot()
        
        # Density text
        cv2.putText(annotated_frame, f"Density: {density}", (10, 30), 
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

        # Vehicle count
        cv2.putText(annotated_frame, f"Vehicles: {count}", (10, 70),
            cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

       # Alert if High
        if density == "High":
                cv2.putText(annotated_frame, "ALERT: HIGH CONGESTION", (10, 110),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)
        # Write annotated frame to output video
        out.write(annotated_frame)
    cap.release()
    out.release()
    return  "cv/output/annotated.mp4"



if __name__ == "__main__":
    print("Annotating video...")
    output_path = annotate_video("cv/test_data/video.mp4")
    print(f"Annotated video saved to: {output_path}")

from ultralytics import YOLO
import cv2
import os
import math

model = YOLO("yolo26s.pt")

def get_center(box):
    x1, y1, x2, y2 = box.xyxy[0]
    return (int((x1 + x2) / 2), int((y1 + y2) / 2))

def detect_emergency(video_path):
    cap = cv2.VideoCapture(video_path)
    vehicle_history = {}
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        timestamp = frame_count / fps
        frame_count += 1
        results = model.track(frame, persist=True)

        for box in results[0].boxes:
            if box.id is None:
                continue
            vehicle_id = int(box.id)
            center = get_center(box)

            if vehicle_id not in vehicle_history:
                vehicle_history[vehicle_id] = []

            vehicle_history[vehicle_id].append((center, timestamp))

    cap.release()
    return vehicle_history

def check_stationary(vehicle_history, stationary_threshold=15):
    emergencies = []

    # Calculate average movement of all vehicles
    all_movements = []
    for vehicle_id, history in vehicle_history.items():
        if len(history) < 2:
            continue
        first = history[0][0]
        last = history[-1][0]
        movement = math.sqrt((last[0] - first[0])**2 + (last[1] - first[1])**2)
        all_movements.append(movement)

    avg_movement = sum(all_movements) / len(all_movements) if all_movements else 0

    # Traffic jam — everyone slow
    if avg_movement < 30:
        emergencies.append({
            "type": "TRAFFIC_JAM",
            "message": "Sustained low movement — attention required",
            "avg_movement": round(avg_movement, 2)
        })
        return emergencies

    # Individual stationary vehicle in moving traffic
    for vehicle_id, vehicle in vehicle_history.items():
        recent = [(pos, t) for pos, t in vehicle if t >= vehicle[-1][1] - stationary_threshold]

        if len(recent) < 2:
            continue

        first_pos = recent[0][0]
        last_pos = recent[-1][0]
        distance = math.sqrt((last_pos[0] - first_pos[0])**2 + (last_pos[1] - first_pos[1])**2)
        stationary_time = recent[-1][1] - recent[0][1]

        if distance < 50 and stationary_time > 15:
            emergencies.append({
                "type": "INCIDENT",
                "vehicle_id": vehicle_id,
                "position": last_pos,
                "stationary_for": round(stationary_time, 1),
                "message": f"Vehicle {vehicle_id} stationary for {round(stationary_time, 1)}s — possible accident or breakdown"
            })

    return emergencies

def get_attention_status(video_path):
    """Main function called by backend — returns simple attention status."""
    history = detect_emergency(video_path)
    emergencies = check_stationary(history)

    return {
        "attention_required": len(emergencies) > 0,
        "emergency_count": len(emergencies),
        "message": "Attention Required" if emergencies else "Normal",
        "details": emergencies
    }

if __name__ == "__main__":
    video_path = "cv/test_data/video.mp4"
    print("Detecting emergencies...")
    result = get_attention_status(video_path)
    print(f"Attention required: {result['attention_required']}")
    print(f"Message: {result['message']}")
    print(f"Emergency count: {result['emergency_count']}")
    for e in result['details']:
        print(e)




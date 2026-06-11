import requests
from datetime import datetime
from config import TOMTOM_API_KEY,CORRIDORS
import csv
import os
import time

def get_traffic_data(lat,lon):
    URL=f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?key={TOMTOM_API_KEY}&point={lat},{lon}&unit=KMPH"
    response = requests.get(URL)
    data=response.json()
    return data
def save_to_csv(corridor_name, data, timestamp):
    segment = data['flowSegmentData']
    
    current_speed = segment['currentSpeed']
    free_flow_speed = segment['freeFlowSpeed']
    travel_time = segment['currentTravelTime']
    confidence = segment['confidence']
    
    congestion = round((1 - current_speed / free_flow_speed) * 100, 2)
    
    row = [timestamp, corridor_name, current_speed, 
           free_flow_speed, travel_time, confidence, congestion]
    
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, '..', 'data', 'raw', 'traffic_readings.csv')
    
    file_exists = os.path.exists(file_path)
    
    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['timestamp', 'corridor', 'current_speed', 
                            'free_flow_speed', 'travel_time', 'confidence', 'congestion'])
        writer.writerow(row)

if __name__ == "__main__":
    for corridor in CORRIDORS:
        data = get_traffic_data(corridor['lat'], corridor['lon'])
        timestamp = datetime.now()
        save_to_csv(corridor['name'], data, timestamp)
        print(f"Saved data for {corridor['name']}")
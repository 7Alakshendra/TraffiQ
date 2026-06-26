from collector.collect import get_traffic_data
from collector.config import CORRIDORS, TOMTOM_API_KEY,OPEN_WEATHER_MAP_API_KEY
import requests
import pandas as pd
import datetime
import os



def get_corridor_density(corridor_name:str):
    """Get real-time traffic density for a specific Bengaluru corridor.
    Returns current speed, free flow speed, congestion percentage and status.
    Use this when you need detailed information about a specific corridor
    or when investigating why a particular road is congested."""

    corridor = next((c for c in CORRIDORS if c["name"] == corridor_name), None)
    
    if corridor is None:
        return {"error": f"Corridor {corridor_name} not found"}
    
    # call TomTom API with the corridor's coordinates
    data = get_traffic_data(corridor["lat"], corridor["lon"])
    segment = data["flowSegmentData"]
    
    current_speed = segment["currentSpeed"]
    free_flow_speed = segment["freeFlowSpeed"]
    congestion = round((1 - current_speed / free_flow_speed) * 100, 2)
    
    # derive status from congestion percentage
    if congestion < 33:
        status = "Low"
    elif congestion <= 66:
        status = "Moderate"
    else:
        status = "High"
    
    return {
        "name": corridor_name,
        "current_speed": current_speed,
        "free_flow_speed": free_flow_speed,
        "congestion": congestion,
        "status": status
    }

def get_all_corridors():
    """Get real-time traffic conditions for all 5 Bengaluru corridors simultaneously.
    Returns a city-wide snapshot of current speed, congestion and status.
    Always call this first to get an overview before investigating specific corridors."""

    results = {}
    for corridor in CORRIDORS:
        name = corridor["name"]
        results[name] = get_corridor_density(name)
    return results

def get_weather(corridor_name:str):
    """Get current weather conditions for a specific Bengaluru corridor.
    Use this when you need to understand if rain, fog, or wind 
    might be affecting traffic conditions."""
    print(f"get_weather called with: {corridor_name}")
    corridor = next((c for c in CORRIDORS if c["name"] == corridor_name), None)
    if corridor is None:
        return {"error": f"Corridor {corridor_name} not found"}
    lat,lon=corridor['lat'],corridor['lon']
    URL=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_MAP_API_KEY}&units=metric"
    response=requests.get(URL)
    data = response.json()
    return {
    "description": data['weather'][0]['description'],
    "temp": data['main']['temp'],
    "visibility": data.get('visibility', 'N/A')}

def get_historical_pattern(corridor_name:str):
    """Get historical traffic patterns for a specific Bengaluru corridor
    based on current hour and day of week.
    Returns average historical congestion and speed for comparison.
    Use this to determine if current congestion is unusual compared
    to what normally happens at this time — helps identify incidents."""

    BASE_DIR = os.path.dirname(__file__)
    csv_path = os.path.join(BASE_DIR, '..', 'data', 'raw', 'traffic_readings.csv')
    df = pd.read_csv(csv_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek

    present_moment=datetime.datetime.now()
    current_hour=present_moment.hour
    current_day=present_moment.weekday()
    filtered = df[
    (df["corridor"] == corridor_name) &
    (df["hour"].between(current_hour - 1, current_hour + 1))]

    if len(filtered) == 0:
        return {"pattern": "No historical data available"}
    
    return {
        "corridor": corridor_name,
        "avg_congestion": round(filtered['congestion'].mean(), 2),
        "avg_speed": round(filtered['current_speed'].mean(), 2),
        "sample_size": len(filtered)
    }
   

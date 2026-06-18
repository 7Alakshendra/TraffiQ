from collector.collect import get_traffic_data
from collector.config import CORRIDORS, TOMTOM_API_KEY

def get_corridor_density(corridor_name):
    # find the corridor dictionary that matches the name
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
    results = {}
    for corridor in CORRIDORS:
        name = corridor["name"]
        results[name] = get_corridor_density(name)
    return results

if __name__ == "__main__":
    print(get_all_corridors())
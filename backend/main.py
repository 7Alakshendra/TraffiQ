from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from cv.model import process_video, check_alert
from cv.emergency import get_attention_status

cached_result = None
cached_emergency = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global cached_result, cached_emergency
    
    # CV analysis
    densities = process_video("cv/test_data/video.mp4")
    alert = check_alert(densities)
    dominant = max(set(densities), key=densities.count) if densities else "Unknown"
    cached_result = {
        "density": dominant,
        "alert": alert,
        "total_readings": len(densities),
        "high_count": densities.count("High"),
        "moderate_count": densities.count("Moderate"),
        "low_count": densities.count("Light")
    }
    
    # Emergency detection
    cached_emergency = get_attention_status("cv/test_data/video.mp4")
    
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET"],
    allow_headers=["*"]
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/predict")
def predict(route: str, departure: str):
    return {
        "route": route,
        "forecast": [
            {"time": "08:45", "status": "heavy"},
            {"time": "09:00", "status": "heavy"},
            {"time": "09:15", "status": "moderate"},
            {"time": "09:30", "status": "clear"}
        ],
        "recommended_departure": "09:35"
    }

@app.get("/analyze-frame")
def analyze_frame():
    return cached_result

@app.get("/emergency-status")
def emergency_status():
    return cached_emergency
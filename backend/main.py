from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server port
    allow_methods=["GET"],
    allow_headers=["*"]
)

@app.get("/health")
def health():
    return {"status":"ok"}

@app.get("/predict")
def predict(route : str, departure: str):

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
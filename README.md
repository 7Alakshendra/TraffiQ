TraffiQ
AI-powered traffic intelligence platform for Indian cities — built for both daily commuters and traffic authorities.
For Citizens

TraffiQ predicts traffic conditions 30–90 minutes ahead so commuters can plan their departure time before stepping out. Unlike real-time navigation apps, TraffiQ tells you the best time to leave — not just how bad it is right now.
For Traffic Authorities

An AI agent monitors live CCTV footage across the city in real time — detecting traffic violations (red light jumping, wrong-side driving, speeding), identifying congestion hotspots, and flagging emergencies. Authorities get an intelligent dashboard that surfaces exactly where intervention is needed, without manually watching hundreds of camera feeds.
How it works

Live traffic data collected from TomTom API across key Bengaluru corridors every 15 minutes via automated pipeline
ML forecasting model predicts traffic states 30–90 minutes ahead based on historical patterns
Computer vision module (YOLOv8) processes road camera footage — counts vehicles, classifies density, detects violations and anomalies
AI agent aggregates signals across all camera feeds and prioritizes alerts for authorities
FastAPI backend serves predictions to both the citizen app and authority dashboard
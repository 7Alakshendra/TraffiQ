import os
from dotenv import load_dotenv

load_dotenv()
TOMTOM_API_KEY = os.getenv("TOMTOM_API_KEY")

CORRIDORS=[{"name":"Silk Board","lat":12.9166968756781,"lon": 77.62332905126449},
             {"name":"MG Road","lat":12.974918739626172,"lon": 77.6095028008516},
             {"name":"Hebbal Flyover","lat":13.043026728189988,"lon": 77.59038123777438} , 
             {"name":"Marathalli Brg","lat":12.96526609231816,"lon": 77.70491310110818} , 
             {"name":"Tin Factory","lat":12.998013296355929,"lon": 77.66963351303413} ]
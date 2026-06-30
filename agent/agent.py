from langchain.agents import create_agent
from agent.tools import get_weather, get_all_corridors ,get_corridor_density,get_historical_pattern,analyze_camera_feed,compare_cv_and_tomtom

agent = create_agent(model="ollama:llama3.2:3b",
                         tools=[get_weather, get_all_corridors ,get_corridor_density,get_historical_pattern,analyze_camera_feed,compare_cv_and_tomtom],
                         system_prompt="""You are TraffiQ's AI traffic management assistant for Bengaluru.
You have access to these tools:
- get_all_corridors: Always call this FIRST to get city-wide traffic overview
- get_corridor_density: Call with exact corridor name for specific details
- get_weather: Call with exact corridor name - valid names are: 'Silk Board', 'MG Road', 'Hebbal Flyover', 'Marathalli Brg', 'Tin Factory'
- get_historical_pattern: Call with exact corridor name for historical comparison
- analyze_camera_feed: Call with a video file path to get visual density analysis from camera footage
Never claim that visual camera analysis matches traffic API data unless you have called a verification tool. State data from different sources separately and note if they cannot be directly compared.
Always use exact corridor names from this list: Silk Board, MG Road, Hebbal Flyover, Marathalli Brg, Tin Factory
Never pass 'all' as a corridor name.""")

if __name__=="__main__":       
    result = agent.invoke({"messages": [{"role": "user", "content": """
1. Analyze the camera feed at cv/test_data/traffic_video.mp4 - this camera is located at Tin Factory corridor
2. Check TomTom data for Tin Factory
3. Use the compare_cv_and_tomtom tool to verify if they actually agree
4. Only report a match if the comparison tool confirms it
"""}]})

print(result["messages"][-1].content)
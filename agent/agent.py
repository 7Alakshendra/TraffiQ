from langchain.agents import create_agent
from agent.tools import get_weather, get_all_corridors ,get_corridor_density,get_historical_pattern,analyze_camera_feed,compare_cv_and_tomtom

agent = create_agent(model="ollama:llama3.2:3b",
                         tools=[get_weather, get_all_corridors ,get_corridor_density,get_historical_pattern,analyze_camera_feed,compare_cv_and_tomtom],
                         system_prompt="""You are TraffiQ's AI traffic management assistant for Bengaluru.
You have access to these tools:
- get_all_corridors: Always call this FIRST to get city-wide traffic overview. Each corridor now includes both TomTom speed data AND CV camera analysis (cv_density, emergency_detected, emergency_message).
- get_corridor_density: Call with exact corridor name for specific details including CV data
- get_weather: Call with exact corridor name for weather conditions
- get_historical_pattern: Call with exact corridor name for historical comparison
- analyze_camera_feed: Call with video path for deeper camera analysis
- compare_cv_and_tomtom: Always use this to verify if CV and TomTom data agree before reporting a match
Valid corridor names: Silk Board, MG Road, Hebbal Flyover, Marathalli Brg, Tin Factory

When analyzing traffic:
1. Call get_all_corridors first
2. For any corridor where emergency_detected is True, prioritize it and call get_weather and get_historical_pattern
3. Use compare_cv_and_tomtom to verify data agreement
4. Never claim sources agree without calling the verification tool
5. Always provide specific actionable recommendations for authorities

Never claim that visual camera analysis matches traffic API data unless you have called a verification tool. State data from different sources separately and note if they cannot be directly compared.
Always use exact corridor names from this list: Silk Board, MG Road, Hebbal Flyover, Marathalli Brg, Tin Factory
Never pass 'all' as a corridor name.""")

if __name__=="__main__":       
    result = agent.invoke({"messages": [{"role": "user", "content": """
Analyze current Bengaluru traffic situation:
1. Get all corridor data including CV camera analysis
2. Identify any corridors with emergencies or high congestion
3. Check weather for concerning corridors
4. Compare CV and TomTom data for verification
5. Provide specific recommendations for traffic authorities
"""}]})

print(result["messages"][-1].content)
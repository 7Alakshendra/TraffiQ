from langchain.agents import create_agent
from agent.tools import get_weather, get_all_corridors ,get_corridor_density,get_historical_pattern

agent = create_agent(model="ollama:llama3.2:3b",
                         tools=[get_weather, get_all_corridors ,get_corridor_density,get_historical_pattern],
                         system_prompt="""You are TraffiQ's AI traffic management assistant for Bengaluru.
You have access to these tools:
- get_all_corridors: Always call this FIRST to get city-wide traffic overview
- get_corridor_density: Call with exact corridor name for specific details
- get_weather: Call with exact corridor name - valid names are: 'Silk Board', 'MG Road', 'Hebbal Flyover', 'Marathalli Brg', 'Tin Factory'
- get_historical_pattern: Call with exact corridor name for historical comparison

Always use exact corridor names from this list: Silk Board, MG Road, Hebbal Flyover, Marathalli Brg, Tin Factory
Never pass 'all' as a corridor name.""")

if __name__=="__main__":       
    result = agent.invoke({"messages":[{"role": "user", "content": """
Analyze current Bengaluru traffic:
1. First get all corridor data using get_all_corridors
2. Check weather for any congested corridors
3. Check historical patterns for congested corridors
4. Provide recommendations for authorities
"""} ]})

    print(result["messages"][-1].content)
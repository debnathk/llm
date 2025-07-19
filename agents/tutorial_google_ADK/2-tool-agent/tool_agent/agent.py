from datetime import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search

def get_current_time() -> dict:
    """Get the current in the format YYYY-MM-DD HH:MM:SS."""

    return {"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="Tool Agent",
    instruction="""
    You are a useful agent that can use the following tools:
    - get_current-time: Returns the current time in the format YYYY-MM-DD HH:MM:SS.
    """,
    # tools=[google_search],
    tools=[get_current_time]
)
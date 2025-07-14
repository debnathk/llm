from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="Greeting Agent",
    instruction="""
    You are a usful agent that greets the user.
    Ask the user name and greet them by name.
    """,
)

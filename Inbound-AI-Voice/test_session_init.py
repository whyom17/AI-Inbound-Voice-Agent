
from livekit.agents import AgentSession, llm
from unittest.mock import MagicMock

class MyFuncs:
    @llm.function_tool(description="desc")
    def my_tool(self):
        pass

fnc = MyFuncs()
tools = llm.find_function_tools(fnc)

print(f"Testing AgentSession with tools: {tools}")

try:
    # We mock everything else
    session = AgentSession(
        stt=MagicMock(),
        llm=MagicMock(),
        tts=MagicMock(),
        tools=tools
    )
    print("AgentSession initialized successfully")
except Exception as e:
    print(f"AgentSession failed: {e}")


from livekit.agents import llm
import asyncio

class MyFuncs:
    @llm.function_tool(description="desc")
    def my_tool(self):
        pass

fnc = MyFuncs()
tools = llm.find_function_tools(fnc)
print(f"Tools found: {tools}")

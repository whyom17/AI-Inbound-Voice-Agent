
from livekit.agents import llm
import asyncio

class MyFuncs:
    @llm.function_tool(description="desc")
    def my_tool(self):
        pass

fnc = MyFuncs()
tools = llm.find_function_tools(fnc)
print(f"Type of first tool: {type(tools[0])}")
print(f"Is instance of FunctionTool? {isinstance(tools[0], llm.FunctionTool)}")
print(f"Is instance of method? {callable(tools[0])}")

from mcp.server.fastmcp import FastMCP
from agents import run_research
import asyncio

# Create MCP instance
mcp = FastMCP("crew_research")

@mcp.tool()
async def crew_research(query: str) -> str:
    """Run CrewAI-based research system for given user query. Can do both standard and deep web search.

    Args:
        query (str): The research query or question.

    Returns:
        str: The research response from the CrewAI pipeline.
    """
    return run_research(query)

# Run the server
if __name__ == "__main__":
    mcp.run(transport="stdio")


# {
#   "mcpServers": {
#     "crew_research": {
#       "command": "uv",
#       "args": [
#         "--directory",
#         "abslute/path/to/project_root",
#         "run",
#         "server.py"
#       ],
#       "env": {
#         "LINKUP_API_KEY": "your_linkup_api_key_here"
#       }
#     }
#   }
# }
from fastmcp import FastMCP

mcp = FastMCP("playmcp-test")


@mcp.tool
def ping() -> str:
    """Health check"""
    return "pong"


if __name__ == "__main__":
    mcp.run()
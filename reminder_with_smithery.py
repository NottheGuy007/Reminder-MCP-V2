"""
Extended Reminder Server with Smithery.ai Integration
This file imports all tools from reminder_server.py and adds Smithery tools
"""
import sys
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger("reminder_with_smithery")

mcp = FastMCP("Xiaozhi Reminder Server with Smithery")

logger.info("Importing Smithery connector...")
from smithery_connector import (
    smithery_connect,
    smithery_list_servers, 
    smithery_list_tools,
    smithery_call_tool
)

logger.info("Importing reminder tools...")
from reminder_server import (
    init_database,
    add_reminder,
    list_reminders,
    get_upcoming_reminders,
    check_overdue_reminders,
    complete_reminder,
    delete_reminder,
    search_reminders,
    get_reminder_stats
)


@mcp.tool()
def connect_smithery_server(server_name: str, server_url: str, config_json: str = "{}"):
    """Connect to a Smithery.ai hosted MCP server. Example: connect_smithery_server('exa', 'https://api.smithery.ai/servers/exa', '{}')"""
    return smithery_connect(server_name, server_url, config_json)


@mcp.tool()
def list_smithery_servers():
    """List all connected Smithery.ai servers"""
    return smithery_list_servers()


@mcp.tool()
def list_smithery_tools(server_name: str):
    """List available tools from a connected Smithery server. Example: list_smithery_tools('exa')"""
    return smithery_list_tools(server_name)


@mcp.tool()
def call_smithery_tool(server_name: str, tool_name: str, arguments_json: str = "{}"):
    """Call a tool on a connected Smithery server. Example: call_smithery_tool('exa', 'search', '{"query": "AI news"}')"""
    return smithery_call_tool(server_name, tool_name, arguments_json)


@mcp.tool()
def add_reminder_tool(title: str, datetime_str: str, description: str = "", user_id: str = "default"):
    """Add a new reminder with title, datetime (YYYY-MM-DD HH:MM), and optional description"""
    return add_reminder(title, datetime_str, description, user_id)


@mcp.tool()
def list_reminders_tool(include_completed: str = "false", user_id: str = "default"):
    """List all reminders, optionally include completed ones (true/false)"""
    return list_reminders(include_completed, user_id)


@mcp.tool()
def get_upcoming_reminders_tool(hours: str = "24", user_id: str = "default"):
    """Get reminders due within the next N hours (default 24)"""
    return get_upcoming_reminders(hours, user_id)


@mcp.tool()
def check_overdue_reminders_tool(user_id: str = "default"):
    """Check for overdue reminders that need immediate attention"""
    return check_overdue_reminders(user_id)


@mcp.tool()
def complete_reminder_tool(reminder_id: str, user_id: str = "default"):
    """Mark a reminder as completed by its ID"""
    return complete_reminder(reminder_id, user_id)


@mcp.tool()
def delete_reminder_tool(reminder_id: str, user_id: str = "default"):
    """Delete a reminder permanently by its ID"""
    return delete_reminder(reminder_id, user_id)


@mcp.tool()
def search_reminders_tool(query: str, user_id: str = "default"):
    """Search reminders by title or description"""
    return search_reminders(query, user_id)


@mcp.tool()
def get_reminder_stats_tool(user_id: str = "default"):
    """Get statistics about all reminders"""
    return get_reminder_stats(user_id)


init_database()

if __name__ == "__main__":
    logger.info("Starting Xiaozhi Reminder Server with Smithery.ai Integration...")
    logger.info("Available features:")
    logger.info("  - All reminder tools (add, list, search, etc.)")
    logger.info("  - Smithery.ai server connections")
    logger.info("  - Access to 2500+ Smithery MCP tools")
    mcp.run(transport="stdio")

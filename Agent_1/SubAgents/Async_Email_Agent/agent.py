import os # Required for path operations
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset,StreamableHTTPServerParams
from google.adk.models.lite_llm import LiteLlm
from datetime import datetime


# # TO LOAD ENVIRONMENT VARIABLES
# import os
from dotenv import load_dotenv
BASEDIR = os.path.abspath(os.path.dirname(__file__))
# Load environment variables from .env file
load_dotenv(os.path.join(BASEDIR, '../../../.env'))


# Zapier MCP server
zapier_toolset = MCPToolset(
    connection_params=StreamableHTTPServerParams(
        # connection_params=StdioConnectionParams(
        url=os.environ.get("ZAPIER_MCP_SERVER_URL") 
    )
)




# Model=LiteLlm("openai/qwen3:latest") #for tool use will OLLAMA
# Model=LiteLlm("openai/gemma3:12b")  # Use LiteLlm for local ollama or openrouter models
# Model=LiteLlm("openrouter/google/gemma-3-27b-it:free"), #this is for openrouter using LiteLlm wrapper
Model="gemini-2.0-flash" #for gemini models


Async_Email_Agent = LlmAgent(
    model=Model,
    name="Async_Email_Agent",  # Use a unique name for your agent
    instruction="""You are a helpful assistant and subagent that can interact with an email MCP server to perform tasks. 
                You can use tools provided by the MCP server to assist with various tasks. 
                For any tools where a schmea field is marked as required, ask me or the user what to fill in for that field. 
                If you do not know what to fill in, ask me for clarification.
                If the response of the tool is SUCCESS or anything similar, tell me so.
                If the response of the tool is error, tell me as well.
                Tell me if you are successful in performing the task or not.
                If not... tell me why you were not successful.
                You can only ask about the heading and body of the email unless there are required fields in the schema of the tool
                that you don't know the answer to.
                if for any reason you cannot perform a task, please delegate back to the root_agent.
                """,
    tools=[zapier_toolset],
)
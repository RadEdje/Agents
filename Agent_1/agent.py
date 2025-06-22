from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.agent_tool import AgentTool
# from google.adk.tools import google_search  # Importing the Google Search tool for use in the agent
# from google.genai import types  

from pydantic import BaseModel, Field
from typing import List, Literal, Optional, Dict, Any

from pydantic import ValidationError as e


print(e) # Print the validation errors

# # TO LOAD ENVIRONMENT VARIABLES if you are on local server
# import os
# from dotenv import load_dotenv
# BASEDIR = os.path.abspath(os.path.dirname(__file__))
# # Load environment variables from .env file
# load_dotenv(os.path.join(BASEDIR, '../.env'))



# loading sub-agents
from .SubAgents.Async_Email_Agent.agent import Async_Email_Agent
from .SubAgents.Async_Google_Search_Agent.agent import Async_Google_Search_Agent    
# from .SubAgents.Async_File_System_Agent.agent import Async_File_System_Agent


class InlineData(BaseModel):
    data: str = Field(..., description="Base64 encoded content of the data.")
    mimeType: str = Field(..., description="MIME type of the content (e.g., 'image/png', 'image/jpeg').")
    displayName: Optional[str] = Field(None, description="Optional display name for the data.")

class MessagePart(BaseModel):
    text: Optional[str] = Field(None, description="Text content of the message part.")
    inlineData: Optional[InlineData] = Field(None, description="Inlined data content, e.g., for images or other small files.")
    # Add other fields like videoMetadata, thought, etc., if your agent uses them
    videoMetadata: Optional[Dict[str, Any]] = None
    thought: Optional[bool] = None
    inlineData: Optional[InlineData] = None # Ensure this is here
    fileData: Optional[Dict[str, Any]] = None
    thoughtSignature: Optional[str] = None
    codeExecutionResult: Optional[Dict[str, Any]] = None
    executableCode: Optional[Dict[str, Any]] = None
    functionCall: Optional[Dict[str, Any]] = None
    functionResponse: Optional[Dict[str, Any]] = None


# Define the Message structure
class Message(BaseModel):
    role: Literal["user", "model", "tool"] = Field(..., description="The role of the message sender (user, model, or tool).")
    parts: List[MessagePart] = Field(..., description="List of content parts within the message.")


# Define the RunRequest structure (as received by the /run endpoint)
class RunRequest(BaseModel):
    appname: str = Field(..., description="The name of the application/agent.")
    userId: str = Field(..., description="The ID of the user interacting with the agent.")
    sessionId: str = Field(..., description="The ID of the current session.")
    newMessage: Message = Field(..., description="The new message from the user to the agent.")
    streaming: bool = Field(False, description="Whether to stream the response (for /run_sse) or return it all at once (for /run).")
    state: Optional[Dict[str, Any]] = Field(None, description="Optional current state to pass to the agent.")
    conversation_history: Optional[List[Message]] = Field(None, description="Optional existing conversation history.")

# (Other imports like Agent, LiteLlm etc. would go here too)

# Model=LiteLlm("openai/qwen3:latest") #for tool use
# Model=LiteLlm("openai/gemma3:12b")  # Use LiteLlm for local ollama or openrouter models
# Model=LiteLlm("openrouter/google/gemma-3-27b-it:free"), #this is for openrouter using LiteLlm wrapper
Model="gemini-2.0-flash" #for gemini models
# Model="gemini-2.5-flash" #for gemini models

# to run adk_api.py server 
# Create the root agent
root_agent = Agent(
    name="Agent_1",
    model=Model,
    description="Helpful Agent for searching the web and assisting with radiology tasks.",
    instruction="""
    You are a helpful assistant to the user who should be a radiologist. You start by saying that you are being designed to help in health care as a radiologist's assistant but 
    you are not yet fully functional so you can make mistakes and that a certified radiologist should always be consulted.
    You can help make radiology reports, describe radiologic images but you should always remind the user that you are not a certified radiologist and 
    that they should always consult a certified radiologist for any medical decisions.
    You then ask for the user's name so you can greet them, and call them by their name. 

    You are also a coordinator for subagents. Your task is to responsibly and intelligently deligate tasks to the following
    agent:
    1. Async_Email_Agent: This agent can send emails to the user and other recipients.

    You also have one tool available to you:    
    1. AgentTool(Async_Google_Search_Agent): This tool can be used to search the web for information that may help you answer the user's questions or perform tasks.
    
    
    """,
    sub_agents=[ 
        Async_Email_Agent,  # Ensure this is the correct import for your Async_Email_Agent
        # Async_Google_Search_Agent  
        # Async_File_System_Agent 
    ],
    tools=[AgentTool(Async_Google_Search_Agent)],  # Add any tools you want to use here
    input_schema=Message  # Define the input schema for the agent
)

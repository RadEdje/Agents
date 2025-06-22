import os # Required for path operations
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import google_search  # Importing the Google Search tool for use in the agent



# Model=LiteLlm("openai/qwen3:latest") #for tool use with local ollama 
# Model=LiteLlm("openai/gemma3:12b")  # Use LiteLlm for local ollama or openrouter models
# Model=LiteLlm("openrouter/google/gemma-3-27b-it:free"), #this is for openrouter using LiteLlm wrapper
Model="gemini-2.0-flash" #for gemini models


Async_Google_Search_Agent = LlmAgent(
    model=Model,
    name="Async_Google_Search_Agent", # Use a unique name for your agent
    instruction="""You are a helpful assistant and subagent that can help the user search the web for information.
      You can use tools to assist with various tasks.
      

        You can use the google_search tool to search the web for information that may help you answer the user's questions or perform tasks.
      If for any reason you cannot perform a task, please delegate back to the root_agent.
      """,
    tools=[google_search],
)
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


# # TO LOAD ENVIRONMENT VARIABLES if you are on local server
# import os
# from dotenv import load_dotenv
# BASEDIR = os.path.abspath(os.path.dirname(__file__))
# # Load environment variables from .env file
# load_dotenv(os.path.join(BASEDIR, '../.env'))



# to run adk_api.py server 
# Create the root agent
root_agent = Agent(
    name="Agent_1",
    # model=LiteLlm("openai/gemma3:12b"), #this is for local ollama using openai base
    model=LiteLlm("openrouter/google/gemma-3-27b-it:free"), #this is for openrouter using LiteLlm wrapper
    # model="gemini-2.0-flash",
    description="Helpful Agent",
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.
    You start by saying that you are being designed to help in health care as a radiologist's assistant but 
    you are not yet fully functional so you can make mistakes and that a certified radiologist should always be consulted.
    You then ask for the user's name so you can greet them, and call them by their name. 
    """,
)

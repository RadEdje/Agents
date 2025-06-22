import os
import uvicorn
from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app

from pydantic import ValidationError as e


print(e) # Print the validation errors


# TO LOAD ENVIRONMENT VARIABLES if on local server
# import os
# from dotenv import load_dotenv
# BASEDIR = os.path.abspath(os.path.dirname(__file__))
# # Load environment variables from .env file
# load_dotenv(os.path.join(BASEDIR, '.env'))

# APP_NAME = "adk_api"  # Name of the application
AGENT_DIR = os.path.dirname(os.path.abspath(__file__))
print(f"Agent directory: {AGENT_DIR}")
# SESSION_DB_URL = os.getenv("SESSION_DB_URL", "sqlite:///./session.db") #no database for now
ALLOWED_ORIGINS = ["http://localhost:8000", "http://localhost:8080","*"]
# Set web=True if you intend to serve a web interface, False otherwise
SERVE_WEB_INTERFACE = True 

app = get_fast_api_app(
    # app_name=APP_NAME,
    agents_dir=AGENT_DIR,
    # session_db_url=SESSION_DB_URL, #no databse for now
    allow_origins=ALLOWED_ORIGINS,
    web=SERVE_WEB_INTERFACE  
)


# # Uncomment the following lines to run the FastAPI app with Uvicorn on a local server
if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        # port=int(os.environ.get("PORT", 8000)) #comment this out if on local pc to protect your ports
    )
## Inspiration
I'm a radiologist/Doctor by profession. Social media is full of posts saying that AI will learn radiology and eventually replace radiologists but does it always have to be this way? Is the end game always about AI replacing humans (in all professions)? What if it works the other way around? Can't the "human" learn AI, be empowered by AI, to do more, and be more than what he/she/they/them was/were trained to do? But what would a radiologist want to build? Want kind of agentic workflow would I want for myself? 

Radiologists are always buried in work but we still want to cater to the questions of our fellow healthworkers. We can't answer them all unfortunately but what if we had a radiology assistant, a chatbot that accepts images from people (fellow doctors, nurses, radtechs, hospital personnel), analyzes the images, searches for differentials if needed,  and based on their interactions, the rad assistant can email me accordingly ... To escalate an emergency for example or even draft a preliminary report so all I have to do is check it. Built in google search tool for the assistant can also help include differentials that can be bundled with the emailed draft. 

In my country, another problem we face is underdiagnosed pulmonary tuberculosis. An AI radiology assistant that can prescreen chest X-rays and push these to a radiologist's email may help for PTB screening, and triage. 



### My goals: 
1. to learn not just vibe coding with google gemini but actual agentic workflow deployment with google-adk 
2. not just on my local machine but in the cloud from backend to frontEnd
3. build a minimum viable product (MVP) for the chatBot.
4. Do this all in just 2 weeks (the time I have left for the hackathon)

### My problem: 
1. I had no prior experience in actual agentic workflows (save for the you tube vides and articles I really enjoy watching and reading but never actually doing).
2. I had no prior experience in serving AI models in the cloud
3. I had only 2 weeks to do this all (the time I have left for the hackathon)
4. I'm a doctor by profession. Programming is not second nature to me.

### Improbable odds but still made possible with...
1. Google gemini, and 
2. Google adk

## What my multiagent chat bot app does.
1. You can drag and drop images (screen shotted jpeg) onto the chat and ask the chatbot about it.
2. Ask it if it has something pertinent or emergent that a radiologist needs to see.
3. If the chat bot thinks so, you have the option for the chatbot to send an email immediately to the radiologist for escalation.
4. The chatbot can write a simple FYI message, do a google search for differentials, or even write a sample radiology report, then add all of these to  the email (for the radiologist to double check and confirm).
5. The chat bot can be hosted in the cloud or locally given the open nature of google-adk. It can use local free models like google gemma (for privacy) or use more powerful models like gemini in the cloud. 



## How I built it
1. I first used google adk to create a main agent called Agent_1. This deligates tasks to subagents.
2. The first subagent does email and is called Async_Email_Agent. It uses a gmail mcp (model context protocol) server.
3. The second agent is a google_search agent but it is appended as an AgentTool under the first agent. It uses a built in google search tool for gemini. 

## Challenges I ran into
1. It took me over 5 days just figure out how to serve an actual AI model in the cloud using python with actual fastAPI end points that a frontEnd webpage could access. I didn't even know what a fastAPI was until now let alone how to use it. I faced entire blocks of "errors" I probably would have never been able to understand in two weeks. However, putting it all into google gemini, I was able to more quickly figure out what went wrong. The best part of chosing google adk was that I instinctively thought that gemini would know a lot about the adk that it was obviously built around? Amazingly, gemini could give quick to the point answers to questions about google-adk I couldn't find answers to on you tube videos or even the actual docs. 
2. Some tutorials on the internet about a month ago were already outdated. However, google gemini could still help me figure out the few changes needed in my code base 
3. With all the time lost to just figuring out the backEnd (again I'm a doctor, not a professional programmer), I had very little time to write the frontEnd. Fortunately, I could vibe code a front end using gemini canvas. I told it to make a webapp chatbot app UX/UI that supports drag and drop (for images) and can communicate with a fastAPI endpoint for google adk. The frontEnd didn't work well at first but with a few vibecoding tweaks, I was able to get it to work with the backEnd. 


## Accomplishments that I'm proud of
As a doctor (not a native programmer), I successfully built a minimum viable product (MVP) for the chatBot agents working dynamically in just two weeks. This would never have been possible given the time constraint if I didn't have such an extensive framework in google adk as well as google gemini as my coding assist. Don't get me wrong, I still be believe that just as we need professional radiologists for professional medical diagnostic work, I also believe that we need professional programmers for important large scale AI projects. It's just that seeing how agentic workflows are even a possibility for a simple AI enthusiast like me given an AI coding agent like google gemini and google adk is mind blowing. 

## What I learned
In two weeks I learned the following:
1. google adk agents, multi-agents (subagents), tool use, mcp (model context protocol)
2. fastAPI servers
3. connecting a frontEnd html webpage to a fastAPI server (different origins)
4. Figured out how to programmatically generate a "program architecture" using google gemini (yes gemini can vibe code program architectures).
5. the pros and cons of running google adk locally and in the cloud, serving free open source models versus google gemini.... gemini just works flawlessly. I had to switch between LLM's for local use since some models were good for vision while others were good for tool use. With gemini, one model does it all. 
6. Perhaps one of the most important things I learned from this endeavor is that vibe coding is still not enough. I couldn't just vibe code my way to an actual product without actually understanding the code, and what I was doing. AI is not a replacement for actually learning a new skill. 
7. Finally, about AI taking over, taking our jobs away (in radiology or in any profession)....I believe that if used properly, as a means to boost learning and not a crutch for lazy thinking,
AI is not our replacement,
AI is not  in our way,
It is OUR way in….
To the future.

 

## What's next for Rad_Gemini
So I believe that given a little more time and effort,
I could have added more agents to my workflow,
Given them more tools to use,
more functionality,
more complexity…
But this project is not a testament for complexity 
it is a testament to possibility to sheer potential and viability.
The fact that a person like myself was able to build and learn this in just under two weeks with the help of google gemini,  and Google Adk …. Opens an entire world of opportunity.

Potential TODO List:
1. I'd like to improve the UX/UI... I didn't have time for this so close to the end of the hackathon. I'd like to work on a mobile first web app that can leverage the phone's camera for streaming. I might try google stitch.
2. I'd like to add more MCP server tools and agents to my team of agents. Populate the team with medical related MCP server tools that focus on sites like PubMed. 
3. Didn't have time to explore more features from google cloud or vertex AI but I would like to figure this out to give the AI agents more granular control. 
4. I might consider adding live streaming or even voice input for the chat bot. 
5. Work on the system prompts for my AI agents for better guard rails when dealing with the "user".
6. I could convert the chatbot web app into a reusable web component (I'll ask gemini canvas to do this). I can then use the chat bot in other apps I might consider building.... like a full blown DICOM reader for radiologic images. 
7. Consider end-to-end encryption for chat conversations.


# The online live demo is at ______________________
1. For the online demo, the email subagent is not allowed to send emails to anyone but the
designated email. This is to protect the email subagent from being used inappropriately.
However, if you want use your own zapier MCP server for gmail (and give it more freedom or control over your gmail account), 
go to to your .env file (placed at the root of the project)  and set it as such

```

########################
# Zapier tools
###################


# For Zapier MCP server
ZAPIER_MCP_SERVER_URL=_________________________  #replace with the URL of your Zapier MCP server 


```


# To try this google-adk fastAPI locally do the followingL:
1. git clone the repository
2. go to the root folder and install the requirements by running

```
pip install -r requirements.txt
```
3. create a .env file with the following information:

```

####################
#GOOGLE API
####################
# For google gemini api testing
#Uncomment out the following. Set GOOGLE_GENAI_USE_VERTEXAI to FALSE if you are using a google studio api key instead of a vertexai key. 
# GOOGLE_GENAI_USE_VERTEXAI=FALSE
# GOOGLE_API_KEY=...


###################
#OLLAMA API  if you want to test with locally run models. 
####################

# For local model api testing using OPENAI api base and LiteLlm_chat wrapper for ollama
# OPENAI_API_BASE=http://localhost:11434/v1 
# OPENAI_API_KEY=anything

# For local model api testing using Ollama_chat
# OLLAMA_API_BASE="http://localhost:11434"
# I noticed this doesn't work with images even if the model is a vision model.
```

4. Go to the  `Agents` Folder and

```
python adk_api.py

```

This will run the fast API server. 

5. You can already test the url out since the built in web service is set to true so ADK WEB will be running at the URL.

6. However, if you want to try the frontEnd web APP, you can go to the `frontEnd` folder.
You can serve or run the `index.html` file inside. This should already run if your on a local server since
  ```
        const ADK_AGENT_URL = 'http://localhost:8000/run';
        const ADK_SESSION_CREATION_URL_BASE = 'http://localhost:8000'; // Base URL for session creation
  ```

 but if you want to run the whole project online, make sure to change these in `index.html` to
 match the URL for the fastAPI endpoints of the hosted google-adk. 


 test update
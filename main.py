from fastapi import FastAPI, Form
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import json
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import os
from platform import python_version
from typing import Annotated

app = FastAPI()

origins = [
    "https://wander-api.onrender.com",
    "http://localhost",
    "https://localhost",
    "http://localhost:3001",
    "https://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


print("Python version: ", python_version())
load_dotenv()
OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(temperature=0.5)


@app.get("/")
async def read_root():
    return {"message": "Hello Hack for Good! Please use a valid endpoint."}


@app.post("/tour/")
async def tour(
    location: Annotated[str, Form()],
    interests: Annotated[str, Form()],
    budget: Annotated[int, Form()],
    duration: Annotated[int, Form()],
    distance: Annotated[int, Form()],
    start_time: Annotated[str, Form()],
):
    chat_prompt = f"""
        You are an expert and enthusiastic tour guide planning walking tours around {location}.
        """
    system_prompt = SystemMessagePromptTemplate.from_template(chat_prompt)

    human_template = f"""
        I am interested in {interests}. I have {duration} hours and would like to walk no more than {distance} miles. My budget is {budget} dollars. I want to start in the {start_time}. Please create a suggested walking tour in {location} based on the previous parameters. I would like the results formatted as valid json with each location having the following properties: location_name, category, story, suggested_visit_duration, and geolocation. geolocation should be an object with latitude and longitude properties. Latitude and Longitude should be in number format only. The story should be fun and detailed.
        """
    print("HUMAN ASK", human_template)
    human_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(
        input_language="English", output_language="English", max_tokens=100
    )

    # check response is in json format
    try:
        # Load JSON string
        data = json.loads(response)
        print(data)
        return data
    except json.JSONDecodeError as e:
        print("Response is not in json format", e)
        return {"message": "Response is not in json format"}

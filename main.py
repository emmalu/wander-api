from fastapi import FastAPI, Form
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

print("Python version: ", python_version())
load_dotenv()
OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(temperature=0.5)


@app.get("/")
async def root():
    return {"message": "Hack for Good! Please use a valid endpoint."}


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

    interests = interests.split(", ")
    if len(interests) > 1:
        interests = f"""{", ".join(interests[:-1])} and {interests[-1]}"""

    human_template = f"""
        I am interested in {interests}. I have {duration} hours and would like to walk no more than {distance} miles. My budget is {budget} dollars. I want to start in the {start_time}. Please give me a list of locations for a {location} walking tour based on the previous parameters. With each location, its category, a fun and detailed story about the location, a recommended time to spend at the location, and its geolocation. Format the results as a json response complete with location name, category, suggested_visit_duration, story and geolocation fields.
        """
    print("HUMAN ASK", human_template)
    human_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(
        input_language="English", output_language="English", max_tokens=100
    )
    print(response)

    # check response is in json format
    try:
        json.loads(response)
        return {response}
    except ValueError as e:
        print("Response is not in json format")
        return {"message": "Response is not in json format"}

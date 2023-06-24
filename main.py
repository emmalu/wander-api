from fastapi import FastAPI, Form
from dotenv import load_dotenv
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
    # location = "Philadelphia, PA"
    return location, interests, budget, duration, distance, start_time
    # chat_prompt = f"""
    #     You are an expert in planning walking tours around {location}.
    #     """
    # system_prompt = SystemMessagePromptTemplate.from_template(chat_prompt)

    # if len(interests) > 1:
    #     interests = f"""{", ".join(interests[:-1])} and {interests[-1]}"""

    # # check if any of the parameters are empty
    # if not interests or not budget or not duration or not distance or not time_of_day:
    #     # return error
    #     return "Please fill out all fields"

    # human_template = f"""
    #     I am interested in {interests}. I have {duration} hours and would like to walk no more than {distance} miles. My budget is {budget} dollars. I want to start in the {time_of_day}. Please give me a list of locations for a {location} walking tour based on the previous parameters. With each location, provide a recommended start time recommended time at the location, a category, a fun, detailed story about the location, and its geolocation. Present each location as an enthusiastic tour guide. Format the results into a json response complete with location name, category, suggested_start_time, suggested_visit_duration, story and geolocation field.
    #     """
    # # print("HUMAN ASK", human_template)
    # human_prompt = HumanMessagePromptTemplate.from_template(human_template)
    # chat_prompt = ChatPromptTemplate.from_messages([system_prompt, human_prompt])

    # chain = LLMChain(llm=chat, prompt=chat_prompt)
    # response = chain.run(
    #     input_language="English", output_language="English", max_tokens=100
    # )

    # return {response}

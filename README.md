# wander-api

This is the backend API for the [WanderGuide](https://github.com/DaveedBalcher/WanderGuide/) iOS app that allows users to generate a customized walking tour for a particular city or town center.

## LangChain API - Python concept api

This is an example walking tour generator api using [LangChain](https://python.langchain.com/docs/get_started/introduction.html), built around the OpenAI API [quickstart tutorial](https://beta.openai.com/docs/quickstart). It uses the [FastAPI](https://fastapi.tiangolo.com/) web framework. Check out the tutorial or follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd wander-api
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ source venv/bin/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ uvicorn main:app --reload
   ```

You should now be able to access the api at [http://localhost:8000](http://localhost:8000)!

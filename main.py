from openai import AsyncOpenAI
from agents import (
    Agent,
    ModelSettings,
    OpenAIChatCompletionsModel,
    Runner,
    set_tracing_disabled,
)
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

API_KEY = os.environ.get("OPENAI_API_KEY", "dummy")
BASE_URL = os.environ.get("BASE_URL")
MODEL = os.environ.get("MODEL")


client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)
model = OpenAIChatCompletionsModel(model=MODEL, openai_client=client)
agent = Agent(
    name="Assistant",
    model=model,
    instructions="You are a helpful assistant",
    model_settings=ModelSettings(temperature=0.7, max_tokens=512),
)
set_tracing_disabled(True)


class RequestContext(BaseModel):
    prompt: str
    temperature: float | None = None
    max_tokens: int | None = None


class UsageInfo(BaseModel):
    input_tokens: int
    output_tokens: int


class ResponseModel(UsageInfo):
    message: str
    input_prompt: str


app = FastAPI()


@app.post("/chat")
async def post_chat(context: RequestContext) -> ResponseModel:
    if context.temperature:
        agent.model_settings.temperature = context.temperature
    if context.max_tokens:
        agent.model_settings.max_tokens = context.max_tokens

    result = await Runner.run(agent, context.prompt)
    usage = result.context_wrapper.usage

    return {
        "message": result.final_output,
        "input_prompt": context.prompt,
        "input_tokens": usage.input_tokens,
        "output_tokens": usage.output_tokens,
    }

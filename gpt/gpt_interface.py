import os

from dotenv import load_dotenv
import openai
from openai.types import CompletionUsage


load_dotenv("api_key.env")
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI(api_key=OPENAI_API_KEY)


def query_gpt(messages: list[dict[str, str]], temperature: float = 0.7, top_p: float = 0.95) -> tuple[str, CompletionUsage]:
    response = client.chat.completions.create(
        messages=messages,  # type: ignore
        model="gpt-4o-2024-08-06",
        temperature=temperature,
        top_p=top_p
    )
    
    # print(response.usage)
    output = response.choices[0].message.content
    if not output or not response.usage:
        raise ValueError("GPT call returned no output.")

    return output, response.usage

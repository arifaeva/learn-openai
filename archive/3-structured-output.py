import os

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel


class FoodRecipe(BaseModel):
    dish_name: list[str]
    ingredients: list[str]
    cooking_steps: list[str]


load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)

messages = [{"role": "user", "content": "Tell me how to make Nasi Goreng"}]

response = client.beta.chat.completions.parse(
    model="gpt-4o-mini", messages=messages, response_format=FoodRecipe
)

parsed_output = response.choices[0].message.parsed.dict()
print(parsed_output.get("dish_name"))
print(parsed_output.get("ingredients"))
print(parsed_output.get("cooking_steps"))

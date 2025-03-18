import os

from dotenv import load_dotenv
from pydantic_ai.models.anthropic import AnthropicModel

load_dotenv()
model = AnthropicModel(
    model_name=os.getenv('ANTROPIC_MODEL'),
    api_key=os.getenv('ANTROPIC_TOKEN'),
)
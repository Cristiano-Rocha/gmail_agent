from pydantic_ai import Agent

from src.llm.anthropic_client import model
from src.models.models import GmailDeps, Email
from src.tools.gmail_tools import gmail_tools

gmail_agent = Agent(
    model=model,
    result_type=Email,
    deps_type=GmailDeps,
    tools=gmail_tools,
    system_prompt="""
        Use the tools avaliable to list my emails
    """,
    retries=3
)

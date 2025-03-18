from dataclasses import dataclass
from datetime import datetime
from typing import List

from googleapiclient.discovery import Resource
from pydantic import BaseModel, Field, ConfigDict


class Email(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    sender: str = Field("email of the sender of the email")
    title: str = Field("Subject of the email")
    result: str = Field("Result of the AI agent")

class Label(BaseModel):
    name: str = Field("LabelId of the email")

class Message(BaseModel):
    title: str = Field("Title of the email")
    labels: List[Label] = Field("Labels associated with email")
    date: datetime = Field("Date time when the email was received")

class EmailsResult(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    emails: List[Email] = Field("List of results")
    total: int = Field("Total number of results")

@dataclass
class GmailDeps:
    gmail_service: Resource



import os
from datetime import datetime

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError
from pydantic_ai import RunContext

from src.models.models import GmailDeps


SCOPES = ["https://mail.google.com/"]



def get_gmail_service():
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  current_dir = os.path.dirname(os.path.abspath(__file__))
  token = os.path.join(current_dir, '..', '..', 'token.json')
  credentials = os.path.join(current_dir, '..', '..', 'credentials.json')
  creds = None
  if os.path.exists(token):
    creds = Credentials.from_authorized_user_file(token, SCOPES)
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          credentials, SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(token, "w") as token:
      token.write(creds.to_json())

  try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)
    return service
  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")

def init_service() -> Resource:
    return get_gmail_service()

def list_messages(ctx: RunContext[GmailDeps], query='', page_token=None, all_mesages=[]):
  try:
    response = ctx.deps.users().messages().list(userId='me', q=query, pageToken=page_token).execute()
    all_mesages.extend(response.get('messages', []))
    next_page_token = response.get('nextPageToken')
    if next_page_token:
      return list_messages(ctx,query, next_page_token, all_mesages)
    return all_mesages

  except HttpError as error:
    print(f'An error occurred: {error}')
    return None

def get_message(ctx: RunContext[GmailDeps], msg_id):
  try:
    _messages = ctx.deps.users().messages().get(userId='me', id=msg_id, format='full').execute()
    return _messages
  except HttpError as error:
    print(f'An error occurred: {error}')
    return None

def get_messages_from_sender(ctx: RunContext[GmailDeps], sender):
  query = f"FROM:{sender}"
  _messages = list_messages(ctx, query)
  return _messages

def get_messages_contains(ctx: RunContext[GmailDeps], term):
    gmail_service = ctx
    return list_messages(gmail_service, term)

def get_messages_between_dates(ctx: RunContext[GmailDeps], term, start_date, end_date=datetime.now().strftime("%d/%m/%Y")):
  query = f"(after:{start_date} (before:{end_date} ) AND {term}"
  gmail_service = ctx
  return list_messages(gmail_service, query)


def delete_messages(ctx: RunContext[GmailDeps], _messages):
    gmail_service = ctx
    try:
        gmail_service.deps.users().messages().batchDelete(userId="me", body={"ids": _messages}).execute()
        print(f"Emails with {_messages} deleted")
    except Exception as e:
        print(f"Error while trying to delete messages: {_messages}")
        print(e)

def get_total_messages_between_dates(ctx: RunContext[GmailDeps], start_date, end_date=datetime.now().strftime("%d/%m/%Y")):
  query = f"(after:{start_date} before:{end_date} )"
  print(query)
  gmail_service = ctx
  messages = list_messages(gmail_service, query)
  return len(messages)

def show_messages(ctx: RunContext[GmailDeps], _messages):
  gmail_service = ctx
  if _messages:
    for msg in _messages:
      message_data = get_message(gmail_service, msg['id'])
      print(f'Message ID: {msg["id"]}')

      if message_data['snippet']:
        print(f"Snippet: {message_data['snippet']}")
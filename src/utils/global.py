import json
import os

def load_credential():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    credentials_path = os.path.join(current_dir, '..', '..', 'credentials.json')
    try:
        with open(credentials_path, 'r') as f:
            credentials = json.load(f)
        return credentials
    except FileNotFoundError:
        print(f"Error: Credential file not found at path {credentials_path}")
        return None

def load_token():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    credentials_path = os.path.join(current_dir, '..', '..', 'token.json')
    try:
        with open(credentials_path, 'r') as f:
            credentials = json.load(f)
        return credentials
    except FileNotFoundError:
        print(f"Error: token file not found at path{token}")
        return None
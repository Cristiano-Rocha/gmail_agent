# Gmail Agent Project

This project uses the Pydantic-AI library and the Gmail API to create an AI agent that can interact with your Gmail account.

## Features

-   List emails based on various criteria (sender, keywords, date range).
-   Retrieve specific email details.
-   Delete emails.

## Prerequisites
-   Python 3.9+
-   A Google Cloud project with the Gmail API enabled.
-   An Anthropic API key.

## Installation

1.  **Clone the repository:**
2.  **Create a virtual environment (recommended):**
3.  **Install dependencies:**
4.  **Set up Gmail API credentials:**

    -   Download your `credentials.json` file from the Google Cloud Console and place it in the root of the project.
    -   The first time you run the script, it will open a browser window to authenticate your Gmail account.
    -   After successful authentication, a `token.json` file will be created to store your credentials.

5.  **Set up environment variables:**
    -   Create a `.env` file in the root of the project.
    -   Add your Anthropic API key:

## Usage

1.  **Run the agent:**
    The script will prompt you to authenticate with your Gmail account if you haven't already.

## Configuration

-   **Model:** You can change the Anthropic model in `agent/agent.py`.
-   **System Prompt:** Modify the `system_prompt` in `agent/agent.py` to change the agent's behavior.
-   **Tools:** Add or modify tools in `agent/tools.py`.

## Contributing

Feel free to contribute to this project by opening issues or submitting pull requests.

## License

MIT



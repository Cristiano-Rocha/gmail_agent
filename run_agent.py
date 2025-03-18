from pydantic_ai import UnexpectedModelBehavior
from src.agent.gmail_agent import gmail_agent
from src.utils.gmail_actions import init_service

def main():
    prompt = 'List my last 10 emails'
    try:
        response = gmail_agent.run_sync(prompt, deps=init_service())
        print(response.data.result)
    except (
            UnexpectedModelBehavior) as e:
        print(e)

if __name__ == '__main__':
    main()

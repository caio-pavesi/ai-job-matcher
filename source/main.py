'''Lorem ipsum dolor sit amet, consectetur adipiscing elit.'''

# Standard
# imports here

# Project
from utils import llm_match_function
from settings import OPENAI_API_KEY

# External
from langchain_openai import ChatOpenAI

LLM = ChatOpenAI(
    name = "gpt-4.1",
    temperature = 0.0,
    api_key = OPENAI_API_KEY,
    model_kwargs = {
        "functions": [llm_match_function()],
        "function_call": {"name": "assess_candidate_fit"},
    }
)

APPLICATION_DOCS = None

# Match
def do_match(job_description, application_docs):
    '''Perform the job matching process.'''
    raise NotImplementedError()

def main() -> None:
    '''Main entry point for the application.'''
    raise NotImplementedError()

if __name__ == "__main__":
    main()

'''Lorem ipsum dolor sit amet, consectetur adipiscing elit.'''

# Standard

# Project
from etl.bmw import main as etl_bmw
from utils import llm_match_function, retrieve
from settings import (
    OPENAI_API_KEY,
    BASE_DIR,
    APPLICATION_FILES_FOLDER_PATH
)

# External
from pydantic.types import SecretStr
from langchain_openai import ChatOpenAI
from langchain_core.prompts.prompt import PromptTemplate
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

LLM = ChatOpenAI(
    model="gpt-5",
    api_key=SecretStr(OPENAI_API_KEY),
).bind_tools([llm_match_function()], tool_choice="assess_candidate_fit")

PROMPT_TEMPLATE = PromptTemplate(
    template = (BASE_DIR / 'tools/match.jinja').read_text('utf-8'),
    template_format = "jinja2",
    input_variables = ["candidate_application", "job_description"],
)

APPLICATION_DOCS = DirectoryLoader(str(APPLICATION_FILES_FOLDER_PATH), glob="*.pdf", loader_cls=PyPDFLoader).load()

FILTER_QUERY = (BASE_DIR / 'sql/filter.sql').read_text('utf-8')

# Match
def do_match(job_description):
    '''Perform the job matching process.'''

    prompt = PROMPT_TEMPLATE.format(
        candidate_application=APPLICATION_DOCS,
        job_description=job_description,
    )

    response = LLM.invoke(prompt)

    return response

def main() -> None:
    '''Main entry point for the application.'''

    # ETL
    # etl_bmw()

    # Do match based on criteria of filters
    for job in retrieve(FILTER_QUERY):
        a = do_match(job[1]['job_description'])
        with open('response.json', 'w', encoding='utf-8') as f:
            f.write(str(a.to_json()))
        break

if __name__ == "__main__":
    main()

'''Lorem ipsum dolor sit amet, consectetur adipiscing elit.'''

# Standard
import sqlite3
from datetime import datetime
from typing import cast

# Project
from etl.bmw import main as etl_bmw
from utils import llm_match_function, retrieve, stop_loop
from settings import (
    OPENAI_API_KEY,
    BASE_DIR,
    APPLICATION_FILES_FOLDER_PATH,
    DATABASE_PATH,
)

# External
from pydantic.types import SecretStr
from langchain_openai import ChatOpenAI
from langchain_core.prompts.prompt import PromptTemplate
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

LLM = ChatOpenAI(
    model="gpt-5-nano",
    api_key=SecretStr(OPENAI_API_KEY),
).bind_tools([llm_match_function()], tool_choice="assess_candidate_fit")

PROMPT_TEMPLATE = PromptTemplate(
    template = (BASE_DIR / 'tools/match.jinja.md').read_text('utf-8'),
    template_format = "jinja2",
    input_variables = ["candidate_application", "job_description"],
)

APPLICATION_DOCS = DirectoryLoader(str(APPLICATION_FILES_FOLDER_PATH), glob="*.pdf", loader_cls=PyPDFLoader).load()

FILTER_QUERY = (BASE_DIR / 'sql/filter.sql').read_text('utf-8')
INSERT_QUERY = (BASE_DIR / 'sql/insert_match.sql').read_text('utf-8')

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
    etl_bmw()

    # Do match based on criteria of filters
    with sqlite3.connect(DATABASE_PATH, autocommit = True) as conn:

        for idx, job in enumerate(retrieve(FILTER_QUERY)):
            match = do_match(job[1]['job_description'])
            match = cast(dict, match.tool_calls[0]['args'])

            # Add missing parameters from job
            match.update({'job_portal_id': job[1]['job_portal_id']})
            match.update({'match_date': datetime.now().isoformat()})

            # Insert into matches table
            conn.execute(INSERT_QUERY, match)

            # Nobody likes infinite loops, and wasted OpenAI credits
            stop_loop(idx, 10)

if __name__ == "__main__":
    main()

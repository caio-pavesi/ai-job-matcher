'''Utility functions'''

# Standard
import json
import logging
from typing import Generator

# Project
from type import JobPosting
from settings import SQLITECLOUD_CONNECTION_STRING, BASE_DIR

# External
import sqlalchemy as sql

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

def already_inserted_in_database(job_link: str) -> bool:
    '''Lorem ipsum'''

    engine = sql.create_engine(SQLITECLOUD_CONNECTION_STRING)
    connection = engine.connect()

    query = sql.text('''SELECT 1 FROM jobs WHERE job_link = :job_link''')
    value = connection.execute(query, {'job_link': job_link}).fetchone()

    connection.close()
    engine.dispose()

    return value is not None

def load(data: Generator[JobPosting, None, None]) -> bool:
    '''Lorem ipsum'''

    engine = sql.create_engine(SQLITECLOUD_CONNECTION_STRING)
    connection = engine.connect()

    query = sql.text('''INSERT INTO jobs (job_portal_id, job_link, job_title, job_description, job_posting_date, job_type, job_field, job_city) VALUES (:job_portal_id, :job_link, :job_title, :job_description, :job_posting_date, :job_type, :job_field, :job_city)''')

    for job in data:
        try:
            connection.execute(query, job.json())
            logger.debug('Inserted job: %s', job.job_portal_id)
        except Exception:
            logger.error('Error inserting job', exc_info = True)

    connection.close()
    engine.dispose()

    return True

def stop_loop(iteration: int, limit: int) -> None:
    '''Stops the loop if the iteration count reaches the limit, i dont want infinite loops or waste all my OPENAI credits because of them.
    Args:
        iteration (int): The current iteration count.
        limit (int): The maximum number of iterations allowed.
    Raises:
        StopIteration: If the iteration count reaches the limit.'''

    if iteration >= limit:
        raise StopIteration("Reached the limit of iterations.")

def llm_match_function() -> dict:
    '''Schema for the match function.'''
    with open(BASE_DIR / 'tools/match.json', 'r', encoding = 'utf-8') as file:
        return json.load(file)

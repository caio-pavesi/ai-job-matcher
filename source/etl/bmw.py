'''BMW job listing extractor, transformer, and loader.'''

# Standard
import re
import logging
from datetime import datetime, date
from typing import Sequence, Generator, cast

# Project
from type import JobPosting
from utils import load, already_inserted_in_database

# External
import requests as req
from bs4 import BeautifulSoup as bs
from bs4.element import Tag

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

URL = 'https://www.bmwgroup.jobs/en/_jcr_content/main/layoutcontainer_5337/jobfinder30.jobfinder_table.content.html?filterSearch=obType_INTERNSHIP,postingDate_7'

# Extract
def extract() -> Sequence[Tag]:
    '''This function fetches job listings from the BMW Group website.

    Returns:
        Sequence[Tag]: Sequence of job postings as bs4 Tag objects.
    '''

    jobs = req.get(URL, timeout = 60).content.decode('utf-8')
    jobs = bs(jobs, 'html.parser')
    jobs = jobs.find_all('div', class_ = 'grp-jobfinder__wrapper')
    jobs = cast(Sequence[Tag], jobs)

    return jobs

# Transform
def get_job_portal_id(html: Tag) -> int:
    '''Lorem ipsum'''

    value = html.get('data-job-id')

    if value is None:
        return 0

    elif isinstance(value, list):
        return int(value[0]) if value else 0

    return int(value)

def get_job_link(html: Tag) -> str:
    '''Lorem ipsum'''

    value = cast(Tag, html.find('a'))
    value = cast(str, value.get('href'))

    return 'https://www.bmwgroup.jobs' + value

def get_job_title(html: Tag) -> str:
    '''Lorem ipsum'''

    value = cast(Tag, html.find('div', class_='grp-jobfinder__cell-title'))
    value = cast(str, value.text)

    return value

def get_job_description(html: str):
    '''Lorem ipsum'''

    value = bs(html, 'html.parser')
    value = cast(Tag, value.find('div', class_ = 'container-layout container no-top-spacing no-bottom-spacing'))

    # ? - We just need the raw HTML content, so we remove all attributes
    # ? - ```list(tag.attrs.keys())``` to avoid modifying dict during iteration
    for tag in cast(Sequence[Tag], value.find_all(True)):
        for attr in list(tag.attrs.keys()):
            del tag.attrs[attr]

    value = (
        value.decode_contents()
        .encode('ascii', 'ignore')
        .decode('utf-8')
        .replace('\n', '')
        .replace('\t', '')
        .replace('\r', '')
        .strip()
    )

    return value

def get_job_posting_date(html: Tag) -> date:
    '''Lorem ipsum'''

    value = cast(Tag, html.find('div', class_ = 'grp-jobfinder__cell-publication'))
    value = cast(str, value.get_text().strip())
    value = cast(re.Match, re.search(r'\d{2}\.\d{2}\.\d{4}', value))
    value = value.group()

    return datetime.strptime(value, "%d.%m.%Y").date()

def get_job_type(html: Tag) -> str:
    '''Lorem ipsum'''

    value = cast(Tag, html.find('div', class_='grp-jobfinder-cell-refno'))
    value = cast(str, value.get('data-job-type'))

    return value

def get_job_field(html: Tag) -> str:
    '''Lorem ipsum'''

    value = cast(Tag, html.find('div', class_='grp-jobfinder-cell-refno'))
    value = cast(str, value.get('data-job-field'))

    return value

def get_job_city(html: Tag) -> str:
    '''Lorem ipsum'''

    value = cast(Tag, html.find('div', class_='grp-jobfinder-cell-refno'))
    value = cast(str, value.get('data-job-location'))

    return value

def transform(job_listing: Sequence[Tag]) -> Generator[JobPosting, None, None]:
    '''Lorem ipsum'''

    for job_data in job_listing:

        job_link = get_job_link(job_data)
        logger.info('Processing job link: %s', job_link)

        if already_inserted_in_database(job_link):
            logger.info('Job already inserted: %s', job_link)
            continue

        job_description_page = req.get(job_link, timeout = 60).content.decode('utf-8')

        job_posting = JobPosting(
            job_link = job_link,
            job_portal_id = get_job_portal_id(job_data),
            job_title = get_job_title(job_data),
            job_description = get_job_description(job_description_page),
            job_posting_date = get_job_posting_date(job_data),
            job_type = get_job_type(job_data),
            job_field = get_job_field(job_data),
            job_city = get_job_city(job_data),
        )

        logger.debug('Job posting created: %s', job_posting)

        yield job_posting

# Main
def main():
    '''Lorem ipsum'''

    data = extract()
    data = transform(data)
    load(data)

if __name__ == '__main__':
    main()

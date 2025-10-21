'''BMW job listing extractor, transformer, and loader.'''

# Standard
import logging
from datetime import date
from typing import Any, List, Dict, Generator

# Project
from type import JobPosting
from utils import load, already_inserted_in_database

# External
import requests as req

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

URL = 'https://porsche-beesite-production-gjb.app.beesite.de/search/?data={"LanguageCode":"DE","SearchParameters":{"FirstItem":1,"CountItem":1000,"Sort":[{"Criterion":"PublicationStartDate","Direction":"DESC"}],"MatchedObjectDescriptor":["ID","PositionTitle","PositionURI","PositionShortURI","PositionLocation.CountryName","PositionLocation.CityName","PositionLocation.Longitude","PositionLocation.Latitude","PositionLocation.PostalCode","PositionLocation.StreetName","PositionLocation.BuildingNumber","PositionLocation.Distance","JobCategory.Name","PublicationStartDate","ParentOrganizationName","ParentOrganization","OrganizationShortName","CareerLevel.Name","JobSector.Name","PositionIndustry.Name","PublicationCode","PublicationChannel.Id"]},"SearchCriteria":[{"CriterionName":"PublicationChannel.Code","CriterionValue":["12"]}]}'

# Extract
def extract() -> List[Dict[str, Any]]:
    '''This function fetches job listings from the Porsche website.

    Returns:
        List[Dict[str, Any]]: List of dictionaries containing job postings data.
    '''

    jobs = req.get(URL, timeout = 60)
    jobs = jobs.json()['SearchResult']['SearchResultItems']

    return jobs

# Transform
def get_job_portal_id(job: Dict[str, Any]) -> int:
    '''Lorem ipsum'''

    value = job['MatchedObjectId']

    return int(value)

def get_job_link(job: Dict[str, Any]) -> str:
    '''Lorem ipsum'''

    value = job['MatchedObjectDescriptor']['PositionURI']

    return value

def get_job_title(job: Dict[str, Any]) -> str:
    '''Lorem ipsum'''

    value = job['MatchedObjectDescriptor']['PositionTitle']

    return value

def get_job_description(html: str) -> str:
    '''Lorem ipsum'''

    # TODO: Extract only relevant parts

    return html

def get_job_posting_date(job: Dict[str, Any]) -> date:
    '''Lorem ipsum'''

    return date.fromisoformat(job['MatchedObjectDescriptor']['PublicationStartDate'])

def get_job_type(job: Dict[str, Any]) -> str:
    '''Lorem ipsum'''

    return job['MatchedObjectDescriptor']['CareerLevel'][0]['Name']

def get_job_field(job: Dict[str, Any]) -> str:
    '''Lorem ipsum'''

    return job['MatchedObjectDescriptor']['JobCategory'][0]['Name']

def get_job_city(job: Dict[str, Any]) -> str:
    '''Lorem ipsum'''

    return job['MatchedObjectDescriptor']['PositionLocation'][0]['CityName']

def transform(job_listing: List[Dict[str, Any]]) -> Generator[JobPosting, None, None]:
    '''Lorem ipsum'''

    for job_data in job_listing:

        job_link = get_job_link(job_data)
        logger.info('Processing job link: %s', job_link)

        if already_inserted_in_database(job_link):
            logger.info('Job already inserted: %s', job_link)
            continue

        job_description_page = req.get(job_link, timeout = 60).content.decode('utf-8')

        try:
            job_posting = JobPosting(
                job_link = job_link,
                job_portal_id = get_job_portal_id(job_data),
                job_title = get_job_title(job_data),
                job_description = get_job_description(job_description_page),
                job_posting_date = get_job_posting_date(job_data),
                job_extraction_date = date.today(),
                job_type = get_job_type(job_data),
                job_field = get_job_field(job_data),
                job_city = get_job_city(job_data),
            )
        except Exception as exception:
            logger.error('Error processing job link %s', job_link, exc_info=exception)
            continue

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

"""Useful functions for the source package."""

import requests
from bs4 import BeautifulSoup

def get_job_page(link: str) -> str:
    """Simply fetches the job page content from the given link.
    Args:
        link (str): The URL of the job page.
    Returns:
        str: The HTML content of the job page."""

    return requests.get(link, timeout = 60).content.decode('utf-8')

def get_job_description(link: str) -> str:
    """This function extracts the job description from the job page HTML, but keeps the formatting.
    Args:
        job_page (Html): The HTML content of the job page.
    Returns:
        str: The formatted job description as a html string."""

    content = get_job_page(link)

    if link.startswith('https://www.bmwgroup.jobs/'):
        description =  BeautifulSoup(content, 'html.parser').find('div', class_ = 'container-layout container no-top-spacing no-bottom-spacing')
    elif link.startswith('https://jobs.porsche.com/'):
        description =  BeautifulSoup(content, 'html.parser').find('article')
    elif link.startswith('https://jobs.ferrari.com/'):
        description =  BeautifulSoup(content, 'html.parser').find('div', class_ = 'job')
    else:
        raise ValueError('Unsupported job page link.')

    # Removing all attributes that are not needed since i just need the formatted HTML.
    for tag in description.find_all(True):
        if 'class' in tag.attrs:
            del tag.attrs['class']
        if 'itemprop' in tag.attrs:
            del tag.attrs['itemprop']
        if 'type' in tag.attrs:
            del tag.attrs['type']
        if 'href' in tag.attrs:
            del tag.attrs['href']
        if 'id' in tag.attrs:
            del tag.attrs['id']

    return (
        description.decode_contents()
        .replace('\n', '')
        .replace('\t', '')
        .replace('\r', '')
        .strip()
    )

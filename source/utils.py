"""Useful functions for the source package."""

import requests

def get_job_page(link: str) -> str:
    """Simply fetches the job page content from the given link.
    Args:
        link (str): The URL of the job page.
    Returns:
        str: The HTML content of the job page."""

    return requests.get(link, timeout = 60).content.decode('utf-8')

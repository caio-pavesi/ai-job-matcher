'''Defines the custom types used in the application.'''

from datetime import date
from dataclasses import dataclass

@dataclass
class JobPosting:
    '''A class representing a job posting with its details.'''
    job_portal_id: int
    job_link: str
    job_title: str
    job_description: str
    job_posting_date: date
    job_type: str
    job_field: str
    job_city: str

    def json(self) -> dict:
        '''Returns the job posting details as a JSON-serializable dictionary.'''
        return {
            'job_portal_id': self.job_portal_id,
            'job_link': self.job_link,
            'job_title': self.job_title,
            'job_description': self.job_description,
            'job_posting_date': self.job_posting_date.isoformat(),
            'job_type': self.job_type,
            'job_field': self.job_field,
            'job_city': self.job_city,
        }

    def tuple(self) -> tuple:
        '''Returns the job posting details as a tuple for SQL insertion.'''
        return (
            self.job_portal_id,
            self.job_link,
            self.job_title,
            self.job_description,
            self.job_posting_date.isoformat(),
            self.job_type,
            self.job_field,
            self.job_city,
        )


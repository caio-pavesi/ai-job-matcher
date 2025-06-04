""""Defines the types used"""

from typing import List, Literal

JobFilterType = Literal[
    'jobType_INTERNSHIP',
    'jobType_GRADUATE_JOB',
    'jobType_SUMMER_JOB',
    'jobType_STANDARD',
    'jobType_APPRENTICESHIP',
    'postingDate_7',
    'postingDate_14',
    'postingDate_30',
]

JobFilter = List[JobFilterType]

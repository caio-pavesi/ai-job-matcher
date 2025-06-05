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
    'jobField_Aftersales',
    'jobField_Construction',
    'jobField_Consultancy',
    'jobField_Communications',
    'jobField_CorporateStrategy',
    'jobField_CustomerService',
    'jobField_Design',
    'jobField_ResearchDevelopment',
    'jobField_Ausbildungsbereiche',
    'jobField_Finance',
    'jobField_InformationTechnology',
    'jobField_LegalServices',
    'jobField_Logistics',
    'jobField_Marketing',
    'jobField_Other',
    'jobField_HumanResources',
    'jobField_Production',
    'jobField_Purchase',
    'jobField_Quality',
    'jobField_RiskManagement',
    'jobField_SalesDistribution',
    'jobField_ServiceAdministration',
    'jobField_SustainabilityEnvironment',
    'location_AT',
    'location_AT/Salzburg',
    'location_AT/Steyr',
    'location_AT/Vienna',
    'location_CA/Richmond+Hill',
]

JobFilter = List[JobFilterType]

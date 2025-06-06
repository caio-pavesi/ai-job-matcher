CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY,
    job_portal_id INTEGER,
    job_link TEXT,
    job_page_source TEXT,
    job_title TEXT,
    job_description TEXT,
    job_posting_date DATE,
    job_type TEXT,
    job_field TEXT,
    job_city TEXT
);

CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY,
    job_portal_id INTEGER,
    score FLOAT,
    strengths TEXT,
    weaknesses TEXT,
    improvement TEXT,
    conclusion TEXT,
    interview TEXT,
    FOREIGN KEY (job_portal_id) REFERENCES jobs(job_portal_id)
);
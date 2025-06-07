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
    match_score FLOAT,
    match_strengths TEXT,
    match_weaknesses TEXT,
    match_improvement_points TEXT,
    match_conclusions TEXT,
    match_possible_interview BOOLEAN,
    FOREIGN KEY (job_portal_id) REFERENCES jobs(job_portal_id)
);
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY,
    job_portal_id INTEGER,
    job_link TEXT,
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

CREATE VIEW IF NOT EXISTS job_matches AS
SELECT
    jobs.job_portal_id,
    jobs.job_link,
    jobs.job_title,
    jobs.job_description,
    jobs.job_posting_date,
    jobs.job_type,
    jobs.job_field,
    jobs.job_city,
    matches.match_score,
    matches.match_strengths,
    matches.match_weaknesses,
    matches.match_improvement_points,
    matches.match_conclusions,
    matches.match_possible_interview
FROM matches
LEFT JOIN jobs ON jobs.job_portal_id = matches.job_portal_id;
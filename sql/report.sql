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
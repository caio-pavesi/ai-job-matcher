INSERT INTO matches (
    job_portal_id,
    match_date,
    match_score,
    match_strengths,
    match_weaknesses,
    match_opportunities,
    match_threats,
    match_improvement_points,
    match_conclusions,
    match_possible_interview
) VALUES (
    :job_portal_id,
    :match_date,
    :match_score,
    :match_strengths,
    :match_weaknesses,
    :match_opportunities,
    :match_threats,
    :match_improvement_points,
    :match_conclusions,
    :match_possible_interview
);

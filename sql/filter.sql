SELECT * FROM jobs WHERE
1 = 1
AND job_title LIKE '%international%intern%'
OR job_title LIKE '%trainee%'
AND job_portal_id NOT IN (SELECT job_portal_id FROM matches);
SELECT job_portal_id, job_description FROM jobs
WHERE job_portal_id NOT IN
(SELECT job_portal_id FROM matches);
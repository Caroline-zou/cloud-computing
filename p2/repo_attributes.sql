SELECT repo_last_events.repository_url AS repository_url,
    repo_languages_watchers.repository_language AS repository_language,
    repo_languages_watchers.repository_watchers AS repository_watchers
FROM

-- Get language and number of stars as of the last event per repository
(SELECT repository_url, MAX(created_at) AS created_at
  FROM `publicdata.samples.github_timeline`
  GROUP BY repository_url) AS repo_last_events

JOIN

(SELECT repository_url, repository_language, repository_watchers, created_at
  FROM `publicdata.samples.github_timeline`
  WHERE repository_watchers >= 500) AS repo_languages_watchers
ON repo_last_events.repository_url = repo_languages_watchers.repository_url
  AND repo_last_events.created_at = repo_languages_watchers.created_at

GROUP BY repository_url, repository_language, repository_watchers;

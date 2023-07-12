SELECT t1.repository AS repository1, t2.repository AS repository2,
    SUM(SQRT(t1.weight * t2.weight)) AS weight
FROM

  (SELECT user, repo_info.repository_url AS repository, SUM(weight) as weight
FROM
  -- Get repositories with over 500 stars as of the end of 2012
  (SELECT repo_last_events.repository_url AS repository_url
    FROM
    (SELECT repository_url, MAX(created_at) AS created_at
      FROM `publicdata.samples.github_timeline`
      GROUP BY repository_url) AS repo_last_events
    JOIN 
    (SELECT repository_url, repository_watchers, created_at
      FROM `publicdata.samples.github_timeline`) AS repo_watchers
    ON repo_last_events.repository_url = repo_watchers.repository_url
      AND repo_last_events.created_at = repo_watchers.created_at
    WHERE repository_watchers >= 500
  ) AS repo_info
  JOIN 
  (SELECT push_events.user AS user, push_events.repository_url, push_events.weight
    FROM
    -- Pushes
    (SELECT actor AS user, repository_url, COUNT(repository_url) AS weight
      FROM `publicdata.samples.github_timeline`
      WHERE type='PushEvent' 
      GROUP BY user, repository_url) AS push_events
    UNION ALL
    -- Merged pull requests
    (SELECT pr_events.payload_pull_request_user_login AS user, pr_events.repository_url,
          COUNT(pr_events.repository_url) AS weight
      FROM `publicdata.samples.github_timeline` AS pr_events
      WHERE pr_events.type='PullRequestEvent'
        AND pr_events.payload_action='closed'
        AND pr_events.payload_pull_request_merged='true'
      GROUP BY user, repository_url)
  ) AS events
  ON repo_info.repository_url = events.repository_url
GROUP BY user, repository) AS t1

JOIN

(SELECT user, repo_info.repository_url AS repository, SUM(weight) as weight
FROM
  -- Get repositories with over 500 stars as of the end of 2012
  (SELECT repo_last_events.repository_url AS repository_url
    FROM
    (SELECT repository_url, MAX(created_at) AS created_at
      FROM `publicdata.samples.github_timeline`
      GROUP BY repository_url) AS repo_last_events
    JOIN 
    (SELECT repository_url, repository_watchers, created_at
      FROM `publicdata.samples.github_timeline`) AS repo_watchers
    ON repo_last_events.repository_url = repo_watchers.repository_url
      AND repo_last_events.created_at = repo_watchers.created_at
    WHERE repository_watchers >= 500
  ) AS repo_info
  JOIN 
  (SELECT push_events.user AS user, push_events.repository_url, push_events.weight
    FROM
    -- Pushes
    (SELECT actor AS user, repository_url, COUNT(repository_url) AS weight
      FROM `publicdata.samples.github_timeline`
      WHERE type='PushEvent' 
      GROUP BY user, repository_url) AS push_events
    UNION ALL
    -- Merged pull requests
    (SELECT pr_events.payload_pull_request_user_login AS user, pr_events.repository_url,
          COUNT(pr_events.repository_url) AS weight
      FROM `publicdata.samples.github_timeline` AS pr_events
      WHERE pr_events.type='PullRequestEvent'
        AND pr_events.payload_action='closed'
        AND pr_events.payload_pull_request_merged='true'
      GROUP BY user, repository_url)
  ) AS events
  ON repo_info.repository_url = events.repository_url
GROUP BY user, repository) AS t2
ON t1.user = t2.user

WHERE t1.repository < t2.repository
GROUP  BY repository1, repository2;


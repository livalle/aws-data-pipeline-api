SELECT
    userid,
    COUNT(*) AS total_posts
FROM posts
GROUP BY userid
ORDER BY total_posts DESC;

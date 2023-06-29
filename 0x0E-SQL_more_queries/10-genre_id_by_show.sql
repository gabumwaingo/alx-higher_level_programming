-- listing all tv shows and genres from a database
SELECT s.title, g.id
FROM shows
	INNER JOIN genre AS g
	ON s.genres.id = g.id
ORDER BY s.title

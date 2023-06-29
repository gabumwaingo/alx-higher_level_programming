-- listing all tv shows and genres from a database
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` as s
	INNER JOIN `tv_show_genres` AS g
	ON s.id = g.`show.id`
ORDER BY s.`title`, g.`genre.id`

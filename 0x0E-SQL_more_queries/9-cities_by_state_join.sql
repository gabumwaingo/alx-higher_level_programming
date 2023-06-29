-- Listing all the cities in the database
SELECT cities.id, cities.name, s.name
FROM cities
INNER JOIN states as s
ON cities.state_id = s.id
ORDER BY cities.id;

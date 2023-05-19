-- displays temperatures in Farenheit of by city ordered in descending order.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;

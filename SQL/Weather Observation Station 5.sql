SELECT CITY, LENGTH(CITY) AS NameLength FROM STATION 
ORDER BY NameLength ASC, CITY LIMIT 1
;
SELECT CITY, LENGTH(CITY) AS NameLength FROM STATION 
ORDER BY NameLength DESC, CITY ASC LIMIT 1
;
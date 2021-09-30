'
Join self table with date(original) - date(join table) = 1
Then select Temperature
'

SELECT Weather.Id 
FROM   Weather 
       JOIN Weather AS w 
         ON w.RecordDate = SUBDATE(Weather.RecordDate, 1) 
WHERE  Weather.Temperature > w.Temperature 
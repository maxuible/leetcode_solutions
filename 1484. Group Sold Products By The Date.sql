WITH UniqueActivities AS (
    SELECT DISTINCT sell_date, product 
    FROM Activities
)
SELECT 
    sell_date,
    COUNT(product) as num_sold,
    STRING_AGG(product, ',') AS products
FROM UniqueActivities
GROUP BY sell_date;
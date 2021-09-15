# Write your MySQL query statement below
with qual as (select query_name, round(avg(rating/position), 2) as quality from Queries
                group by query_name),

poor_query as (select query_name, round(count(if(rating < 3, 1, null))*100 / count(rating), 2) as poor_query_percentage from Queries
              group by query_name)
     
     
select qual.query_name as query_name, quality, poor_query_percentage from qual
left join poor_query
on qual.query_name = poor_query.query_name
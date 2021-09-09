# Thought process
'
Very Straight forward thinking. The key point is union.
-> get the counts of comments of every user (simple group by) from Movie_Rating as u_r
-> get the max counts from above table from above table u_r
-> combin max counts info to u_r to get the largest id in the same time join Users table to get username
-> order by user name limit one (since both largest and lexographic order)

Almost same by doing to movie 
However the last step
get username , get movie name -> union.
(The column of to table must be the same. Using ___ as ___ to rename is also valid)
'

with u_r as (select user_id, count(user_id) as user_count from Movie_Rating
            group by user_id),
            

user_name as (select name as result1 from Users left join u_r
              on Users.user_id = u_r.user_id
              where user_count = (select max(user_count) from u_r)
              order by name limit 1),
              
              
              
m_r as (select movie_id, avg(rating) as avg_rating from Movie_Rating
            where Year(created_at) = 2020 and Month(created_at) = 2
            group by movie_id),
            
movie_name as (select title as result2 from Movies left join m_r
              on Movies.movie_id = m_r.movie_id
              where avg_rating = (select max(avg_rating) from m_r)
              order by title limit 1)
              
              
select result1 as results from user_name
union
select result2 as results from movie_name
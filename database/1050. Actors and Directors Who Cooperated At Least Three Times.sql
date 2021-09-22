# Though process
'
Get the rows where the count is equal over 3 group by actor_id and director_id with timestamp
left join then select those which is not null
'

with derived as (select timestamp, count(actor_id) as is_large from ActorDirector
group by actor_id, director_id
having count(actor_id) >= 3)


select actor_id, director_id from ActorDirector
left join derived
on ActorDirector.timestamp = derived.timestamp
where is_large is not null
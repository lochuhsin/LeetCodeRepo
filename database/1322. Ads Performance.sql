# Though process
'
The first thought is seperate the query to 3 steps,
1. using group by ad_id to get the counts for action where action = 'Viewed'
2. same but the condition is action = 'Clicked'
3. combine two results then do some calculations

However it can reduces the code by combine all operations using sum ...etc
after that the below is final result.

Actually the if statement can combine to the output table to do one select
but the if statement will be extremely long. So i decided to break into two
steps.
'


with output as (select ad_id, (sum(action='Clicked')/(sum(action='Viewed') + sum(action='Clicked')))*100 as ctr from ads
group by ad_id)

select ad_id, if(ctr is null, round(0), round(ctr,2)) as ctr from output
order by ctr DESC, ad_id ASC
# Write your MySQL query statement below
with derived as (select sales_id from orders left join company
                 on orders.com_id = company.com_id
                 where company.name = 'RED'
                 group by sales_id)
                 
                
        
select name  from salesperson left join derived
on derived.sales_id = salesperson.sales_id
where derived.sales_id is null
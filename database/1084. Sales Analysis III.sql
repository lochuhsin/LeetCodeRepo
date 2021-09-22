# Write your MySQL query statement below
'
In order to get product only sold in 2019-01-01 to 2019-03-31,
negilate the prodcut rows that only sold 2019-01-01 to 2019-03-31

get the product_id that are left. These product_id are those not
only sold between 2019-01-01 to 2019-03-31.

Therefore join these table back to Product table,
get the null one.

'

with derived as (select product_id as not_id from Sales
                where not sale_date between '2019-01-01' and '2019-03-31'
                group by product_id)
                
                
            
select product_id, product_name from Product
left join derived
on Product.product_id = derived.not_id
where not_id is null
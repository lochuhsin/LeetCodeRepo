# Thought process
'
First we get the first_year when the product sold to a table from Sales table.
Next combine the new_table back to original table Sales, then get the information
Where year equals to the first_year(we need first year information not other years.)
'

with min_year as (select product_id, min(year) as first_year from Sales
group by product_id)

select Sales.product_id as product_id, first_year, quantity, price from Sales left join min_year
on Sales.product_id = min_year.product_id
where year = first_year
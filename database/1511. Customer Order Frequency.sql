# Though process
'
First get the total spending amount (quantity*price) by join Orders and Product
after that using where to limit the possible date (month) to june and july
Now group by the customer_id and month (in order to sum the quantity and price)
THe reason that month is also in group by is because that
user could spend several times in same month. So we need to sum(quantity*price)
Finally using having to eleminate the rows that sum(quantity*price) is lower than 100

This is how the table will look like:

customer_id, mon, amount
1             6    101
1             7    120
2             6    150
3             7    115
.
.
.
.
and so on

Now we need the user spend over 100 in both june and july
-> group by customer_id , count(mon) = 2 Done!

'

with derived as (select customer_id, month(order_date) as mon, sum(quantity*price) as amount from Orders
                left join Product
                on Product.product_id = Orders.product_id
                where order_date between '2020-06-01' and '2020-07-31' 
                group by customer_id, mon
                having sum(quantity*price) >= 100)          
                
                
select Customers.customer_id, name from Customers
left join derived
on Customers.customer_id = derived.customer_id
group by customer_id, name
having count(mon) =2
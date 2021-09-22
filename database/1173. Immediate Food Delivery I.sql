# Thought process
'
using the if condition to filter the result that needs to be count,
null -> using will not be count by count().
Therefore the count with if statment counts the number of dates
that customer_pref_delivery_date is equal to order_date
'
select round(count(if(customer_pref_delivery_date = order_date, 1, null))*100 / count(order_date), 2) as immediate_percentage
from Delivery
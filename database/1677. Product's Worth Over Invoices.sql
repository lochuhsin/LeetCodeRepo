#Though process
#Remember to use ifnull(statement, null set value) to handle null
#it is important to think which table joins to which table when there
#are null values appear

select name, ifnull(sum(rest),0) as rest, ifnull(sum(paid),0) as paid, ifnull(sum(canceled),0) as canceled, ifnull(sum(refunded),0) as refunded
from Product left join Invoice
on Invoice.product_id = Product.product_id
group by Invoice.product_id, name
order by name

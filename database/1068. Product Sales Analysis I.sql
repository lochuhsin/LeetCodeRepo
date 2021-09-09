# Though process.... it is pretty easy, one simple join
select product_name, year, price from Sales left join Product
on Sales.product_id = Product.product_id
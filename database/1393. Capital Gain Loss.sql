# Though process
'
+---------------+-----------+---------------+--------+
| stock_name    | operation | operation_day | price  |
+---------------+-----------+---------------+--------+
| Leetcode      | Buy       | 1             | 1000   |
| Corona Masks  | Buy       | 2             | 10     |
| Leetcode      | Sell      | 5             | 9000   |
| Handbags      | Buy       | 17            | 30000  |
| Corona Masks  | Sell      | 3             | 1010   |
| Corona Masks  | Buy       | 4             | 1000   |
| Corona Masks  | Sell      | 5             | 500    |
| Corona Masks  | Buy       | 6             | 1000   |
| Handbags      | Sell      | 29            | 7000   |
| Corona Masks  | Sell      | 10            | 10000  |
+---------------+-----------+---------------+--------+

For any total stock, the net income(whether positive or not) for each stock is fix buy sum(sell price) - sum(buy price)
Therefore we calculate two tables.
The first table contains the total buy for each stock.
The second table contains the total sell for each stock.

Combine two of them -> sell - buy, join with id than get the result.
'

with b as (select stock_name, sum(price) as buy from Stocks
          where operation = 'Buy'
          group by stock_name),
          
s as (select stock_name, sum(price) as sell from Stocks
       where operation = 'Sell'
       group by stock_name)
       
       
select s.stock_name as stock_name, sell - buy as capital_gain_loss from b join s
on b.stock_name = s.stock_name
# Though process
'
To find consecutive seats (continous), join another table by cross product.
After that will discover that if the value is continous, the two id with diff
of 1 will both free for example:

1 1 
2 0 
3 1   
4 1 
5 0 

after cross

1 1 1 1 
1 1 2 0 
1 1 3 1
1 1 4 1 
1 1 5 0 
2 0 1 1 
2 0 2 0 
............ and so on
examin on 
3 1 1 1 
3 1 2 0 
3 1 3 1 
3 1 4 1  ----- > this the desire value and so as 4 1 3 1  
3 1 5 0

therefore there might be dupliciates when continous is large than 3
put distinct to prevent duplicates.

'

select distinct c1.seat_id from cinema as c1 join cinema as c2
on abs(c1.seat_id - c2.seat_id) = 1
where c1.free = 1 and c2.free = 1
order by c1.seat_id

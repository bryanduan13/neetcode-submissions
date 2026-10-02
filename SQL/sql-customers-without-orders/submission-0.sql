-- Write your query below
select name from customers 
Left join orders on customers.id = orders.customer_id
where orders.id is Null
-- Write your query below
select employee_id,
    Case 
        WHEN employee_id %2 =1 AND name NOT LIKE 'M%' THEN salary
        ELSE 0
    END as bonus 
from employees
ORDER by employee_id
select customerFirstName
from (		
		select c.customerFirstName
		, sum(o.orderCost) as TotalOrderCost
		from orders as o
		join customers as c on o.customerID = c.customerID
		group by 1
) a
qualify row_number() over(order by TotalOrderCost desc) in (1,2,3,4,5)
/*
Exercise 1 : Items and customers
We will work on the public database that we created yesterday.
1.    Use SQL to get the following from the database:
        All items, ordered by price (lowest to highest).
        Items with a price above 80 (80 included), ordered by price (highest to lowest).
        The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
        All last names (no other columns!), in reverse alphabetical order (Z-A)
*/
/*
select * from items ORDER BY item_price asc;
select * from items  where item_price >= 80 order by item_price desc;

CREATE TEMPORARY TABLE TempCustomers AS SELECT * FROM Customers;
ALTER TABLE TempCustomers DROP COLUMN customer_id;
select * from TempCustomers order by first_name asc limit 3;
select last_name from customers order by last_name desc;
*/
/*
2. Create a table named purchases. It should have 3 columns :

    id : the primary key of the table
    customer_id : this column references the table customers
    item_id : this column references the table items
    quantity_purchased : this column is the quantity of items purchased by a certain customer

Insert purchases for the customers, use subqueries:

    Scott Scott bought one fan
    Melanie Johnson bought ten large desks
    Greg Jones bougth two small desks
*/
/*
CREATE TABLE purchases(
	id SERIAL,
	customer_id INT,
	item_id INT,
	PRIMARY KEY (id),
	FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
	FOREIGN KEY (item_id) REFERENCES items (item_id)
);

insert into purchases(customer_id) values((select customer_id from customers limit 1));
insert into purchases(customer_id, item_id) values (1,5), (2,4), (3,4),(4,5),(5,6);
*/
/*
Part II
    Use SQL to get the following from the database:
        All purchases. Is this information useful to us?
        All purchases, joining with the customers table.
        Purchases of the customer with the ID equal to 5.
        Purchases for a large desk AND a small desk
*/
/*
select * from purchases;
select * from purchases inner join customers on purchases.customer_id = customers.customer_id;
select * from purchases inner join customers on purchases.customer_id = customers.customer_id where customers.customer_id = 4;
select * from purchases inner join items on purchases.item_id = items.item_id where items.office_items = 'Small desk' and items.office_items = 'Large desk';
*/
/*
2. Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
    Customer first name
    Customer last name
    Item name
*/
select customers.first_name, customers.last_name, items.office_items from purchases inner join items on items.item_id = purchases.item_id inner join customers on purchases.customer_id = customers.customer_id;

select * from actors;

update actors
set age = NULL
where first_name = 'Matt' and number_oscars = 0

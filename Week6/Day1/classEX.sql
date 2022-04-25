INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Angelina','Jolie','06/04/1975', 1);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Marilyn','Monroe','06/01/1962', 0);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES
('Brad','Pitt','12/18/1963', 5),
('Leonardo','DiCaprio','11/11/1974', 1),
('Tom','Cruise','07/03/1962', 0);

delete from actors where actor_id >= 8;


/* Use the table actors to retrieve :
    The first 4 actors
    The first 4 actors ordered in descending order of the last_name (ie. sorted DESCENDING by the "last_name" column))
    The actors that have the letter 'e' in their first_name
    The actors that got at least 5 oscars
*/


select * from actors limit 4;

select * from actors ORDER BY last_name DESC limit 4;

select * from actors where first_name ILIKE '%e%';

select * from actors where number_oscars >= 5;

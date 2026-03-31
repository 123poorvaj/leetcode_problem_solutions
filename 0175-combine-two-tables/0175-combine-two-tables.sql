/* Write your T-SQL query statement below */
select firstName,lastName,city,state from person left join Address on person.personId=address.personId;
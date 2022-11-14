#1
INSERT INTO persons(id, name, pwd, email, gender) values ('1', 'Vasya', '21341234qwfsdf', 'mmm@mmail.com', 'm'), ('2', 'Alex',
'21341234','mmm@gmail.com','m'),('3', 'Alexey','qq21341234Q','alexey@gmail.com','m'), ('4', 'Helen','MarryMeeee','hell@gmail.com','f'), ('5', 'Jenny','SmakeMyb','eachup@gmail.com','f'), ('6', 'Lora','burn23','tpicks@gmail.com','f');

#2
SELECT CONCAT ('This is ', name, ',', CASE WHEN gender LIKE 'm' THEN ' he' WHEN gender LIKE 'f' THEN ' she' END, ' has email', email)AS "info" FROM persons;

#3
SELECT CONCAT('We have ', COUNT(*), CASE WHEN gender LIKE 'm' THEN ' boys!' WHEN gender LIKE 'f' THEN ' girls!' END)AS "Gender information:" FROM persons GROUP BY gender;

#4
SELECT name, COUNT(*) AS "words" FROM vocabulary FULL JOIN word on(vocabulary.id=vocabulary_id)GROUP BY name;
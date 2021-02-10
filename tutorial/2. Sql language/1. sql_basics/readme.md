## SQL Syntax
SQL is followed by unique set of rules and guidelines called Syntax. This tutorial gives you a quick start with SQL by listing all the basic SQL Syntax:
All the SQL statements start with any of the keywords like **SELECT, INSERT, UPDATE, DELETE, ALTER, DROP, CREATE, USE, SHOW and all the statements end with a semicolon (;).**

Important point to be noted is that SQL is case insensitive, which means SELECT and select have same meaning in SQL statements, but MySQL makes difference in table names. So if you are working with MySQL, then you need to give table names as they exist in the database.

**1.SQL SELECT Statement:**

    SELECT column1, column2....columnN FROM table_name;
    SQL DISTINCT Clause:
    SELECT DISTINCT column1, column2....columnN FROM table_name;

**2. SQL WHERE Clause:**

    SELECT column1, column2....columnN FROM table_name
    WHERE CONDITION;

 **3. SQL AND/OR Clause:**
 
    SELECT column1, column2....columnN FROM table_name
    WHERE CONDITION-1 {AND|OR} CONDITION-2;

 **4. SQL IN Clause:**
 
    SELECT column1, column2....columnN
    FROM
    table_name
    WHERE column_name IN (val-1, val-2,...val-N);

**5. SQL BETWEEN Clause:**

    SELECT column1, column2....columnN
    FROM
    table_name
    WHERE column_name BETWEEN val-1 AND val-2;

**6.SQL LIKE Clause:**

    SELECT column1, column2....columnN FROM table_name
    WHERE column_name LIKE { PATTERN };

**7.SQL ORDER BY Clause:**

    SELECT column1, column2....columnN
    FROM
    table_name
    WHERE CONDITION
    ORDER BY column_name {ASC|DESC};

**8.SQL GROUP BY Clause:**

    SELECT SUM(column_name)
    FROM
    table_name
    WHERE CONDITION
    GROUP BY column_name;

#### 9.SQL COUNT Clause:

    SELECT COUNT(column_name)
    FROM
    table_name
    WHERE CONDITION;

#### 10.SQL HAVING Clause:

    SELECT SUM(column_name)
    FROM
    table_name
    WHERE CONDITION
    GROUP BY column_name
    HAVING (arithematic function condition);

#### 11. SQL CREATE TABLE Statement:

    CREATE TABLE table_name(
    column2
    .....
    columnN
    PRIMARY KEY( one or more columns ));

#### 11.SQL DROP TABLE Statement:

    DROP TABLE table_name;

#### 12. SQL CREATE INDEX Statement:

    CREATE UNIQUE INDEX index_name
    ON table_name ( column1, column2,...columnN);

#### 13. SQL DROP INDEX Statement:

    ALTER TABLE table_name
    DROP INDEX index_name;

#### 14. SQL DESC Statement:

    DESC table_name;

#### 15. SQL TRUNCATE TABLE Statement:
   
    TRUNCATE TABLE table_name;

#### 16.SQL ALTER TABLE Statement:

    ALTER TABLE table_name {ADD|DROP|MODIFY} column_name {data_ype};

#### 17.SQL ALTER TABLE Statement (Rename):

    ALTER TABLE table_name RENAME TO new_table_name;

#### 18.SQL INSERT INTO Statement:

    INSERT INTO table_name( column1, column2....columnN)
    VALUES ( value1, value2....valueN);

#### 19.SQL UPDATE Statement:

    UPDATE table_name
    SET column1 = value1, column2 = value2....columnN=valueN
    [ WHERE CONDITION ];

#### 20.SQL DELETE Statement:
   
    DELETE FROM table_name
    WHERE {CONDITION};

#### 21.SQL CREATE DATABASE Statement:

    CREATE DATABASE database_name;
    SQL DROP DATABASE Statement:
    DROP DATABASE database_name;

#### 22.SQL USE Statement:
    
    USE DATABASE database_name;

#### 22.SQL COMMIT Statement:
    COMMIT;
  
#### 23.SQL ROLLBACK Statement:

    ROLLBACK;

![1](https://user-images.githubusercontent.com/58425689/107518037-a7f5a880-6bd6-11eb-964f-14c8b0ca4232.jpg)
![2](https://user-images.githubusercontent.com/58425689/107518044-a9bf6c00-6bd6-11eb-92d1-ef7037d74cae.jpg)
![3](https://user-images.githubusercontent.com/58425689/107518047-aaf09900-6bd6-11eb-84b2-5d44abb1af01.jpg)
![4](https://user-images.githubusercontent.com/58425689/107518049-ab892f80-6bd6-11eb-9d88-adaa3b36c18a.jpg)
![5](https://user-images.githubusercontent.com/58425689/107518052-ac21c600-6bd6-11eb-9418-d5218a0d897f.jpg)
![6](https://user-images.githubusercontent.com/58425689/107518055-acba5c80-6bd6-11eb-9a10-82a0588d6a20.jpg)
![7](https://user-images.githubusercontent.com/58425689/107518056-ad52f300-6bd6-11eb-8052-6df3091c9ed8.jpg)
![8](https://user-images.githubusercontent.com/58425689/107518057-adeb8980-6bd6-11eb-9d7c-ae156c6d17e9.jpg)

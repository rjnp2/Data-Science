# SQL Overview

SQL is **Structured Query Language**, which is a computer language for storing, manipulating and retrieving data stored in relational database.
SQL is the standard language for Relation Database System. All relational database management systems like MySQL, MS Access, Oracle, Sybase, Informix, postgres and SQL Server use SQL as standard database language.

## Why SQL?
    • Allows users to access data in relational database management systems.
    • Allows users to describe the data.
    • Allows users to define the data in database and manipulate that data.
    • Allows to embed within other languages using SQL modules, libraries & pre-compilers.
    • Allows users to create and drop databases and tables.
    • Allows users to create view, stored procedure, functions in a database.
    • Allows users to set permissions on tables, procedures and views.
    
## SQL Process:
When you are executing an SQL command for any RDBMS, the system determines the best way to carry out your request and SQL engine figures out how to interpret the task. There are various components included in the process. These components are Query Dispatcher, Optimization Engines, Classic Query Engine and SQL Query Engine, etc. Classic query engine handles all non-SQL queries, but SQL query engine won't handle logical files.

#### Following is a simple diagram showing SQL Architecture: 
  ![pro 8](https://user-images.githubusercontent.com/58425689/105805616-78398480-5fca-11eb-8c27-ae998b935d28.png)

## SQL RDBMS Concepts

RDBMS stands for Relational Database Management System. RDBMS is the basis for SQL and for all modern database systems like MS SQL Server, IBM DB2, Oracle, MySQL, and Microsoft Access.
A Relational database management system (RDBMS) is a database management system (DBMS) that is based on the relational model. 

#### Table
The data in RDBMS is stored in database objects called tables. The table is a collection of related data entries and it consists of columns and rows.

![5](https://user-images.githubusercontent.com/58425689/105806355-efbbe380-5fcb-11eb-8736-3bf1ca73ee29.png)

#### Field
Every table is broken up into smaller entities called fields. The fields in the CUSTOMERS table consist of ID, NAME, AGE, ADDRESS and SALARY.
A field is a column in a table that is designed to maintain specific information about every record in the table.

#### Record or Row
A record, also called a row of data, is each individual entry that exists in a table. For example, there are 7 records in the above CUSTOMERS table. Following is a single row of data or record in the CUSTOMERS table:
        1 Ramesh 32 Ahmedabad 2000.00 
A record is a horizontal entity in a table.

#### Column
A column is a vertical entity in a table that contains all information associated with a specific field in a table.

## SQL Data Types
SQL data type is an attribute that specifies type of data of any object. Each column, variable and expression has related data type in SQL.
You would use these data types while creating your tables. You would choose a particular data type for a table column based on your requirement.
SQL Server offers six categories of data types for your use:

#### 1.Exact Numeric Data Types: Int

#### 2.Approximate Numeric Data Types:
    • Float -1.79E + 308 1.79E + 308
    • Real -3.40E + 38 3.40E + 38
      
#### 3.char Types:
    • Char Maximum length of 8,000 characters.( Fixed length non-Unicode
          characters)
    • Varchar Maximum of 8,000 characters.(Variable-length non-Unicode data).
    • varchar(max) Maximum length of 231characters, Variable-length non-Unicode data(SQL Server 2005 only).
    • text Variable-length non-Unicode data with a maximum length of
    • 2,147,483,647 characters
    
## SQL Commands/Syntax:
The standard SQL commands to interact with relational databases are CREATE, SELECT, INSERT, UPDATE, DELETE and DROP. These commands can be classified into groups based on their nature:

1. DDL - Data Definition Language: \
      ​ ![1](https://user-images.githubusercontent.com/58425689/105805921-175e7c00-5fcb-11eb-9e48-5368268619dc.png)
  
2.DML - Data Manipulation Language:

  ![2](https://user-images.githubusercontent.com/58425689/105805925-17f71280-5fcb-11eb-8c0c-089800c538b3.png)

3. DCL - Data Control Language:

  ![3](https://user-images.githubusercontent.com/58425689/105805928-188fa900-5fcb-11eb-9188-db6339b022a7.png)

4. DQL - Data Query Language:

  ![4](https://user-images.githubusercontent.com/58425689/105805930-19283f80-5fcb-11eb-832e-3f43a23beb76.png)

## SQL Constraints:
Constraints are the rules enforced on data columns on table. These are used to limit the type of data that can go into a table. This ensures the accuracy and reliability of the data in the database.
Constraints could be column level or table level. Column level constraints are applied only to one column, whereas table level constraints are applied to the whole table.

Following are commonly used constraints available in SQL:

    • NOT NULL Constraint: Ensures that a column cannot have NULL value.
    • DEFAULT Constraint: Provides a default value for a column when none is specified.
    • UNIQUE Constraint: Ensures that all values in a column are different.
    • PRIMARY Key: Uniquely identified each rows/records in a database table.
    • FOREIGN Key: Uniquely identified a rows/records in any another database table.
    • CHECK Constraint: The CHECK constraint ensures that all values in a column satisfy certain conditions.
    • INDEX: Use to create and retrieve data from the database very quickly.

## Data Integrity:
The following categories of the data integrity exist with each RDBMS:

    • Entity Integrity : There are no duplicate rows in a table.
    • Domain Integrity : Enforces valid entries for a given column by restricting the type,
      the format, or the range of values.
    • Referential Integrity : Rows cannot be deleted which are used by other records.
    • User-Defined Integrity : Enforces some specific business rules that do not fall 
      into entity, domain, or referential integrity.

## Database Normalization
Database normalization is the process of efficiently organizing data in a database.
There are two reasons of the normalization process:

    • Eliminating redundant data, for example, storing the same data in more than one table.
    • Ensuring data dependencies make sense.
    
Both of these are worthy goals as they reduce the amount of space a database consumes and ensure that data is logically stored. Normalization consists of a series of guidelines that help guide you in creating a good database structure.

Normalization guidelines are divided into normal forms; think of form as the format or the way a database structure is laid out. The aim of normal forms is to organize the database structure so that it complies with the rules of first normal form, then second normal form, and finally third normal form.

## SQL Operators
An operator is a reserved word or a character used primarily in an SQL statement's WHERE clause to perform operation(s), such as comparisons and arithmetic operations.
Operators are used to specify conditions in an SQL statement and to serve as conjunctions for multiple conditions in a statement.

    • Arithmetic operators: + - * /
    • Comparison operators: = !=  <>  >=
    • Logical operators: all and any between in is
    • Operators used to negate conditions:
    
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
 

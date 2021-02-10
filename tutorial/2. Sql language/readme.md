# SQL Overview
___

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
___    

## SQL Process:
When you are executing an SQL command for any RDBMS, the system determines the best way to carry out your request and SQL engine figures out how to interpret the task. There are various components included in the process. These components are Query Dispatcher, Optimization Engines, Classic Query Engine and SQL Query Engine, etc. Classic query engine handles all non-SQL queries, but SQL query engine won't handle logical files.

#### Following is a simple diagram showing SQL Architecture: 
  ![pro 8](https://user-images.githubusercontent.com/58425689/105805616-78398480-5fca-11eb-8c27-ae998b935d28.png)
___
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
___
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
___
## [SQL Commands/Syntax:](https://github.com/rjnp2/Data-Science/blob/main/tutorial/2.%20Sql%20language/1.%20sql_basics/readme.md)
The standard SQL commands to interact with relational databases are CREATE, SELECT, INSERT, UPDATE, DELETE and DROP. These commands can be classified into groups based on their nature:

 1. DDL - Data Definition Language: \
    ![1](https://user-images.githubusercontent.com/58425689/105805921-175e7c00-5fcb-11eb-9e48-5368268619dc.png)

 2. DML - Data Manipulation Language: \
  ![2](https://user-images.githubusercontent.com/58425689/105805925-17f71280-5fcb-11eb-8c0c-089800c538b3.png)

 3. DCL - Data Control Language: \
  ![3](https://user-images.githubusercontent.com/58425689/105805928-188fa900-5fcb-11eb-9188-db6339b022a7.png)

 4. DQL - Data Query Language: \
  ![4](https://user-images.githubusercontent.com/58425689/105805930-19283f80-5fcb-11eb-832e-3f43a23beb76.png)
___
## [SQL Constraints:](https://github.com/rjnp2/Data-Science/edit/main/tutorial/2.%20Sql%20language/SQL_Constraints/readme.md)
Constraints are the rules enforced on data columns on table. These are used to limit the type of data that can go into a table. This ensures the accuracy and reliability of the data in the database.
Constraints could be column level or table level. Column level constraints are applied only to one column, whereas table level constraints are applied to the whole table.
___
## Data Integrity:
The following categories of the data integrity exist with each RDBMS:

    • Entity Integrity : There are no duplicate rows in a table.
    • Domain Integrity : Enforces valid entries for a given column by restricting the type,
      the format, or the range of values.
    • Referential Integrity : Rows cannot be deleted which are used by other records.
    • User-Defined Integrity : Enforces some specific business rules that do not fall 
      into entity, domain, or referential integrity.
___
## Database Normalization
Database normalization is the process of efficiently organizing data in a database.
There are two reasons of the normalization process:

    • Eliminating redundant data, for example, storing the same data in more than one table.
    • Ensuring data dependencies make sense.
    
Both of these are worthy goals as they reduce the amount of space a database consumes and ensure that data is logically stored. Normalization consists of a series of guidelines that help guide you in creating a good database structure.

Normalization guidelines are divided into normal forms; think of form as the format or the way a database structure is laid out. The aim of normal forms is to organize the database structure so that it complies with the rules of first normal form, then second normal form, and finally third normal form.
___
## SQL Operators
An operator is a reserved word or a character used primarily in an SQL statement's WHERE clause to perform operation(s), such as comparisons and arithmetic operations.
Operators are used to specify conditions in an SQL statement and to serve as conjunctions for multiple conditions in a statement.

    • Arithmetic operators: + - * /
    • Comparison operators: = !=  <>  >=
    • Logical operators: all and any between in is
    • Operators used to negate conditions:
___


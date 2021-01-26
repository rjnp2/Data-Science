## Introduction to Python SQL Libraries
All software applications interact with data, most commonly through a database management system (DBMS). Some programming languages come with modules that you can use to interact with a DBMS, while others require the use of third-party packages. In this, explore the different Python SQL libraries that you can use. You’ll develop a straightforward application to interact with SQLite, MySQL, and PostgreSQL databases.

In this, we will learn how to:

    • Connect to different database management systems with Python SQL libraries
    • Interact with SQLite, MySQL, and PostgreSQL databases
    • Perform common database queries using a Python application
    • Develop applications across different databases using a Python script

### Using Python SQL Libraries to Connect to a Database 

Before interact with any database through a Python SQL Library, have to connect to that database. In this, how to connect to SQLite, MySQL, and PostgreSQL databases from within a Python application.

## SQLite
SQLite is probably the most straightforward database to connect with a Python since you don’t need to install any external Python SQL modules to do so. By default, Python contains a Python SQL library named sqlite3 that i can use to interact with an SQLite database.
What’s more, SQLite databases are serverless and self-contained, since they read and write data to a file. This means that, unlike with MySQL and PostgreSQL, you don’t even need to install and run an SQLite server to perform database operations!

Here’s how you use sqlite3 to connect to an SQLite database in Python:

```python
import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection 
```

Here’s how this code works:
***-import sqlite3 and the module’s Error class.
- uses .connect() from sqlite3 module and takes the SQLite database path as a parameter. If the database exists at the specified location, then a connection to the database is established. Otherwise, a new database is created at the specified location, and a connection is established***
***- catches any exception that might be thrown if .connect() fails to establish a connection.***

connection object- This connection object can be used to execute queries on an SQLite database. 

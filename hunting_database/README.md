I created a hunting trip database program to improve my understanding of Python, SQL, and relational database programming.

The software allows a user to add, view, update, and delete hunting trip records. It uses Python to connect to a SQLite relational database. The program is used through a menu in the terminal. When the user selects an option, the program runs the appropriate SQL command and saves the changes in the database.

My purpose for writing this software was to learn how to connect a Python program to a SQL relational database and use SQL commands to manage stored data.

Demo Video: https://youtu.be/gMarJ-iph8Q

Relational Database

I am using SQLite for the relational database. SQLite stores the database in a file and works directly with Python through the built-in sqlite3 library.

The database contains a table named hunting_trips. The table stores information about each hunting trip, including a unique trip ID, location, animal, trip date, and result.

Development Environment

I used Visual Studio Code to write and test the software.

I used Python as the programming language. I also used the built-in sqlite3 library to connect to the SQLite database and execute SQL commands.

Useful Websites
Python sqlite3 Documentation
SQLite Documentation
W3Schools SQL Tutorial
Future Work
Add a search feature for finding specific hunting trips.
Add another related table using a foreign key.
Improve input validation and error handling.
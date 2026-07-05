# Overview

I wrote this software to practice building a Python program that connects to a cloud database. The program stores used truck records in Google Firebase Firestore. It lets the user create and modify truck records.

The program runs in the terminal. When the program starts, it shows a menu with different options. The user can seed sample truck data, add a new truck, view all trucks, search by make, search by price, update a truck, or delete a truck. The data is not stored on my computer. It is stored in the cloud using Firestore.

My purpose for writing this software was to better understand how Python can work with cloud data. I wanted to learn how to connect Python to Firebase and use cloud database commands instead of only using local files or a local database.

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

The cloud database I used is Google Firebase Firestore. Firestore is a NoSQL cloud database. Instead of using normal SQL tables, it stores data in collections and documents.

The database has one collection called `trucks`. Each document in the collection is one truck record.

Each truck record stores this information:

- make
- make_lower
- model
- year
- mileage
- price
- engine
- drivetrain
- title_status
- notes
- created_at
- updated_at

The `make_lower` field is used to make searching by truck make easier. For example, Ford, ford, and FORD can all be searched the same way.

# Development Environment

I used Visual Studio Code to write and run the program. I also used the Firebase Console to create the Firestore database and view the cloud data.

The program was written in Python. I used the `firebase-admin` library to connect Python to Firebase Firestore. I also used a Firebase service account JSON file to give the program permission to access my Firestore database.

# Useful Websites

[Firebase Console](https://console.firebase.google.com/)
[Cloud Firestore Documentation](https://firebase.google.com/docs/firestore)
[Firebase Admin SDK for Python](https://firebase.google.com/docs/admin/setup)
[Python Documentation](https://docs.python.org/3/)

# Future Work

Add more truck fields, such as condition, location, trim, and seller type.
Add better input checks so the user cannot enter bad data.
Add a simple user interface instead of only using the terminal.
Add real truck market data from used car websites.
Add a future price estimate tool that can compare trucks by year, mileage, engine, and title status.
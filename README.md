## CLI Address Book
Is a Python command-line interface that allows users to manage contacts and their associated addresses using an object-oriented approach and a SQLite database with custom ORM methods. 

Requirements:
python 3.8.10

git clone github url
cd cli Address Book
pipenv install && pipenv shell

🚀 How to Use

Run the main script to start the CLI:

python main.py

Follow the interactive prompts to:

Add, view, delete contacts

Add, view, delete addresses for a contact

Search for a contact by name or ID

Display all contacts and their addresses

Exit the program

📁 File Overview

#main.py

This is the main entry point of the application. It presents the user with a text-based menu and handles all user interactions, routing commands to the appropriate model methods.

It provides features such as:

Displaying contacts and addresses

Adding/deleting contacts

Viewing addresses for a specific contact

Validating user input

Graceful error messages for bad input or missing data

##Key Features
-Attributes: id, name, email, phone

-Relationships: One Contact has many Addresses

ORM methods:

-create(): Create a new contact in the database

-delete(): Delete a contact (and optionally cascade delete their addresses)

-find_by_id(), find_by_name()

-all(): Returns a list of all contacts

-addresses(): Returns all addresses for a specific contact

💡 Features

.Persistent storage via SQLite

.Object-Oriented Programming

.Custom ORM methods for interacting with the database

.CLI menu with loops, input validation, and error handling

.Simple and readable codebase






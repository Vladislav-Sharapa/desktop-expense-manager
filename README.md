# Desktop task manager 

This simple desktop application, built using Python and Qt, offers to record and manage expenses. Users can perform basic operations such as deletion, modification, and creation of expenses, as well as group expenses into categories. The application displays all expense-related information in a table format on the main form.

## Technology Stack

* **Python**: core programming language used for developing the application.
* **Qt**: graphical user interface toolkit utilized for creating the application's interface.
* **SQLAlchemy**: SQL toolkit and ORM library for Python used for database operations.

## Features
* Expense recording: input and save expense details including amount, category, and date.
* Expense categorization: categorize expenses for better organization and tracking.
* User-friendly interface: view and manage expense records in a clear and intuitive tabular layout.

## Installing

1. Clone git repository:
```
$ git clone https://github.com/Vladislav-Sharapa/desktop-expense-manager
```
2. Create virtual enviroment using following command:

```
$ python -m venv venv
```
3. Install Python packages specified in the 'requirements.txt':
```
$ pip install -r requirements.txt
```
> :heavy_exclamation_mark: Before running this command, make sure your virtual environment has been activated

## Getting started

To start application run the script "main.py":
```
$ python src/main.py
```
## How to use

Upon launching the application, you will be presented with a table displaying all recorded expenses. Here are some key actions you can perform within the application:

* **Add an expense**: click on the "New Expense" button to enter new expense details.
* **Edit an expense**: select expense in table and click on button "Edit expense" to modify the recorded information.
* **Delete an expense**: select an expense and click the "Delete expense" button to remove it from the record.
* **Add category**: click on button "Add category" to create new category on databese
* **Delete category**: click on button "Delete category" and select existing category to delete it"
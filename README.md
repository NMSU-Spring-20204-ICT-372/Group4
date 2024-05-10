# Agile Aggies Repository

This repository is for use by the Agile Aggies group for ICT-377 
during the Spring 2024 semester at New Mexico State University. 

The project contained in this repository is an internal blogging tool created 
for a fictional company called A Mountain Ale who is needing a way for managers 
to post updates for employees. 

## Prerequisites
- python3
- pip
- virtualenv

## Setting Up Your Virtual Environment
If you are on Windows open Powershell and if you are on Mac or Linux 
open your terminal and navigate to the directory where you downloaded the
Agile Aggies Repository and create a virtual environment called `venv`. 

```
python -m venv venv
```

Activate your virtual environment so you have a clean environment to install 
the required python modules in. 

On windows you will use: 

```
venv\Scripts\Activate.ps1
```

On Mac or Linux you will use:

```
source venv/bin/activate
```

## Installing Required Python Modules
Now that you have your virtual environement activated you will need to install
the python modules required by the A Mountain Ale Blogging Tool. 

To install the requirements run:

```
pip install -r requirements.txt
```

## Starting the Application
Now that all the setup has been completed you can launch the application using 

```
python manage.py runserver
```

## Accessing the Admin Panel 
In your browsers navigate to `http://127.0.0.1:8000/admin` and you can log in
with the user you just created.

There is one superuser and two test manager account already created. 

|     Username |    Password |
| ------------ | ----------- |
| superuser1   | testpass123 |
| testmanager1 | passpass321 |
| testmanager2 | passpass123 |

## Accessing the Home Page
In your web browser navigate to `http://127.0.0.1:8000`

---

> WARNING: The below steps will revert the application back to an empty database.

## Clearing Test Data
If you want to start from scratch and do your own thing you can delete 
db.sqlite3 and then follow the steps below to start over. 

## Preparing The Database
To prepare the database for the blogging application 
from the `a_mountain_ale` directory run the following:

```
python manage.py migrate
```

Unless you've configured the application to run using an external database
you will see db.sqlite3 show up in your directory. This is your local database.

## Creating Your Super User
to create a superuser for initial login and the ability to create other users 
from the `a_mountain_ale` directory run the following:

```
python manage.py createsuperuser
```

There will be prompts for username, email, password, etc. Just fill out the 
prompts.


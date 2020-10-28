# S_Club : An Article website for students

## About the Project 

This is a fullstack project in which as user is able to post and read articles posted by other students. The backend is done using django and frontend is done using HTML,CSS and Bootstrap.

#### Highlights :
- Users can make their profiles with profile picture and username of their choice.
- Users can also reset their email or/and password in case they forget it.
- Users can view articles sorted from latest article to oldest.
- Users can also see all the artciles that a specific user has posted/written.
- Users get the option to CRUD their articles.

## Installation

### Prerequisites

#### Install Python
Install ```python-3.7.2``` and ```python-pip```. Follow the steps from the below reference document based on your Operating System.
Reference: [https://docs.python-guide.org/starting/installation/](https://docs.python-guide.org/starting/installation/)

#### Install MySQL
Install ```mysql-8.0.15```. Follow the steps form the below reference document based on your Operating System.
Reference: [https://dev.mysql.com/doc/refman/5.5/en/](https://dev.mysql.com/doc/refman/5.5/en/)
#### Setup virtual environment
```bash
# Install virtual environment
sudo pip install virtualenv

# Make a directory
mkdir envs

# Create virtual environment
virtualenv ./envs/

# Activate virtual environment
source envs/bin/activate
```
#### Install requirements
```bash
cd S_club/
pip install -r requirements.txt
```

#### Run the server
```bash
# Make migrations
python manage.py makemigrations
python manage.py migrate

# Run the server
python manage.py runserver

# your server is up
```
Try opening [http://localhost:8000](http://localhost:8000) in the browser.
Now you are good to go.

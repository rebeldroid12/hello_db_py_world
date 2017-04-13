# Python <> Postgres
---

## Requirements:

* [python](https://www.python.org/)
* [pycharm](https://www.jetbrains.com/pycharm/download/)
* [postgres](https://www.postgresql.org/)

## Installation:

* clone the repo:

```git clone https://github.com/rebeldroid12/hello_db_py_world```

* get [pip](https://pip.pypa.io/en/stable/installing/)

* test pip:

```
pip install doge

doge
```

### Create [virtual env](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

```
pip install virtualenv

virtualenv -p /usr/bin/python2.7 db_py

source db_py/bin/activate


For when we are done:
deactivate

```

### Run requirements
* pip install requirements:

```pip install -r requirements.txt```


#### trouble with [psycopg2](http://initd.org/psycopg/docs/install.html#install-from-source)???

### Now you are ready to start...


***


# Becoming the Official Data Troll 
###  ...aka the Data Guardian 
###  ...aka the One who says "You Shall Not Pass"



## Scenario:

You are the data troll who allows what data can be pushed up.
All data requests are in your hands. But first you need to become an official data troll by getting your info in the data troll table (you need to be legit in the database or else it didn't happen ;P)

## Goal:

This is a super simple example of how python can be friends with database (in this case postgres). The goal is to show how simple it is to use python to interact with postgres while having oodles of fun! woo parseltongue :D

## Outline

There will be one table that we will be pushing data to: user_scratch.data_trolls

Fields you will be updating via command line:
* name (text)
* favorite_color (text)
* title (text)
* enjoyed (boolean)


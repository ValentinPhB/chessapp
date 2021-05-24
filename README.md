# chessapp  -CENTRE ÉCHEC-

## Table of contents

1. [Technologies](#1-technologies)
2. [General information](#2-general-information)
3. [Installation Python](#3-installation-python)
4. [Setup](#4-setup)
	- [Setup for Unix](#a-setup-for-unix)
 	- [Setup for Windows](#b-setup-for-windows)
5. [Advises for users](#5-advises-for-users)
6. [Flake8 HTML reports](#6-flake8-html-reports)
	- [Unix](#a-unix)
	- [Windows](#b-windows)
7. [Author](#7-author)

## 1. Technologies

Project is created with Python 3.8.6.

- astroid==2.5.6
- flake8==3.9.2
- flake8-html==0.4.1
- importlib-metadata==4.0.1
- isort==5.8.0
- Jinja2==2.11.3
- lazy-object-proxy==1.6.0
- MarkupSafe==1.1.1
- mccabe==0.6.1
- pycodestyle==2.7.0
- pyflakes==2.3.1
- Pygments==2.9.0
- pylint==2.8.2
- tinydb==4.4.0
- toml==0.10.2
- wrapt==1.12.1
- zipp==3.4.1


## 2. General information

Chessapp is an offline application to manage chess tournaments, save/load them from database and display reports.
It supports data persistence, this application can be turn-off in a middle of tournament,
the state of this tournament will be saved and continue next time the user run this application.

Matches-making is based on Swiss-system tournament.

DataBase contains 'tournaments' and 'players' tables.

Global ranking can be reset during the tournament.


Reports :
- All players in data base (in alphabetic order).
- All players in data base (in global-ranking order).
  
- All tournaments.
	- All players for a chosen tournament (in alphabetic order). 
	- All players for a chosen tournament (in tournament-ranking order).
	- All rounds for a chosen tournament.
	- All matches for a chosen tournament.

## 3. Installation Python

Project is created with Python 3.8.6.

First download Python.exe from https://www.python.org/downloads/ for the 3.8.6 Python version __or above__ and execute
it. 
After installing Python.exe please see the appropriate guide for your operating System.

## 4. Setup
### A) *Setup for Unix*

After downloading chessapp-main.zip from Github, extract it to a location of your choice (exemple : "PATH").
Or if you use git, download it from https://github.com/ValentinPhB/chessapp.git

Create a virtual environment in "PATH" and install packages from requirements.txt.
```
$ cd ../path/to/chessapp-main
$ python3 -m venv env
$ source env/bin/activate
$ python3 -m pip install -U pip
$ pip install -r requirements.txt
```

#### *Execute main.py for Unix* 
```
$ python3 main.py
```

### B) *Setup for Windows* 

After downloading chessapp-main.zip from Github, extract it to a location of your choice (exemple : "PATH").
Or if you use git, download it from https://github.com/ValentinPhB/chessapp.git

Then, using cmd, go to "PATH", create a virtual environment and install packages from requirements.txt.
```
$ CD ../path/to/chessapp-main
$ py -m venv env
$ env\Scripts\activate.bat
$ py -m pip install -U pip
$ pip install -r requirements.txt
```

#### *Execute main.py for Windows*
```
$ python main.py
```

## 5. Advises for users

This application will suggest you all possible action.
Let yourself be guided.

## 6. Flake8 HTML reports

While this application is not running you can use flake8 (max_lenght == 119) and create HTML reports as follows :

### A) *Unix*

Go to the path 'chessapp-main' and execute this line :
```
$ flake8 ./chessapp/ --max-line-length=119 --ignore=E128 --format=html --htmldir=flake-report
```

### B) *Windows*
Go to the path 'chessapp-main' and execute this line :
```
$ flake8 .\chessapp\ --max-line-length=119 --ignore=E128 --format=html --htmldir=flake-report
```

## 7. Author


Valentin Pheulpin

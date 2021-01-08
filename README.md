# P4-Centre-Echecs
    
*This repository hosts a project to achieve during my training OpenClassRooms.com*

This script was created on Python 3.9.

The purpose of this progam is to manage an offline chess tournament.


## Installation

Download the files in the directories of your choice

### 1) Create a Virtual Environment :
 
Go to the directory where you downloaded files and run this command on your terminal:

    python3 -m venv env
    
Then, initialize it :
 
- On Windows, run:

        env\Scripts\activate.bat
    
- On Unix or MacOS, run:

        source env/bin/activate
        
For more information, refer to the python.org documentation :

<https://docs.python.org/3/tutorial/venv.html>
    
### 2) Install the requirements

Still on you terminal, with the environment activated, run the following command to install the required libraries
    
    pip install -r requirements
    
### 3) Run the script

You can run the script using this command :

    python chess_center.py

### 4) use flake8 html

In order to generate a flake8 report, run the following command :

    flake8 --format=html --htmldir=flake-report --exclude=env

Open the html file into the flake-report repertory to show the report.

### 5) Usage

Simply navigate following menu option.

Suisse algorithm is used to create match each round.

This program use tinyDB and create a db.json file at the root.

Take care:
- You can't delete players and tournaments,
- Suisse Algorithm is partial in this program

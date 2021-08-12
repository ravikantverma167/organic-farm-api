# organic-farm-api

Steps To Run organic-farm-api on your ubuntu20.04 machine.

### Step 1 — Setting Up Python 3

 `sudo apt update`
 `sudo apt -y upgrade`


### Step 2 — Check Version of Python

`python3 -V`

### Step 3 — Install pip

`sudo apt install -y python3-pip`

### Step 4 — Install venv

`sudo apt install -y python3-venv`

### Step 5 — Activate environment

Open the terminal in project folder and run command
`source organic-farm-env/bin/activate`

### Step 6 - Install dependencies

`pip install django`
`pip install djangorestframework`
`pip install django-cors-headers`

### Step 7 - Run Server

First move to OrganicFarmApi using command  `cd OrganicFarmApi` and then command
`python3 manage.py runserver`

Navigate to `http://localhost:8000/`. The app will automatically reload if you change any of the source files.

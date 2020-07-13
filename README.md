[![Build Status](https://travis-ci.com/huxaiphaer/travel_huxy.svg?branch=master)](https://travis-ci.com/huxaiphaer/travel_huxy)
[![codecov](https://codecov.io/gh/huxaiphaer/travel_huxy/branch/master/graph/badge.svg)](https://codecov.io/gh/huxaiphaer/travel_huxy)

# Huxy Travels

The number one stop experience for having fascinating tours.

### Requirements for setting up the project.
1. Python3. 
2. Flask
3. Virtualenv. 
4. Redis. 
You need to install redis on your machine, then afterwards you activate it.
This is the command you run on mac ``` brew services start redis```
5. Celery. This is also needed to perform some background processes, for this project, 
celery is already in the `requirements.txt` file.


### Installation on Mac

1 . First clone this repository 

```
https://github.com/huxaiphaer/travel_huxy.git
```
Add the following variables in your Environment Variables :


2 . Create a `.env` file in the root directory and add the following :

```buildoutcfg
FLASK_APP=run.py
DATABASE_URL=postgresql://postgres:your_db_password@localhost:5432/huxy_tours
REDIS_URL=redis://localhost:6379/0
WEATHER_API_KEY=1d4ce67223a53a013fc03ead36137396
```


3 . Then, create a virtual environment and install in on Mac :

```buildoutcfg
virtualenv env
source env/bin/activate
```

4.  After activating the `virtualenv`, then install the necessary dependencies :

```buildoutcfg
pip3 install -r requirements.txt
```

5. Activate celery to perform background tasks, open a new tab in the project directory (Ensure that if you have 
saved the Environment variables temporary, add them again to your new tab, plus activating the `virtualenv`).
Run this first command :

`celery -A app.tasks.weather_tasks.celery worker -l info`

Then, after running the above command, create another tab in the terminal with the environment variables and run
the command below :

`celery -A app.tasks.weather_tasks.celery beat -l info`


**HINT**:
_In order to run the commands smooth in different terminals ensure that the environment
variables a permanently saved._


6. After, that, open another terminal and now run the entire project with the following command:

`python3 run.py`

Then, Viola you easily navigate to the server URL


### Running Tests

Running tests of the project :

```buildoutcfg
nosetests
```

Running tests with coverage :

```buildoutcfg
nosetests --with-coverage
```


### Improvements
 Due to time being as a factor the following were left out, but they could improve on the 
 experience :
 
 - Docker
 - Exhausting more on unit tests
 - Hosting the project (e.g Heroku) etc.

### Contributors 

* Lutaaya Huzaifah Idris
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
6. Postgres DB


### Installation on Mac

1 . First clone this repository 

```
$ git clone https://github.com/huxaiphaer/travel_huxy.git
```

2 . Add the following variables in your Environment Variables permanently:

```buildoutcfg
FLASK_APP=run.py
DATABASE_URL=postgresql://postgres:your_db_password@localhost:5432/huxy_tours
REDIS_URL=redis://localhost:6379/0
WEATHER_API_KEY=1d4ce67223a53a013fc03ead36137396
SECRET_KEY=anything_you_put_here
APPLICATION_HOST=0.0.0.0
APPLICATION_PORT=5002
APPLICATION_DEBUG=False

```

After, setting up the environment variables add create a Postgres Database called `huxy_tours`, followed by running SQLAlchemy migrations with the commands 
below to create all the necessary tables :


**NOTE :**
- The commands below won't run unless  you have your Redis server running and as well
as setting all the environment variables above.

```
$ flask db init
$ flask db migrate
$ flask db upgrade

```


3 . Then, create a virtual environment and install in on Mac :

```buildoutcfg
$ virtualenv env
$ source env/bin/activate
```

4.  After activating the `virtualenv`, then install the necessary dependencies :

```buildoutcfg
$ pip3 install -r requirements.txt
```

5. Activate celery to perform background tasks, open a new tab in the project directory.
Run this first command :

`$ celery -A app.tasks.weather_tasks.celery worker -l info`

Then, after running the above command, create another tab in the terminal with the environment variables and run
the command below :

`$ celery -A app.tasks.weather_tasks.celery beat -l info`


**HINT**:

_In order to run the commands smooth in different terminals ensure that the environment
variables a permanently saved._


6. After, that, open another terminal and now run the entire project with the following command:

  `$ python3 run.py`

Then, Viola you easily navigate to the server URL 
`http://APPLICATION_HOST:APPLICATION_PORT` 


## Running with Docker.

The alternative way of running this project is by using Docker.

#### Requirements.

- Ensure that you have installed docker on your machine.

After, installing , then run the following command in the root folder of the 
project to spin the container.

```python3

 $ docker-compose up --build

```

If the command is successfully done , it shows the `celery` logs 
of the beats.

To access, the application use `http://APPLICATION_HOST:APPLICATION_PORT` 

 #### Endpoints to create a user account and login into the application

| HTTP Method   | End Point             | Action          |
| ------------- | --------------------- |-----------------|
| POST          | api/v1/register       |Create an account|
| POST          | /api/v1/login         |Login user       |



#### Other Endpoints.

| HTTP Method   | End Point                                   | Action                         |
| ------------- | ------------------------------------------  |--------------------------------|
| POST          | /api/v1/tourpackages                        |Creates tour packages.          |
| GET           | /api/v1/tourpackages                        |Get list of tour packages.      |
| GET           |/api/v1/tourpackages/<first_date>/<end_date> |Get tourpackages by date        | 
| GET           | /api/v1/tourpackages/<tour_id>              |Get tour package by ID.         |
| PUT           | /api/v1/tourpackages/<tour_id>              |Update tour package by ID.      | 
| DELETE        | api/v1/tourpackages/<tour_id>               |Delete tour package by ID       |
| POST          | /api/v1/booking/<tour_id>                   |Make a booking request          |
| DELETE        | /api/v1/booking/<tour_id>                   |Delete a booking request        |
| GET           | /api/v1/weather/{lat}/{lon}                 |Get weather updates by location |
|               |                                             |                                |


### Further More API Docs.

This is the [link](https://huxytours.docs.apiary.io/) to the API Docs.


### Running Tests Locally

Running tests of the project :

```python3
$ nosetests
```

Running tests with coverage :

```python3
$ nosetests --with-coverage
```


### Improvements
 Due to time being as a factor the following were left out, but they could improve on the 
 experience :
 
 - _Exhausting more on unit tests_.
 - _Hosting the project (e.g Heroku) etc._

### Contributors 

* [Lutaaya Idris](https://github.com/huxaiphaer)

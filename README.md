# Courses App for NeoBis


## API BluePrint URL:

```sh
https://app.apiary.io/coursesapp3
```

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/JediFaust/courses.git
$ cd courses
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd courses
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/courses/`.


## Walkthrough

Go to admin panel and add some courses to models

### Courses List

Get list of courses by going to `http://127.0.0.1:8000/courses/`

### Course Detail

For getting the concrete information about the first course go to `http://127.0.0.1:8000/courses/1` and etc



## Tests
(This feature is on development stage)
To run the tests, `cd` into the directory where `manage.py` is:
```sh
(env)$ python manage.py test coursesapp
```


# Timetable Schedulr
 This is a web app designed to help lecturers find available lecture periods or venues and also re-schedule their own periods.

## Setting up the project

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/dunfred/TimetableSchedulr.git
$ cd TimetableSchedulr
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd TimetableSchedulr
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`

## Project Presentaion
[View file here](https://docs.google.com/presentation/d/1I7_wptVINioTSd7CtIkJQl_MoLVk4qALV5z8KF9cuZM/edit#slide=id.g1f87997393_0_787)

### Authors
- Fred Dunyo `https://github.com/dunfred`
- Jeremiah Quaynor `https://github.com/Jeremiah-Quaynor`
- Joshua Tetteh `https://github.com/joshthedevelopa`

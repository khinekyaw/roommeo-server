# Roommeo Backend


## Description
Backend Api for Roommeo


## Install

1. clone the repo

```
$ git clone https://github.com/khinekyaw/roommeo-server.git
```

2. install packages

```
$ cd roommeo-server
$ pipenv install
$ pipenv shell
```

3. migrate

```
$ python manage.py migrate
```

##

## Setup

Create `.env` file that include:

```env eg
DEBUG = True
SECRET_KEY = roommeo-secret
GOOGLE_ID =
GOOGLE_SECRET =
GOOGLE_REDIRECT_URL = http://localhost:3000
```

## Start development

```
python manage.py runserver
```

##

## Bugs

1. -

## Working Updates

1. Rooms
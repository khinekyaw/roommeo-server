# Roommeo Backend


## Description
Backend Api for Roommeo


## Install

1. clone the repo

```
git clone https://github.com/khinekyaw/roommeo-server.git
```

2. install packages

```
cd roommeo-server
pipenv install
pipenv shell
```

##

## Setup

1. create `.env` file that include:

```env eg
DEBUG = True
SECRET_KEY = your-secret
GOOGLE_ID =
GOOGLE_SECRET =
GOOGLE_REDIRECT_URL = http://localhost:3000
```

2. migrate

```
python manage.py migrate
```

3. create a '\static' folder in root directory

4. collectstatic

```
python manage.py collectstatic
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
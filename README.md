# Базовая Админка на Джанго #

## To init Django: ##

1) Create virtual environment for python3.6:
```
virtualenv -p python3.6 venv
. venv/bin/activate
```

2) Install requirements:
```
python -m pip install -r requirements.txt
```

3) Make a copy of local.py.default named local.py and set valid local values:
```
cp settings/local.py.default settings/local.py
```

4) create database and apply migrations:
```
sudo -u postgres psql -c 'create database basic_admin;'
python manage.py migrate
```
5) create basic user and client:
```
python scripts/fill_db

```

## To run server: ##

```
. venv/bin/activate
python manage.py runserver
```

## Development ##

1) install requirements-dev.txt
```
python -m pip install -r requirements-dev.txt
```

2) activate pre-commit
```
pre-commit install
```


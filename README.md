# Giphy

A gif serving api developed using Django. It has authentication using both json web token and tokenauth.


## Api Endpoints

- `/api/token` to retreive access token
- `/tags` To create, delete or list available tags
- `/gifs` To upload, list or delete gifs

### Example Usage

Using httpie
```
http POST https://127.0.0.1:80000/api/token email=123@test.com password=testpassword
http post http://127.0.0.1:8000/tags/ "Authorization: Token YOURTOKEN" name=testtag
```

## Installation

Clone this repo and cd into it
```
git clone https://github.com/b4skyx/giphapi
cd giphapi
```


Install python-venv and create a virtual environment to isolate the deps. *[Optional]*
```python
pip install --user python-venv
python -m venv .venv
source .venv
```

Install the dependancies
```
pip install djangorestframework djangorestframework-simplejwt django
```

##### Initial Configuration

```
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py runserver
```

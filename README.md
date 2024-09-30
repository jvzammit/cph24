# cph24

[Django Day CPH 2024](https://2024.djangoday.dk/) proof of concept application.

## Demo application

This shows a use case stripped to the minimum possible detail. For demo purposes.

Django project called `project`, with `config` directory containing config, including Django `settings` module.

Starts with Django project and an app called `agents`.

`agents` app contains models for `Conversation` and `Message`.

Both `Conversation` and `Message` have unique UUID keys as set by an external platform.

We expose a webhook with messages and conversations; when we receive such webhook request we want to:

1. store the message and conversation
2. send the updated conversation to an indexing service used for autosuggest; this is a network-bound request

## Getting started

Make sure you have [poetry](https://python-poetry.org/) set up locally.

There are various ways to do this:

* Install poetry: https://python-poetry.org/docs/#installation
* Install poetry with [pyenv](https://github.com/pyenv/pyenv): https://python-poetry.org/docs/managing-environments/

What you do on your local is up to you. Just make sure to run below commands within the expected virtualenv. Pro tip: To avoid having to prefix every command with `poetry run`, enter a `poetry shell` first.

* Create and activate a Python virtual env. For example using pyenv:

 ```
 pyenv virtualenv 3.12 venv
 pyenv activate venv
 ```

* Install the required dependencies, including local `dev` dependencies (used for running tests):

 ```
 poetry install
 ```

Create a copy of the `.env` file, in this demo for sharing environment variables:

```
$ cd project
$ cp .env.example .env
```

Make sure you're in `project` directory before running the test commands.

* Run the tests

  ```
  $ ./manage.py test
  ```

* Run tests and generate coverage report:

  ```
  $ coverage run ./manage.py test && coverage report -m
  ```

`coverage` is configured its config file `.coveragerc`.

Sample output:

```
$ coverage run ./manage.py test && coverage report -m

Found 2 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.018s

OK
Destroying test database for alias 'default'...
Name                                Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------------------
agents/__init__.py                      0      0      0      0   100%
agents/admin.py                         0      0      0      0   100%
agents/apps.py                          4      0      0      0   100%
agents/migrations/0001_initial.py       6      0      0      0   100%
agents/migrations/__init__.py           0      0      0      0   100%
agents/models.py                       19      0      0      0   100%
config/__init__.py                      0      0      0      0   100%
config/settings.py                     18      0      0      0   100%
config/urls.py                          3      0      0      0   100%
-------------------------------------------------------------------------------
TOTAL                                  50      0      0      0   100%
```

You can use `nox` command as well to run linting, mypy, tests/coverage in one "nox" command:

```
$ nox
```

## Running the applications

Make sure you're in `project` directory.

### Run Django

First time:

```
$ manage.py migrate
```

And from then on:

```
$ manage.py runserver
```

This will run Django at `http://localhost:8000/`

### Run FastAPI

To run FastAPI at `http://localhost:8001/`

```
$ fastapi dev backend/main.py --port 8001
```

You can tweak ports as you like.

To run FastAPI tests:

```
pytest backend/tests
```

Sample output:

```
$ pytest backend
========================= test session starts ==========================
platform darwin -- Python 3.12.3, pytest-8.3.3, pluggy-1.5.0
django: version: 5.1.1
rootdir: /Users/jv/dev/cph24
configfile: pyproject.toml
plugins: asyncio-0.24.0, anyio-4.6.0, django-4.9.0, Faker-30.0.0
asyncio: mode=Mode.AUTO, default_loop_scope=function
collected 4 items

backend/tests/domains/messages/test_routes.py .                  [ 25%]
backend/tests/domains/messages/test_repositories.py ..           [ 75%]
backend/tests/domains/messages/test_services.py .                [100%]

========================== 4 passed in 0.12s ===========================
```

For coverage check the `test_backend` session in the `noxfile`.
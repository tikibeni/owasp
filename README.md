# OWASP-5

This is cybersecurity themed course project regarding the University of Helsinki course Cyber Security Base (TKT20009).

The intention of this project is solely to create at least five web application risks listed on [OWASP](
https://owasp.org/www-project-top-ten/) inside this template project, from which I will build a report.

## Installation guide

1. Clone:

```shell
~$ git clone git@github.com:tikibeni/owasp.git
~$ cd owasp
~/owasp$ 
```

3. Migrate & run:

```shell
~/owasp$ python3 manage.py migrate
~/owasp$ python3 manage.py runserver   
```
   
4. Open the frontend via browser within: http://127.0.0.1:8000/

### Dependencies

You will need Python 3.x.y and Django. I used Python [3.9.5](https://www.python.org/downloads/release/python-395/)
and Django [4.0](https://docs.djangoproject.com/en/4.0/releases/4.0/).

## Usage

### Login credentials

| role          | username | password |
|---------------|----------|----------|
| administrator | admin    | admin    |
|               |          |          |

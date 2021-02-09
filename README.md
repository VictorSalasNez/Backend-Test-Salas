# Backend-Test-Salas

## About The Project

### Built With

* [Django](https://www.djangoproject.com/)
* [bootstrap](https://getbootstrap.com/)

## Getting Started

### Prerequisites

* Python 3.8 with virtualenv

### Setup

* create virtualenv named `venv`

```sh
virtualenv venv
```

* activate environment and install requirements.txt

```sh
source venv/bin/activate
pip install -r requirements.txt
```

### Inicialize server

* Run server

```sh
python manage.py runserver
```

* Lgin as Nora
    * UserName: Nora
    * Password: Cornershop1


### Testing

* Run tests
```sh
coverage run --source=employees,main,menu manage.py test
```
* see report

```sh
coverage report -m
```
* html report

```sh
coverage html
```

* Open the index.html file to see a web coverage report

<!-- CONTACT -->
## Contact

Victor Salas - [@victorfsalasn](https://www.instagram.com/victorfsalasn/) - victor.salasnez@gmail.com

# Fizz-Buzz-REST-Server

Setup

    First we need to setup our virtual environment

        python -m venv ./venv

    To activate the virtual environment run following command in command line

        venv\Script\activate

    In settings.py add database details

        for ex:

        DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'fizzbuzz',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost'
        }

    }

    In order to Django ORM to work you need to install psycopg2 library. Which will handle the Django ORM transactions with PostgreSQL database.

        pip install psycopg2

    You need to run following commands to transfer all django in built tables and our model tables to be transferred into our PostgreSQL database.

        python manage.py makemigrations
        python manage.py migrate

Now to run application

    Change directory
        cd .\FizzBuzzProject\

    To start our application run following command
        python manage.py runserver

API Documentation
1)Fizz Buzz endpoint

        url:localhost:8000/fizzbuzz

        query params:
            int1:2 //int
            int2:3 //int
            limit:6 //int
            str1:fizz //string
            str2:buzz //string

        output:
            [
            "1",
            "fizz",
            "buzz",
            "fizz",
            "5",
            "fizzbuzz"
            ]

    2)statistics:

        url:localhost:8000/statistics

        output:
            {
                "max_used_parameter": [
                    {
                        "id": 2,
                        "int1": 1,
                        "int2": 2,
                        "limit": 5,
                        "str1": "aa",
                        "str2": "bb",
                        "hits": 9
                    }
                ]
            }

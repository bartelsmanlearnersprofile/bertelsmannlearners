### Migration commands
```
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ python manage.py db --help
```

### Coverage command

    coverage run --source=./tests -m pytest discover -s tests/ && coverage report

# Restaurant eMenu
- download project from github
```sh
git clone https://github.com/matmajessuper/Restauracja.git
```
- create virtualenv
- install requirements.txt
```sh
pip install -r requirements.txt
```

- collect static files
```sh
python manage.py collectstatic
```
- migrate data
```sh
python manage.py makemigrations
python manage.py migrate
```
- load data for database from datadump.json
```sh
python manage.py loaddata datadump.json
```
- and finally start a server
```sh
python manage.py runserver
```



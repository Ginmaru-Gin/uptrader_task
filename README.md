# uptrader_task

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd uptrader
python3 manage.py migrate
python3 manage.py createsuperuser
pyton3 manage.py loaddata db_dump_example.json
python3 manage.py runserver
```

# uptrader_task

```sh
git clone git@github.com:Ginmaru-Gin/uptrader_task.git
cd uptrader_task
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd uptrader
python3 manage.py migrate
python3 manage.py createsuperuser
pyton3 manage.py loaddata db_dump_example.json
python3 manage.py runserver
```

# hillel-10
<ol>
<li>Install dependency</li>

```
pip install -r reqquirements.txt
```

<li>Run broker</li>

```
docker run -d -p 5672:5672 rabbitmq
```

<li>Set your TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN as env vars</li>
```
export TWILIO_ACCOUNT_SID="some"
export TWILIO_AUTH_TOKEN="some_2"
```

<li>Run worker process</li>>

```
celery -A hillel_10 worker -l INFO
```

<li>Run Django app server</li>

```
python manage.py runserver
```
</ol>

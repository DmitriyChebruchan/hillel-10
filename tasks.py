import time

from celery import Celery

app = Celery("hello", broker="amqp://guest@localhost//")


@app.task
def hello(sleep_time):
    print(
        f"hello from inside of the task with sleep period{sleep_time} "
        f"seconds"
    )
    time.sleep(sleep_time)
    print("Hello after sleep")
    return "hello world"

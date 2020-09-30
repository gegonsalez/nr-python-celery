import newrelic.agent
from celery import Celery
from time import sleep

app = Celery('tasks')

@app.task
def add(x, y):
    func_a()
    return x + y

@newrelic.agent.background_task()
def func_a():
	sleep(1)
	func_b()

@newrelic.agent.function_trace()
def func_b():
    sleep(3)
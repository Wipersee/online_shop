from __future__ import absolute_import, unicode_literals
from celery import task
from .models import Order

@task()
def task_number_one():
    print(Order.objects.all())
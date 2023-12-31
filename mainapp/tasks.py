
from celery import shared_task
from datetime import datetime
from .models import CounterHistory

@shared_task
def add_to_counter(amount):
    current_counter_value = CounterHistory.get_current_counter()
    new_counter_value = current_counter_value + amount
    CounterHistory.objects.create(value=new_counter_value, timestamp=datetime.now())

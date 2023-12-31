from django.db import models

class CounterHistory(models.Model):
    value = models.IntegerField()
    timestamp = models.DateTimeField()

    @classmethod
    def get_current_counter(cls):
        latest_entry = cls.objects.last()
        return latest_entry.value if latest_entry else 0
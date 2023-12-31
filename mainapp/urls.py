from django.urls import path
from .views import update_counter, get_counter_history

urlpatterns = [
    path('update_counter/', update_counter, name='update_counter'),
    path('get_counter_history/', get_counter_history, name='get_counter_history'),
]

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .tasks import add_to_counter
from .models import CounterHistory
from datetime import datetime, timedelta
from django.utils import timezone

@csrf_exempt
@require_POST
def update_counter(request):
    amount = int(request.POST.get('amount', 0))
    add_to_counter.delay(amount)
    return JsonResponse({'status': 'success', 'message': 'Task qued successfully'})

def get_counter_history(request):
    history = CounterHistory.objects.all().order_by('-timestamp')
    data = [{'timestamp': entry.timestamp, 'value': entry.value} for entry in history]
    return JsonResponse({'counter_history': data})

def scheduled_task():
    current_counter_value = CounterHistory.get_current_counter()
    CounterHistory.objects.create(value=current_counter_value, timestamp=datetime.now())

  
    # CounterHistory.objects.all().delete()

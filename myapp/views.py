from django.shortcuts import render
from .models import SensorData
from django.db.models import Max, Min, Avg

def index(request):
    data = SensorData.objects.all().order_by('-timestamp')[:10]
    return render(request, 'index.html', {'data': data})




def analysis(request):
    max_temperature = SensorData.objects.filter(topic='sensor/temperature').aggregate(Max('value'))['value__max']
    min_temperature = SensorData.objects.filter(topic='sensor/temperature').aggregate(Min('value'))['value__min']
    avg_temperature = SensorData.objects.filter(topic='sensor/temperature').aggregate(Avg('value'))['value__avg']
    max_humidity = SensorData.objects.filter(topic='sensor/humidity').aggregate(Max('value'))['value__max']
    min_humidity = SensorData.objects.filter(topic='sensor/humidity').aggregate(Min('value'))['value__min']
    avg_humidity = SensorData.objects.filter(topic='sensor/humidity').aggregate(Avg('value'))['value__avg']
    return render(request, 'analysis.html', {
        'max_temperature': max_temperature,
        'min_temperature': min_temperature,
        'avg_temperature': avg_temperature,
        'max_humidity': max_humidity,
        'min_humidity': min_humidity,
        'avg_humidity': avg_humidity,
    })

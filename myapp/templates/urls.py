from django.urls import path
from myapp.views import index, analysis

urlpatterns = [
    path('', index, name='index'),
    path('analysis/', analysis, name='analysis'),
]

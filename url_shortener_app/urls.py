from django.urls import path
from .views import shorten_url, resolve_short_url

urlpatterns = [
    path('shorten/', shorten_url, name='shorten_url'),
    path('<str:short_url>/', resolve_short_url, name='resolve_short_url'),
]

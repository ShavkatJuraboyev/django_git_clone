from django.urls import path
from .views import main, persons
urlpatterns = [
    path('', main, name='main'),
    path('pers/', persons, name='pers')
]
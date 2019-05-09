from django.urls import path
from . import views

app_name = 'api_caller'

urlpatterns = [
    path('', views.test_api, name='test_api'),
    path('wiki_api', views.wiki_api, name='wiki_api'),
]


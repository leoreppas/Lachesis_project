from django.conf.urls import url
from lachesis import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

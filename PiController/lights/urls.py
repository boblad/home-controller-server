from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^on$', views.on, name='on'),
    url(r'^off$', views.off, name='off')
]

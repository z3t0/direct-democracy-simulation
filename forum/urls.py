from django.conf.urls import url

from . import views

app_name = 'forum'
urlpatterns = [
    # forum index
    url(r'^$', views.index, name='index'),
]

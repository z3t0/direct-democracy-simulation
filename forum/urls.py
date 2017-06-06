from django.conf.urls import url

from . import views

urlpatterns = [
    # forum index
    url(r'^$', views.index, name='index'),
]

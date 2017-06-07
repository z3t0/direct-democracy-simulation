from django.conf.urls import url, include

from . import views

app_name = 'forum'
urlpatterns = [
    # forum index
    url(r'^$', views.index, name='index'),
    url(r'^(?P<issue_id>[0-9]+)/$', views.issueDetail, name='issue'),
]

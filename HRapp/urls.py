from django.conf.urls import url
from . import views

app_name = 'HRapp'

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^add/$', views.adddetails, name='adddetails'),
    url(r'^list/$', views.listcontent, name='list'),
]

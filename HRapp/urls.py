from django.conf.urls import url

from . import views

from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'HRapp'

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    url(r'^add/$', views.adddetails, name='adddetails'),
    url(r'^list/$', views.listcontent, name='list'),
    url(r'^details/', views.Details.as_view(), name='apidetails'),
    url(r'^post/', views.Details.as_view(), name='apiadddetails')
]

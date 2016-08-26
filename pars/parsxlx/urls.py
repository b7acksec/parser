from django.conf.urls import url
from parsxlx import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add/$', views.parsxlx, name='add_xls'),
]
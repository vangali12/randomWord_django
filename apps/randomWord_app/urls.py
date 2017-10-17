from django.conf.urls import url
from django.contrib import admin

from . import views

def test(request):
	print """


	some other thing



	"""

urlpatterns = [
	url(r'^$', views.index),
	url(r'^getVal$', views.getVal)

]
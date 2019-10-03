from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.for_edu, name='for_edu'),
]

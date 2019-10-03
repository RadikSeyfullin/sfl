from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.for_organisation, name='for_organisation'),
]

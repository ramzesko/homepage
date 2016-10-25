from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_index, name='index'),
    url(r'^cv', views.show_cv, name='cv'),
]
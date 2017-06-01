from django.conf.urls import url

from . import views

# from polls import views 같은 명령

urlpatterns = [
    url(r'^$', views.index, name='index'),
]


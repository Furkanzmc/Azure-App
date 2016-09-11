from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/$', views.TestAPIView.as_view(), name='test-api'),
]

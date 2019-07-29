from django.conf.urls import  url
from . import views
from django.conf import settings
from django.core.mail import EmailMessage

urlpatterns = [
    url(r'^contacts/$', views.contact, name='contact'),

]

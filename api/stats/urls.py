from django.views.generic import TemplateView
from django.urls import path,re_path, include
from .views import os_view,filesystem_view
urlpatterns = [
    re_path(r'^(?P<ipaddress>(?:(?:0|1[\d]{0,2}|2(?:[0-4]\d?|5[0-5]?|[6-9])?|[3-9]\d?)\.){3}(?:0|1[\d]{0,2}|2(?:[0-4]\d?|5[0-5]?|[6-9])?|[3-9]\d?))/os$', os_view, name='Operating System Detail'),
    re_path(r'^(?P<ipaddress>(?:(?:0|1[\d]{0,2}|2(?:[0-4]\d?|5[0-5]?|[6-9])?|[3-9]\d?)\.){3}(?:0|1[\d]{0,2}|2(?:[0-4]\d?|5[0-5]?|[6-9])?|[3-9]\d?))/filesystem$', filesystem_view, name='File System Detail')
]

# -*- coding:utf-8 -*-
from django.conf.urls import url
from .views import check_code, home


urlpatterns = [
    url(r'^checkcode/', check_code),
    url(r'^$', home),

]

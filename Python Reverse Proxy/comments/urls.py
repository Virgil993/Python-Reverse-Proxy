import imp
from django.urls import path
from . import views


# URLConf
urlpatterns = []
for i in range(1,501):
    urlpatterns.append(path(str(i)+"/",views.comments))
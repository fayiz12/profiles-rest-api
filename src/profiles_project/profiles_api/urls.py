from django.contrib import admin
from django.urls import include,path
from . import  views


urlpatterns=[

    path('hello-view/',views.HelloApiView.as_view())
]

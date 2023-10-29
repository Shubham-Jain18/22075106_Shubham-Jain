from django.urls import path
from django.http import HttpResponse
from shortener.views import createURL, routetoURL, URLlist

urlpatterns = [

    path('', createURL),
    path('<slug:key>/', routetoURL),
    path('urllist', URLlist)
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('quotes.urls')),   #To use the "urls.py" file of the "qoute" app
]

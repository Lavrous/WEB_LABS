# irezumi101/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('irezumi.urls')),
    path('masters/', include('masters.urls')), 
]

handler404 = 'irezumi.views.page_not_found'
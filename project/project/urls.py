from django.contrib import admin
from django.urls import path, include
import app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.home, name='home'),
    path('app/', include('app.urls')),
]

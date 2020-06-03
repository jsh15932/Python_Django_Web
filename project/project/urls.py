from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import app.views
import member.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.home, name='home'),
    path('app/', include('app.urls')),
    path('member/', include('member.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
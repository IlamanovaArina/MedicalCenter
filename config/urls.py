from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('medical.urls', namespace='medical')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

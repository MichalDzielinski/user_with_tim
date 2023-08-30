from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('app.urls')),
]

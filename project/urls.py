from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('',include('tasks.urls')),
    path('admin/', admin.site.urls),
    # path('accounts/', include('accounts.urls')),
    path('tasks/', include('tasks.urls')),
    path('', include('tasks.urls')), 
]

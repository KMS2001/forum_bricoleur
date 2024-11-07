from django.contrib import admin
from django.urls import path, include  # inclure "include"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls')),  # Inclure les URLs de l'app `forum`
]

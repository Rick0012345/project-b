
from django.contrib import admin
from django.urls import path
from .views import VizualizarSalas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', VizualizarSalas.as_view(), name='home-b'),
]

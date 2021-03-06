from django.urls import path
from django.contrib import admin
from django.urls.conf import include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='home-page'),
    path('category/<int:category_id>', views.get_category)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

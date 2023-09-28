from django.urls import path
from . import views

from django.views.generic import TemplateView

# app_name = 'photography'  # Replace with your app's name NAMESPACE

urlpatterns = [
    path('about/', TemplateView.as_view(template_name = 'about.html'), name = 'about'),
    # path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('', views.GalleryDetailView.as_view(), name='home'),
]
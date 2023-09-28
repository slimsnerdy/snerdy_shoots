from .views import contactView
from django.urls import path

urlpatterns = [
    path('contact/', contactView, name = 'contact'),
    # path('success/', successView, name = 'success'),
]
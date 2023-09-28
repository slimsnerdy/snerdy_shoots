from django.shortcuts import render
# from django.views import generic
from django.views.generic import ListView, DetailView
from .models import Gallery


# Create your views here.

# class GalleryListView(ListView):
#     model = Gallery
#     template_name = 'gallery.html'
#     context_object_name = 'galleries'


class GalleryDetailView(DetailView):
    model = Gallery
    template_name = 'gallery.html'
    context_object_name = 'gallery'

    def get_object(self, queryset=None):
        # return Gallery.objects.get(pk=1)  # Example: Display the gallery with PK 1 by default
        return Gallery.objects.get(is_default=True)
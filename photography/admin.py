from django.contrib import admin
from .models import Gallery, Image

# Register your models here.

class ImageInline(admin.TabularInline):  # You can also use admin.StackedInline for a different display style
    model = Image
    extra = 64  # Set the number of empty image forms to display (adjust as needed)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'status', 'is_default')
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate the slug based on the title
    inlines = [ImageInline]  # Add the ImageInline formset

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'image', 'upload_date')
from django.db import models
from django.urls import reverse


STATUS = (          #tuple
    (0,"Draft"),
    (1,"Publish")
)

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    meta_description = models.CharField(max_length=150, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    is_default = models.BooleanField(default=False)  # Add this field

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Galleries"

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse('post_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        existing_default_gallery = Gallery.objects.filter(is_default=True).first()

        if existing_default_gallery is None:
            # If there is no existing default gallery, this gallery becomes the default
            self.is_default = True
        elif self.is_default and self != existing_default_gallery:
            # If this gallery is marked as default and it's not the existing default gallery, unmark the existing one
            existing_default_gallery.is_default = False
            existing_default_gallery.save()

        super().save(*args, **kwargs)

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', blank=False)
    image_alt = models.CharField(max_length=150, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.gallery.title
from django.db import models

class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/', default='static/gallery/selfie.jpg')
    description = models.TextField(blank=True)
    def __str__(self):
        return self.title
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100)
    html = models.TextField()
    css = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='post_pics')

    def __str__(self):
        return self.title
    
    def  get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.image.path)
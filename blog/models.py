from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.shortcuts import reverse

class Post(models.Model):
    
    Captions = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg')
    Comment = models.TextField(blank= True)
    date_posted = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Captions}"
    
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


        #img  = Image.open(self.image.path)
        
        # if img.height >300 or img.width > 300:
        #     output_size = (300,300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)
from django.db import models

# Create your models here.
class Profil(models.Model):
    enterprise_title = models.CharField(max_length=250)
    rue_1 = models.CharField(max_length = 250)
    rue_2 = models.CharField(max_length = 250)
    phone_number_1 = models.CharField(max_length = 15)
    phone_number_2 = models.CharField(max_length=15)
    about = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.enterprise_title

class MediaContent(models.Model):
    title = models.CharField(max_length=250)
    description =models.TextField()
    image = models.ImageField(upload_to='images')
    is_banner = models.BooleanField()

    def __str__(self):
        return self.title


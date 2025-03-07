from django.db import models
class Post(models.Model): # new
 text = models.TextField()


 from django.db import models
class Post(models.Model):
 text = models.TextField()
 def __str__(self): # new
    return self.text[:50]


# Create your models here.

from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length = 100)
    blog_text  = models.TextField()
    blog_img  = models.ImageField(upload_to="images/", default = "default.jpg")

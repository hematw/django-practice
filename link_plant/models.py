from django.db import models

# Create your models here.

class Profile(models.Model):
    BG_COLORS = (
        ("blue", "Blue"),
        ("red", "Red"),
        ("yellow", "Yellow"),
    )
    
    name= models.CharField(max_length=100)
    slug= models.SlugField(max_length=100, unique=True)
    bg_color= models.CharField(max_length=100, choices=BG_COLORS)
    
    def __str__(self):
        return self.name
    
    
class LinkP(models.Model):
    text= models.CharField(max_length=100)
    url= models.URLField(max_length=200)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links")
    
    def __str__(self):
        return f"{self.text} - {self.url}"
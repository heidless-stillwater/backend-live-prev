from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Research(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    link = models.CharField(max_length=250)
    link_blog = models.CharField(max_length=250, default="#")
    image = models.ImageField(upload_to='images')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
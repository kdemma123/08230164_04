from django.db import models

# Learning Journey Model
class LearningJourney(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

# About Me Model
class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    education = models.CharField(max_length=200)
    village = models.CharField(max_length=100)

    def __str__(self):
        return self.name

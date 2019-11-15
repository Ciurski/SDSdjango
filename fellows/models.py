from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Adress(models.Model):
    post_code = models.CharField(max_length=6)
    street =  models.CharField(max_length=6)
    city = models.CharField(max_length=6)
    house_nummer = models.CharField(max_length=6)
    apartment = models.CharField(max_length=6)

    def __str__(self):
        return "{}, {}".format(self.street, self.house_nummer)

class Author(models.Model):
    name = models.CharField(max_length=6)
    surname = models.CharField(max_length=6)

    def __str__(self):
        return "{}., {}".format(self.name[0], self.surname)



class Profile(models.Model):
    user = models.OneToOneField(User, blank=True, null=True, default=None, on_delete=models.SET_NULL, related_name = 'user')
    profile_pic = models.ImageField(upload_to='img', blank=True)
    adress = models.OneToOneField(Adress, blank=True, null=True, default=None, on_delete=models.SET_NULL, related_name = 'adress', editable=True)

class Article(models.Model):
    # Relations
    authors = models.ManyToManyField(Author, blank=True, editable=True,default=None)
    profile = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
    # Attributes Mandatory
    title = models.CharField(max_length=6)
    dziedzina = models.CharField(max_length=6)
    publish_date = models.DateField(max_length=6)
    # Attributes Optional
    content = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.title

class WorkExperience(models.Model):
    # Relations
    work_experience = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
    # Attributes
    company = models.CharField(max_length=6)
    position = models.CharField(max_length=6)
    start_time = models.DateField(max_length=6)
    end_time = models.DateField(max_length=6)

    def __str__(self):
        return self.company

class Project(models.Model):
    # Relations
    work_experience = models.ForeignKey(WorkExperience, blank=True, null=True, on_delete=models.CASCADE)
    # Attributes Mandatory
    title = models.CharField(max_length=6)
    start_time = models.DateField(max_length=6)
    end_time = models.DateField(max_length=6)
    position = models.CharField(max_length=6)

    def __str__(self):
        return self.title

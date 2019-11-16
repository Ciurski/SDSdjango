from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class Adress(models.Model):
    post_code = models.CharField(max_length=6)
    street =  models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    house_nummer = models.CharField(max_length=3)
    apartment = models.CharField(max_length=3)

    def __str__(self):
        return "{}, {}".format(self.street, self.house_nummer)

class Author(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=50)

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
    title = models.CharField(max_length=125)
    field = models.CharField(max_length=25, default="")
    publish_date = models.DateField()
    # Attributes Optional
    content = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        return self.title

class WorkExperience(models.Model):
    # Relations
    profile = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
    # Attributes
    company = models.CharField(max_length=25)
    position = models.CharField(max_length=25)
    start_time = models.DateField()
    end_time = models.DateField()

    def __str__(self):
        return self.company

class Project(models.Model):
    # Relations
    work_experience = models.ForeignKey(WorkExperience, blank=True, null=True, on_delete=models.CASCADE)
    # Attributes Mandatory
    title = models.CharField(max_length=125)
    start_time = models.DateField()
    end_time = models.DateField()
    position = models.CharField(max_length=25)

    def __str__(self):
        return self.title

class University(models.Model):
    # Realtions
    profile = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
    # Attributes Mandatory
    name = models.CharField(max_length=125)
    city = models.CharField(max_length=25)
    degree_cours = models.CharField(max_length=25)
    start_time = models.DateField()
    end_time = models.DateField()
    # Attributes Optional
    students_group = models.CharField(max_length=125, blank=True, default='')

    def __str__(self):
        return self.name

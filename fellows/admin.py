from django.contrib import admin
from fellows.models import Profile, Adress, Article, Author, WorkExperience, Project, University
# Register your models here.

class AuthorInLine(admin.TabularInline):
    model = Author

class ArticleAdmin(admin.ModelAdmin):
    inlines = [AuthorInLine]

class ArticleInLine(admin.TabularInline):
    model = Article

class WorkExperienceInLine(admin.TabularInline):
    model = WorkExperience

class UniversityInLine(admin.TabularInline):
    model = University

class ProfileAdmin(admin.ModelAdmin):
    inlines = [WorkExperienceInLine, ArticleInLine, UniversityInLine]

class ProjectInLine(admin.TabularInline):
    model = Project

class WorkExperienceAdmin(admin.ModelAdmin):
    inlines = [ProjectInLine]
admin.site.register(Adress)
admin.site.register(Article)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)

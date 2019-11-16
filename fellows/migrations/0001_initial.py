# Generated by Django 2.2.2 on 2019-11-15 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_code', models.CharField(max_length=6)),
                ('street', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=6)),
                ('house_nummer', models.CharField(max_length=6)),
                ('apartment', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=6)),
                ('surname', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=6)),
                ('start_time', models.DateField(max_length=6)),
                ('end_time', models.DateField(max_length=6)),
                ('position', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=6)),
                ('position', models.CharField(max_length=6)),
                ('start_time', models.DateField(max_length=6)),
                ('end_time', models.DateField(max_length=6)),
                ('projects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fellows.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='img')),
                ('adress', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fellows.Adress')),
                ('user', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='competitor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=6)),
                ('dziedzina', models.CharField(max_length=6)),
                ('publish_date', models.DateField(max_length=6)),
                ('content', models.FileField(blank=True, null=True, upload_to='pdfs/')),
                ('authors', models.ManyToManyField(to='fellows.Author')),
            ],
        ),
    ]

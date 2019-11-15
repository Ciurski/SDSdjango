# Generated by Django 2.2.2 on 2019-11-15 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fellows', '0003_auto_20191115_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='authors',
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(blank=True, null=True, to='fellows.Author'),
        ),
    ]

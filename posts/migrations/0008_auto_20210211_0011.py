# Generated by Django 3.1.6 on 2021-02-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20210210_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='posts.Tag'),
        ),
    ]
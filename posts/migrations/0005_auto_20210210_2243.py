# Generated by Django 3.1.6 on 2021-02-10 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_relation_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['tag']},
        ),
        migrations.AddField(
            model_name='tag',
            name='posts',
            field=models.ManyToManyField(to='posts.Post'),
        ),
        migrations.DeleteModel(
            name='Relation',
        ),
    ]
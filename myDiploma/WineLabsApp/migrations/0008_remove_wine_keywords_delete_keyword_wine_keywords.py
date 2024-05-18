# Generated by Django 5.0.4 on 2024-04-15 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WineLabsApp', '0007_keyword_wine_keywords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wine',
            name='keywords',
        ),
        migrations.DeleteModel(
            name='Keyword',
        ),
        migrations.AddField(
            model_name='wine',
            name='keywords',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
# Generated by Django 4.2.1 on 2023-08-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('with_medicine_free', '0008_free_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='free_comment',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
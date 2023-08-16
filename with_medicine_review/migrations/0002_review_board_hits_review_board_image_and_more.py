# Generated by Django 4.2.1 on 2023-08-16 18:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('with_medicine_review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review_board',
            name='hits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review_board',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='review_board',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='review_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review_board',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review_comment',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='review_comment',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_posts_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
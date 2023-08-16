# Generated by Django 4.2.1 on 2023-08-15 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('with_medicine_review', '0007_review_board_image'),
    ]

    operations = [
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
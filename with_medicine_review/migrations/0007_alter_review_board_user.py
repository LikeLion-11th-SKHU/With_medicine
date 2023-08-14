# Generated by Django 4.2.1 on 2023-08-14 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('with_medicine_review', '0006_review_board_hits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review_board',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]

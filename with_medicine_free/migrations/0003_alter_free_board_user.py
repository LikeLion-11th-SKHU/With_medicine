# Generated by Django 4.2.1 on 2023-08-12 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('with_medicine_free', '0002_alter_free_board_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='free_board',
            name='user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='l_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
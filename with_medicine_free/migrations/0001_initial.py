# Generated by Django 4.2.1 on 2023-08-16 18:53

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
            name='Free_board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='data published')),
                ('body', models.TextField()),
                ('hits', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('like_users', models.ManyToManyField(blank=True, related_name='like_posts', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='l_posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Free_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_text', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('free_board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='with_medicine_free.free_board')),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='l_posts_comment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

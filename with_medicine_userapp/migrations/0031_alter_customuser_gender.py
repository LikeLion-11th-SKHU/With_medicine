# Generated by Django 4.2.1 on 2023-08-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('with_medicine_userapp', '0030_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('O', '기타(Other)'), ('M', '남성(Man)'), ('W', '여성(Woman)')], max_length=1, null=True, verbose_name='성별'),
        ),
    ]
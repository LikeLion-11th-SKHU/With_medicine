# Generated by Django 4.2.4 on 2023-08-14 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('with_medicine_userapp', '0023_alter_customuser_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', '남성(Man)'), ('W', '여성(Woman)'), ('O', '기타(Other)')], max_length=1, null=True, verbose_name='성별'),
        ),
    ]
# Generated by Django 4.0.4 on 2022-07-07 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_usercount'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercount',
            name='ip_address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
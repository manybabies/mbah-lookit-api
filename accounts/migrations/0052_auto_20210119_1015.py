# Generated by Django 3.0.7 on 2021-01-19 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0051_daily_announcement_email_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=255, verbose_name='Nickname'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-19 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_challenge_status_challenge_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='memo',
            field=models.TextField(null=True),
        ),
    ]
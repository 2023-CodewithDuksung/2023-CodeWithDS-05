# Generated by Django 4.2.4 on 2023-08-19 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_alter_challenge_memo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='memo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
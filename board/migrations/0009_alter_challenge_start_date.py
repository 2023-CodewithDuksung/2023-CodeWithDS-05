# Generated by Django 4.2.4 on 2023-08-19 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_alter_challenge_memo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

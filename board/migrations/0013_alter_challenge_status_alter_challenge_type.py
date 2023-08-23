# Generated by Django 4.2.4 on 2023-08-19 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_alter_challenge_status_alter_challenge_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='status',
            field=models.CharField(choices=[('0', '진행중'), ('1', '성공'), ('2', '실패')], default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='type',
            field=models.CharField(choices=[('0', '학업'), ('1', '자격증'), ('2', '대외활동'), ('3', '기타')], default=3, max_length=4),
        ),
    ]
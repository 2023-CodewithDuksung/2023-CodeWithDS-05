# Generated by Django 4.2.4 on 2023-08-19 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0010_alter_challenge_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='status',
            field=models.CharField(choices=[('진행중', '진행중'), ('성공', '성공'), ('실패', '실패')], default='진행중', max_length=3),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='type',
            field=models.CharField(choices=[('학업', '학업'), ('자격증', '자격증'), ('대외활동', '대외활동'), ('기타', '기타')], default='기타', max_length=4),
        ),
    ]

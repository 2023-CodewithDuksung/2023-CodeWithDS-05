# Generated by Django 4.2.4 on 2023-08-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0015_alter_user_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='status',
            field=models.CharField(choices=[('0', '진행중'), ('1', '성공'), ('2', '실패')], default=0, max_length=5),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='type',
            field=models.CharField(choices=[('0', '진행중'), ('1', '성공'), ('2', '실패')], default=3, max_length=5),
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]

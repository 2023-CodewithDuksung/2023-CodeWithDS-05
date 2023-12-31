# Generated by Django 4.2.4 on 2023-08-19 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0013_alter_challenge_status_alter_challenge_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='challenge',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.type'),
        ),
    ]

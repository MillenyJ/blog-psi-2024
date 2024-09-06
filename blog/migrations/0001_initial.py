# Generated by Django 5.1 on 2024-09-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=100)),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=150)),
                ('subtitulo', models.CharField(max_length=100)),
                ('conteudo', models.TextField(max_length=1200)),
            ],
        ),
    ]

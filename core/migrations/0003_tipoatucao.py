# Generated by Django 4.2.6 on 2023-10-18 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pais'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipoAtucao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
    ]

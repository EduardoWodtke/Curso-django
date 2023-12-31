# Generated by Django 4.2.6 on 2023-10-18 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_membros'),
    ]

    operations = [
        migrations.CreateModel(
            name='filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('ano', models.IntegerField()),
                ('sinops', models.TextField()),
                ('classificacao', models.IntegerField()),
                ('duracao', models.TimeField()),
                ('produtora', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.produtora')),
            ],
        ),
    ]

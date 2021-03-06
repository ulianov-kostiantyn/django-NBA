# Generated by Django 3.0.6 on 2020-06-11 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('city', models.CharField(max_length=255, unique=True)),
                ('arena', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('logo', models.ImageField(upload_to='media')),
                ('wins', models.IntegerField()),
                ('looses', models.IntegerField()),
                ('conference', models.CharField(blank=True, choices=[('WESTERN', 'Western'), ('EASTERN', 'Eastern')], max_length=30)),
            ],
            options={
                'ordering': ['-wins'],
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('surname', models.CharField(max_length=255, unique=True)),
                ('height', models.FloatField()),
                ('age', models.IntegerField()),
                ('photo', models.ImageField(default='', upload_to='media')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_related', to='general.Team')),
            ],
            options={
                'ordering': ['surname'],
            },
        ),
    ]

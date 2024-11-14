# Generated by Django 5.1.1 on 2024-11-14 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('origin', models.CharField(max_length=255)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('formation_year', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]

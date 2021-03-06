# Generated by Django 2.1.5 on 2019-01-05 16:42

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='catégorie')),
            ],
            options={
                'verbose_name': 'catégorie',
                'verbose_name_plural': 'catégories',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='nom')),
                ('address', models.CharField(max_length=255, verbose_name='adresse')),
                ('streetnumber', models.CharField(max_length=255, verbose_name=',uméro')),
                ('postcode', models.IntegerField(verbose_name='code postal')),
                ('city', models.CharField(max_length=255, verbose_name='commune')),
                ('phone', models.CharField(max_length=255)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='géométrie')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partners.Category')),
            ],
            options={
                'verbose_name': 'partenaire',
                'verbose_name_plural': 'partenaires',
            },
        ),
    ]

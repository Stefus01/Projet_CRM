# Generated by Django 3.2.13 on 2022-06-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('id_client', models.CharField(max_length=3, verbose_name='Id Client')),
                ('age', models.CharField(max_length=3)),
                ('email', models.EmailField(max_length=50, verbose_name='Email Address')),
                ('address', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=14, verbose_name='Contact Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nom du produit')),
                ('type', models.CharField(max_length=200, verbose_name='Type de produit')),
                ('quantity', models.CharField(max_length=4, verbose_name='Quantité')),
                ('price', models.CharField(max_length=7, verbose_name='Prix')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=300, verbose_name='Venue Address')),
                ('phone', models.CharField(max_length=14)),
            ],
        ),
    ]

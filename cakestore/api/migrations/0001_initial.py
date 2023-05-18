# Generated by Django 4.1.3 on 2023-01-05 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('weight', models.PositiveBigIntegerField()),
                ('shape', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=20)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('price', models.PositiveBigIntegerField()),
            ],
        ),
    ]

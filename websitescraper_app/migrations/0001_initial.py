# Generated by Django 4.2.4 on 2023-08-21 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500, null=True)),
                ('stringname', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]

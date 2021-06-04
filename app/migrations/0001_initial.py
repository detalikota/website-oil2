# Generated by Django 3.2.4 on 2021-06-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'services',
            },
        ),
    ]

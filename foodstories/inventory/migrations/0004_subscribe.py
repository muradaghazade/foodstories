# Generated by Django 3.1.2 on 2020-10-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20201012_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=400)),
            ],
            options={
                'verbose_name': 'Subscribe',
                'verbose_name_plural': 'Subscribes',
            },
        ),
    ]
# Generated by Django 3.0.7 on 2020-06-26 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='destini',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer', models.BooleanField()),
                ('img', models.ImageField(upload_to='bob')),
                ('city', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('price', models.CharField(max_length=200)),
            ],
        ),
    ]
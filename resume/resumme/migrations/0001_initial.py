# Generated by Django 3.2.6 on 2021-08-20 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='eg Jane', max_length=30)),
                ('last_name', models.CharField(help_text='eg Doe', max_length=30)),
                ('email', models.EmailField(help_text='eg yourname@gmail.com', max_length=30)),
                ('message', models.CharField(default='Hello', max_length=300)),
            ],
        ),
    ]
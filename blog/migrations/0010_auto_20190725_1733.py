# Generated by Django 2.2.1 on 2019-07-25 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190725_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]

# Generated by Django 2.2.1 on 2019-07-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190725_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', height_field=500, upload_to='post_pictures', width_field=500),
        ),
    ]

# Generated by Django 2.2.1 on 2019-07-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default/default.jpg', upload_to=''),
        ),
    ]
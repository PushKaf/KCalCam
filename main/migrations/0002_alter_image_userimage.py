# Generated by Django 3.2.4 on 2021-06-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='userImage',
            field=models.ImageField(default='l', upload_to=''),
            preserve_default=False,
        ),
    ]
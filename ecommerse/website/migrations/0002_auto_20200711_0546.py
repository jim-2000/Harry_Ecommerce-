# Generated by Django 3.0.7 on 2020-07-11 05:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_date',
            new_name='published_date',
        ),
        migrations.AddField(
            model_name='product',
            name='catagory',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='subcatagory',
            field=models.CharField(default='', max_length=70),
        ),
    ]

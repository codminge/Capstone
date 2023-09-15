# Generated by Django 4.2.1 on 2023-05-31 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False, verbose_name='번호')),
                ('image', models.ImageField(null=True, upload_to='', verbose_name='이미지')),
            ],
        ),
        migrations.AddField(
            model_name='result',
            name='image',
            field=models.ImageField(null=True, upload_to='result/', verbose_name='이미지'),
        ),
        migrations.AlterField(
            model_name='result',
            name='date_time',
            field=models.DateTimeField(verbose_name='날짜'),
        ),
    ]

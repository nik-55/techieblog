# Generated by Django 4.1 on 2022-09-05 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='blog_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

# Generated by Django 4.1 on 2022-09-05 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_myuser_blog_id_myuser_blog_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='blog_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.blog_id'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-25 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0004_alter_post_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

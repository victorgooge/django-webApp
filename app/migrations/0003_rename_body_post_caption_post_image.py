# Generated by Django 5.0 on 2024-01-22 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_author_post_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='caption',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='notes'),
        ),
    ]
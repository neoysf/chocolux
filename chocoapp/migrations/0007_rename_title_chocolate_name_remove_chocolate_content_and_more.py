# Generated by Django 5.1.7 on 2025-03-13 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chocoapp', '0006_useremail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chocolate',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='chocolate',
            name='content',
        ),
        migrations.RemoveField(
            model_name='chocolate',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='chocolate',
            name='post_image',
        ),
        migrations.RemoveField(
            model_name='chocolate',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='chocolate',
            name='image',
            field=models.ImageField(default=True, upload_to='images/'),
            preserve_default=False,
        ),
    ]

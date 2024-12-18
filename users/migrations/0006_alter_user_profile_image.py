# Generated by Django 5.1.2 on 2024-10-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_user_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_image",
            field=models.ImageField(
                blank=True,
                default="default_image.jpg",
                null=True,
                upload_to="profile_images",
            ),
        ),
    ]

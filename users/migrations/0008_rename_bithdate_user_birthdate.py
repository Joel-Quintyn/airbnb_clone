# Generated by Django 4.1 on 2022-08-24 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_user_login_method"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="bithdate",
            new_name="birthdate",
        ),
    ]
# Generated by Django 4.1 on 2022-08-12 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_user_login_method_alter_user_email_secret"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="login_method",
            field=models.CharField(
                choices=[("email", "Email"), ("google", "Github")],
                default="email",
                max_length=10,
            ),
        ),
    ]

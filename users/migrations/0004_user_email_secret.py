# Generated by Django 4.1 on 2022-08-06 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_email_confirmed_alter_user_currency_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="email_secret",
            field=models.CharField(blank=True, default="", max_length=120),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-19 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mychatapp", "0006_alter_friend_profile"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatmessage",
            name="creation_date",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="chatmessage",
            name="subject",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]

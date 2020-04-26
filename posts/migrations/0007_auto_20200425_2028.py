# Generated by Django 3.0.4 on 2020-04-25 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20200423_2022'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpost',
            name='published_at',
            field=models.DateTimeField(db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='published_at',
            field=models.DateTimeField(db_index=True, null=True),
        ),
    ]
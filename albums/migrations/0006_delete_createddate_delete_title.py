# Generated by Django 4.2.7 on 2023-11-13 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0005_remove_createddate_created_on_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CreatedDate',
        ),
        migrations.DeleteModel(
            name='Title',
        ),
    ]
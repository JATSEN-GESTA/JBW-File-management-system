# Generated by Django 4.0.2 on 2022-05-22 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JBW_File_Manage_System_APP', '0004_quotation_auth_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotation',
            name='auth_user',
        ),
    ]

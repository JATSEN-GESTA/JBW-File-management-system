# Generated by Django 4.0.2 on 2022-05-26 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JBW_File_Manage_System_APP', '0011_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='codex',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 4.1.2 on 2023-04-08 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0002_alter_contactus_is_read_by_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='massage',
            new_name='message',
        ),
    ]
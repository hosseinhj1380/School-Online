# Generated by Django 4.1 on 2023-06-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_module', '0008_alter_talentcategory_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='NumberofCorses',
            field=models.IntegerField(verbose_name='تعداد دوره '),
        ),
    ]

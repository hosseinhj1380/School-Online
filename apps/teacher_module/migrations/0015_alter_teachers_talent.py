# Generated by Django 4.1 on 2023-06-04 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_module', '0014_remove_talentcategory_parent_remove_teachers_talent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='talent',
            field=models.ManyToManyField(to='teacher_module.talentcategory', verbose_name='مهارت استاد '),
        ),
    ]
# Generated by Django 4.1 on 2023-05-07 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0007_remove_comments_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='title',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='article_module.articlecategory'),
        ),
    ]

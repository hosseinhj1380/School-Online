# Generated by Django 4.2.1 on 2023-05-10 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0011_article_comment_alter_comments_blog_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': ' کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='full_name',
            field=models.CharField(max_length=50, verbose_name='نام '),
        ),
        migrations.AlterField(
            model_name='comments',
            name='message',
            field=models.TextField(max_length=500, verbose_name='پیام '),
        ),
    ]
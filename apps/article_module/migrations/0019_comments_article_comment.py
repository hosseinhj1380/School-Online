# Generated by Django 4.1.2 on 2023-06-10 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0018_merge_20230610_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='نام ')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('message', models.TextField(max_length=500, verbose_name='پیام ')),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article_module.article', verbose_name='مقاله مربوطه  ')),
            ],
            options={
                'verbose_name': ' کامنت',
                'verbose_name_plural': 'کامنت ها',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article_module.comments', verbose_name='کامنت ها '),
        ),
    ]
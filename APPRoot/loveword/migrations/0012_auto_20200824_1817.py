# Generated by Django 2.2.1 on 2020-08-24 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loveword', '0011_auto_20200824_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic_author',
            name='uid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='author_comic', to='loveword.Comic', verbose_name='作品id'),
        ),
    ]

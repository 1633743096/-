# Generated by Django 2.2.1 on 2020-08-24 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loveword', '0009_comic_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic_author',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loveword.Comic', verbose_name='作品id'),
        ),
    ]

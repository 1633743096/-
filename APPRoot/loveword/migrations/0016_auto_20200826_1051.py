# Generated by Django 2.2.1 on 2020-08-26 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loveword', '0015_auto_20200826_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic_chapter',
            name='chapter_number',
            field=models.IntegerField(verbose_name='章节编号'),
        ),
    ]
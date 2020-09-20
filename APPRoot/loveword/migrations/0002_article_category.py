# Generated by Django 2.2.1 on 2020-07-12 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loveword', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='loveword.Category', verbose_name='分类'),
            preserve_default=False,
        ),
    ]
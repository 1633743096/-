# Generated by Django 2.2.1 on 2021-02-17 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loveword', '0021_quotation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quotation',
            name='content',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='语录内容'),
        ),
    ]
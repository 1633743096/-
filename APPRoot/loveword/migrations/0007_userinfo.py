# Generated by Django 2.2.1 on 2020-08-05 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loveword', '0006_auto_20200731_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('token', models.CharField(blank=True, max_length=64, null=True, verbose_name='token值')),
            ],
        ),
    ]
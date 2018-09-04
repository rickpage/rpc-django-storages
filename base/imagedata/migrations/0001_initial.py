# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to='imagedata')),
                ('caption', models.CharField(max_length=64, blank=True, null=True)),
                ('description', models.CharField(max_length=256, blank=True, null=True)),
            ],
        ),
    ]

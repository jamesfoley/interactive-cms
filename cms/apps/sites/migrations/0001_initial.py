# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Friendly name for the site', max_length=2048)),
                ('domain', models.CharField(help_text=b"Domain name for the site. Example: 'example.com'", max_length=2048)),
            ],
        ),
    ]

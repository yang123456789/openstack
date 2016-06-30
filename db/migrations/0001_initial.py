# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('auth_token', models.CharField(max_length=255)),
                ('register_time', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=255, db_index=True)),
                ('phone', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('again_password', models.CharField(max_length=255)),
                ('identify_code', models.CharField(max_length=255)),
            ],
        ),
    ]

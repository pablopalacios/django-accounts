# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email address')),
                ('is_staff', models.BooleanField(help_text='Designates whether the user can log into this admin site.', verbose_name='staff status', default=False)),
                ('is_active', models.BooleanField(help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('groups', models.ManyToManyField(related_name='user_set', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, verbose_name='groups', to='auth.Group', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(related_name='user_set', help_text='Specific permissions for this user.', blank=True, verbose_name='user permissions', to='auth.Permission', related_query_name='user')),
            ],
            options={
                'ordering': ['name', 'email'],
                'abstract': False,
            },
        ),
    ]

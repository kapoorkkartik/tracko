# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(max_length=3000)),
                ('creator', models.ForeignKey(related_name='comments', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('application_no', models.CharField(unique=True, max_length=50)),
                ('birth_date', models.DateField()),
                ('license_no', models.CharField(max_length=50)),
                ('applicant_name', models.CharField(max_length=100)),
                ('issue_description', models.TextField(null=True, blank=True)),
                ('office', models.CharField(max_length=50, choices=[(b'SAM', b'Samba'), (b'KAT', b'Kathua'), (b'REA', b'Reasi'), (b'JAM', b'Jammu'), (b'UDH', b'Udhampur')])),
                ('closed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('project', models.CharField(max_length=100, choices=[(b'SAR', b'Sarathi'), (b'VAH', b'Vahan'), (b'OTH', b'Other')])),
                ('creator', models.ForeignKey(related_name='create_issues', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('owner', models.ForeignKey(related_name='created', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=100)),
                ('creator', models.ForeignKey(related_name='tags', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='tags',
            field=models.ManyToManyField(related_name='issues', to='issuetrack.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='issue',
            field=models.ForeignKey(related_name='comments', blank=True, to='issuetrack.Issue', null=True),
        ),
    ]

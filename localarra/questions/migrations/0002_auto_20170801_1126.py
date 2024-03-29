# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloseReasonTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=40, null=True)),
                ('Description', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AcceptedAnswerId', models.IntegerField()),
                ('ParentId', models.IntegerField(blank=True, null=True)),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('DeletionDate', models.DateTimeField()),
                ('Score', models.IntegerField(default='0')),
                ('ViewCount', models.IntegerField(default='0')),
                ('Body', models.TextField()),
                ('OwnerUserId', models.IntegerField()),
                ('OwnerDisplayName', models.CharField(max_length=40)),
                ('LastEditorUserId', models.IntegerField(blank=True, null=True)),
                ('LastEditorDisplayName', models.CharField(blank=True, max_length=40, null=True)),
                ('LastEditDate', models.DateTimeField(blank=True, null=True)),
                ('LastActivityDate', models.DateTimeField(auto_now_add=True)),
                ('Title', models.CharField(max_length=140)),
                ('Tags', models.CharField(max_length=250)),
                ('AnswerCount', models.IntegerField(default='0')),
                ('CommentCount', models.IntegerField(default='0')),
                ('FavoriteCount', models.IntegerField(default='0')),
                ('ClosedDate', models.DateTimeField()),
                ('CommunityOwnedDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PostTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PostId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Posts')),
            ],
        ),
        migrations.CreateModel(
            name='PostTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TagName', models.CharField(max_length=250)),
                ('Count', models.IntegerField()),
                ('WikiPostId', models.IntegerField()),
                ('ExcerptPostId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Posts')),
            ],
        ),
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserId', models.IntegerField()),
                ('CreationDate', models.DateTimeField(auto_now_add=True)),
                ('BountyAmount', models.IntegerField()),
                ('PostId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Posts')),
            ],
        ),
        migrations.CreateModel(
            name='VoteTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='reporter',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
        migrations.AddField(
            model_name='votes',
            name='VoteTypeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.VoteTypes'),
        ),
        migrations.AddField(
            model_name='posttags',
            name='TagId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Tags'),
        ),
        migrations.AddField(
            model_name='posts',
            name='PostTypeId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.PostTypes'),
        ),
    ]

# Generated by Django 2.2 on 2024-04-21 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0006_auto_20240417_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('follower', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserFollowing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('following', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='userpost',
            name='post_dislikes',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='post_likes',
            field=models.IntegerField(default='0'),
        ),
    ]
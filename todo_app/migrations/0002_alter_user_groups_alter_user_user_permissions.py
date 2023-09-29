# Generated by Django 4.2.5 on 2023-09-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='custom_user_set', related_query_name='user', to='auth.group', verbose_name=('groups',)),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='custom_user_set', related_query_name='user', to='auth.permission', verbose_name=('user permissions',)),
        ),
    ]

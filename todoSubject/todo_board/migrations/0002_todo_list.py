# Generated by Django 2.1.2 on 2019-05-15 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo_list',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('pcode', models.CharField(max_length=4)),
                ('user_id', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000)),
                ('is_complete', models.BooleanField()),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'todo_list',
                'managed': False,
            },
        ),
    ]
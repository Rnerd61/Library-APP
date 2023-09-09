# Generated by Django 4.2.5 on 2023-09-09 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0003_delete_usermodel2'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('role', models.CharField(choices=[('User', 'User'), ('Admin', 'Admin')], default='User', max_length=20)),
            ],
            options={
                'db_table': 'user2',
            },
        ),
    ]

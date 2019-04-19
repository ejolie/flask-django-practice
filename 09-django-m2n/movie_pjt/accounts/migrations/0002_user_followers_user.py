# Generated by Django 2.2 on 2019-04-19 04:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Followers_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ManyToManyField(related_name='to_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

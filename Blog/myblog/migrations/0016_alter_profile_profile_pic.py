# Generated by Django 4.2.1 on 2023-05-31 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0015_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='Blog/images/user.png', null=True, upload_to='images/profile/'),
        ),
    ]

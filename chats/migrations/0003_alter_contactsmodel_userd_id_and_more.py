# Generated by Django 5.2.4 on 2025-07-16 03:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_alter_contactsmodel_userd_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactsmodel',
            name='userd_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts_as_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contactsmodel',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts_recived', to=settings.AUTH_USER_MODEL),
        ),
    ]

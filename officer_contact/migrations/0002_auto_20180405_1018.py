# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('officer_contact', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='officercontact',
            name='OfficerContact_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='officer_contact', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='officer_contact_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='officer_contact.OfficerContact'),
        ),
    ]
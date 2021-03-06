# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('video', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SpecialArt', '0002_auto_20180405_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialart',
            name='SpecialArt_Video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.video'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_SpecialArt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsSpecialArt', to='SpecialArt.SpecialArt'),
        ),
        migrations.AddField(
            model_name='comment',
            name='SpecialArt_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentssSpecialArt', to=settings.AUTH_USER_MODEL),
        ),
    ]

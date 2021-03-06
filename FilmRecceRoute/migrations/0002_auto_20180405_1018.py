# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('FilmRecceRoute', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmrecceroute',
            name='FilmRecceRoute_Creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FilmRecceRoutes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='filmrecceroute',
            name='FilmRecceRoute_Film_Location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FilmRecceRoute', to='Location.Location'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_FilmRecceRoute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsFilmRecceRoute', to='FilmRecceRoute.FilmRecceRoute'),
        ),
        migrations.AddField(
            model_name='comment',
            name='FilmRecceRoute_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CommentssFilmRecceRoute', to=settings.AUTH_USER_MODEL),
        ),
    ]

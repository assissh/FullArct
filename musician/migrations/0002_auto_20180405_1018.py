# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ratings', '0002_auto_20180405_1018'),
        ('musician', '0001_initial'),
        ('video', '0001_initial'),
        ('Comments', '0002_auto_20180405_1018'),
        ('portfolio_element', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ProfileProjects', '0002_auto_20180405_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='Musician_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musician', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='musician',
            name='Musician_Comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Musician', to='Comments.Comments'),
        ),
        migrations.AddField(
            model_name='musician',
            name='Musician_Description_Portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_element.PortfolioElement'),
        ),
        migrations.AddField(
            model_name='musician',
            name='Musician_Description_Profile_Projects',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProfileProjects.ProfileProjects'),
        ),
        migrations.AddField(
            model_name='musician',
            name='Musician_Description_Ratings',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ratings.Rating'),
        ),
        migrations.AddField(
            model_name='musician',
            name='Musician_Description_Video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.video'),
        ),
        migrations.AddField(
            model_name='comment',
            name='musician_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.Musician'),
        ),
    ]

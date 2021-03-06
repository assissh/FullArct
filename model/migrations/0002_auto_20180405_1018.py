# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('model', '0001_initial'),
        ('Ratings', '0002_auto_20180405_1018'),
        ('video', '0001_initial'),
        ('Comments', '0002_auto_20180405_1018'),
        ('portfolio_element', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='models',
            name='Models_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='models',
            name='Models_Comments',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Models', to='Comments.Comments'),
        ),
        migrations.AddField(
            model_name='models',
            name='Models_Portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Models', to='portfolio_element.PortfolioElement'),
        ),
        migrations.AddField(
            model_name='models',
            name='Models_Rating',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Models', to='Ratings.Rating'),
        ),
        migrations.AddField(
            model_name='models',
            name='Models_Video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Models', to='video.video'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Model_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='model.Models'),
        ),
    ]

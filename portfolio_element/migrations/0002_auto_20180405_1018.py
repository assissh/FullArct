# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Search', '0002_auto_20180405_1018'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio_element', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioelement',
            name='PortfolioElement_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='portfolio_element', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='portfolioelement',
            name='PortfolioElement_Material_Tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PortfolioElement', to='Search.Search'),
        ),
        migrations.AddField(
            model_name='comment',
            name='portfolio_element_Comment_Author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_element.PortfolioElement'),
        ),
    ]

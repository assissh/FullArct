# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('help_category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('help_subcategory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='help_category',
            name='Help_Category_Creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='helpcategorys', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='help_category',
            name='Help_subcatagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='helpsubcategorys', to='help_subcategory.HelpSubCategory'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Help_Category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help_category.Help_Category'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Help_Category_Comment_Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='help_category_Comment_Author', to=settings.AUTH_USER_MODEL),
        ),
    ]

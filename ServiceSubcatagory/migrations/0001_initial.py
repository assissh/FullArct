# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceSubcatagory_Comment', models.CharField(max_length=150)),
                ('ServiceSubcatagory_Comment_Created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceSubcatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_Subcatagory_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_ServiceSubcatagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentsServiceSubcatagory', to='ServiceSubcatagory.ServiceSubcatagory'),
        ),
    ]

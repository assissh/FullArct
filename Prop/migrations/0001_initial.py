# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prop_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Prop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prop_Color', models.CharField(max_length=200)),
                ('Prop_Daily_Rent', models.IntegerField()),
                ('Prop_Making_Year', models.DateField(auto_now_add=True)),
                ('Prop_Modification_Allowed', models.BooleanField(max_length=200)),
                ('Prop_Ownership_Status', models.BooleanField()),
                ('Prop_ID', models.IntegerField()),
                ('Prop_Make', models.CharField(max_length=200)),
                ('Prop_Type', models.CharField(max_length=200)),
                ('Prop_Weekly_Rent', models.IntegerField()),
                ('Prop_Modified_Date', models.DateField(auto_now_add=True)),
                ('Prop_Created_Date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
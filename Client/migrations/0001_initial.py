# Generated by Django 2.0.3 on 2018-04-05 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client_Contact_Person', models.CharField(max_length=100, unique=True)),
                ('Client_Contact_Person_Designation', models.CharField(max_length=100)),
                ('Client_Contact_Person_Email', models.CharField(max_length=100)),
                ('Client_Contact_Person_Number', models.CharField(max_length=100)),
                ('Client_Previous_work', models.CharField(max_length=100)),
                ('Client_Production_House_City_Address', models.CharField(max_length=100)),
                ('Client_Production_House_Name', models.CharField(max_length=100)),
                ('Client_Production_House_Street_Addrerss', models.CharField(max_length=100)),
                ('Client_Modified_Date', models.DateTimeField(auto_now_add=True)),
                ('Client_Created_Date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client_Comment', models.CharField(max_length=150)),
            ],
        ),
    ]
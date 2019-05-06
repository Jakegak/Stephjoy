# Generated by Django 2.1.4 on 2019-05-06 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20190504_0725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_number', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=10)),
                ('second_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('classes', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=13)),
                ('fingerPrint', models.CharField(max_length=4)),
                ('photo', models.ImageField(upload_to='media')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
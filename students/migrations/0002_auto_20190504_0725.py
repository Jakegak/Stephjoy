# Generated by Django 2.1.4 on 2019-05-04 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
            name='Students',
        ),
    ]

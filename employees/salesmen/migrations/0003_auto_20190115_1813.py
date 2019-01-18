# Generated by Django 2.1.3 on 2019-01-15 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesmen', '0002_auto_20181221_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='responsibility',
            name='date_accomplished',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishyou', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='images',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='your_contact',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='your_email',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='your_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='email',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
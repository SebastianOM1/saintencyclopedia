# Generated by Django 3.2.9 on 2021-11-24 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saint',
            name='birthDay',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='saint',
            name='birthDelimiter',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='saint',
            name='birthMonth',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='saint',
            name='birthPlace',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='saint',
            name='birthYear',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='saint',
            name='deathDay',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='saint',
            name='deathDelimiter',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='saint',
            name='deathMonth',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='saint',
            name='deathPlace',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='saint',
            name='deathYear',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='saint',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]

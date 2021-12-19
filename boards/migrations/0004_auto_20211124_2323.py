# Generated by Django 3.2.9 on 2021-11-25 07:23

from django.db import migrations, models
import partial_date.fields


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_auto_20211124_1435'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saint',
            old_name='birthPlace',
            new_name='birthCountry',
        ),
        migrations.RenameField(
            model_name='saint',
            old_name='birthDelimiter',
            new_name='birthDateType',
        ),
        migrations.RenameField(
            model_name='saint',
            old_name='deathPlace',
            new_name='deathCountry',
        ),
        migrations.RenameField(
            model_name='saint',
            old_name='deathDelimiter',
            new_name='deathDateType',
        ),
        migrations.RemoveField(
            model_name='saint',
            name='birthDay',
        ),
        migrations.RemoveField(
            model_name='saint',
            name='birthMonth',
        ),
        migrations.RemoveField(
            model_name='saint',
            name='birthYear',
        ),
        migrations.RemoveField(
            model_name='saint',
            name='deathDay',
        ),
        migrations.RemoveField(
            model_name='saint',
            name='deathMonth',
        ),
        migrations.RemoveField(
            model_name='saint',
            name='deathYear',
        ),
        migrations.AddField(
            model_name='saint',
            name='birthCity',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='saint',
            name='birthDate',
            field=partial_date.fields.PartialDateField(null=True),
        ),
        migrations.AddField(
            model_name='saint',
            name='deathCity',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='saint',
            name='deathDate',
            field=partial_date.fields.PartialDateField(null=True),
        ),
    ]

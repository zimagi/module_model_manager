# Generated by Django 3.1 on 2021-05-19 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyperparameter', '0001_initial'),
        ('model_config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelconfig',
            name='hyperparameters',
            field=models.ManyToManyField(related_name='modelconfig_relations', to='hyperparameter.HyperParameter'),
        ),
    ]

# Generated by Django 3.1 on 2021-05-19 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('model', '0001_initial'),
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelConfig',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=256)),
                ('library', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modelconfig_relation', to='library.library')),
                ('model', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modelconfig_relation', to='model.model')),
            ],
            options={
                'verbose_name': 'model config',
                'verbose_name_plural': 'model configs',
                'db_table': 'model_manager_model_config',
                'ordering': ['name'],
                'abstract': False,
                'unique_together': {('model', 'name')},
            },
        ),
    ]

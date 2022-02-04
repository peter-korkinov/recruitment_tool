# Generated by Django 4.0 on 2022-01-21 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiters', '0001_initial'),
        ('candidates', '0003_alter_candidatemodel_recruiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatemodel',
            name='recruiter',
            field=models.ForeignKey(default=6, on_delete=django.db.models.deletion.CASCADE, to='recruiters.recruitermodel'),
        ),
    ]

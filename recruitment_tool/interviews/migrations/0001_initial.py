# Generated by Django 4.0 on 2021-12-20 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidates', '0003_alter_candidatemodel_recruiter'),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidatemodel')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobmodel')),
            ],
        ),
    ]
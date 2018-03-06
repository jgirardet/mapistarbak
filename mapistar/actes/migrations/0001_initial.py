# Generated by Django 2.0.2 on 2018-02-21 21:18

# Third Party Libraries
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0002_patient_birthdate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('motif', models.CharField(max_length=40)),
                ('body', models.TextField(blank=True)),
                ('owner',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.PROTECT,
                     related_name='observations',
                     to=settings.AUTH_USER_MODEL)),
                ('patient',
                 models.ForeignKey(
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='observations',
                     to='patients.Patient')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
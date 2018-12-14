# Generated by Django 2.1.1 on 2018-12-14 10:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(choices=[('0', 'Station0'), ('1', 'Station1'), ('2', 'Station2'), ('3', 'Station3'), ('4', 'Station4')], default=None, max_length=100)),
                ('status', models.CharField(choices=[(1, 'PASS'), (2, 'FAIL')], max_length=4)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('serial_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Board.Board')),
            ],
        ),
    ]

# Generated by Django 3.2.5 on 2021-09-24 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover', models.ImageField(upload_to='event_cover/')),
                ('detail', models.TextField(max_length=1000)),
                ('place', models.CharField(max_length=1000)),
                ('total', models.IntegerField()),
                ('gained', models.IntegerField(blank=True, default=0)),
                ('deadline', models.DateTimeField(null=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now_add=True)),
                ('ready_to_distribute', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('method', models.CharField(choices=[('bkash', 'Bkash'), ('roket', 'Roket'), ('nagad', 'Nagad')], default='Bkash', max_length=50)),
                ('mobile_no', models.IntegerField()),
                ('transid', models.CharField(max_length=50)),
                ('date_donated', models.DateField(auto_now_add=True)),
                ('isapproved', models.CharField(choices=[('no', 'No'), ('yes', 'Yes')], default='no', max_length=25)),
                ('doner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='AssetDistribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('Item', models.TextField(blank=True, max_length=600)),
                ('donate_date', models.DateField(auto_now_add=True)),
                ('event', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('person', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='events.person')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 5.0.2 on 2024-04-22 20:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semester_id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('starting_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('semester_tuition', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expected_end_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('student_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('income_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_recurring', models.BooleanField()),
                ('date_last_updated', models.DateField(auto_now=True)),
                ('recurring_period', models.CharField(max_length=20)),
                ('memo', models.CharField(max_length=200, null=True)),
                ('semester_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='budget.semester')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('income_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_recurring', models.BooleanField()),
                ('date_last_updated', models.DateField(auto_now=True)),
                ('recurring_period', models.CharField(max_length=20)),
                ('memo', models.CharField(max_length=200, null=True)),
                ('semester_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='budget.semester')),
            ],
        ),
    ]

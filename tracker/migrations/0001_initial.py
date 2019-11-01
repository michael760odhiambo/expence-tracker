# Generated by Django 2.2.6 on 2019-10-31 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=1000, null=True)),
                ('type', models.CharField(max_length=30)),
                ('payment', models.CharField(max_length=30)),
                ('amount', models.FloatField()),
                ('created_by', models.CharField(max_length=100)),
                ('created_at', models.DateField()),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
                'ordering': ['-id'],
            },
        ),
    ]

# Generated by Django 5.1.5 on 2025-01-16 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('head', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='projects/')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('ongoing', 'Ongoing'), ('completed', 'Completed'), ('upcoming', 'Upcoming')], default='upcoming', max_length=10)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['-start_date'],
            },
        ),
        migrations.AddField(
            model_name='deposit',
            name='deposit_for',
            field=models.CharField(choices=[('TITHE', 'Tithe'), ('THANKSGIVING', 'Thanksgiving'), ('WEDDING', 'Wedding'), ('OFFERTORY', 'Offertory'), ('FIRST FRUIT', 'First Fruit'), ('CHURCH PROJECT', 'Church Project'), ('OTHERS', 'Others')], default='OFFERTORY', max_length=200),
        ),
    ]

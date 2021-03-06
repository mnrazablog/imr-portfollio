# Generated by Django 3.0.1 on 2019-12-27 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20191227_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='devtools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='framework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('short_desc', models.CharField(max_length=100)),
                ('avatar', models.ImageField(upload_to='avatar/')),
                ('title_of_detail', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('skills_image', models.ImageField(upload_to='skills/')),
                ('skills_desc', models.CharField(max_length=300)),
                ('devtools', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.devtools')),
                ('framework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.framework')),
                ('languages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.languages')),
            ],
        ),
    ]

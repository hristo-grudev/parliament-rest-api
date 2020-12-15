# Generated by Django 3.1.2 on 2020-12-14 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('date', models.IntegerField()),
                ('email', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('town', models.TextField(max_length=50)),
                ('country', models.TextField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionsToNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parliament_api.names')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parliament_api.professions')),
            ],
        ),
        migrations.CreateModel(
            name='PartiesToNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parliament_api.names')),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parliament_api.parties')),
            ],
        ),
        migrations.AddField(
            model_name='names',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parliament_api.places'),
        ),
        migrations.CreateModel(
            name='LanguagesToNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parliament_api.languages')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='parliament_api.names')),
            ],
        ),
    ]
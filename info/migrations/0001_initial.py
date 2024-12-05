# Generated by Django 3.1.12 on 2024-12-05 16:55

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoModel',
            fields=[
                ('owner', models.IntegerField()),
                ('rollnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('extra_data', jsonfield.fields.JSONField()),
            ],
        ),
    ]
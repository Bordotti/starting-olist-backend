# Generated by Django 3.1.7 on 2021-03-22 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField()),
                ('initial_call', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='initial_call_bill', to='records.callrecord')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_bill', to='records.callrecord')),
            ],
            options={
                'unique_together': {('source', 'initial_call')},
            },
        ),
    ]

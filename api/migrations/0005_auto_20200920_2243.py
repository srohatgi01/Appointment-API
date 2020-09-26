# Generated by Django 3.1.1 on 2020-09-20 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200825_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_gender', to='api.gender'),
        ),
    ]
# Generated by Django 3.1.1 on 2020-09-24 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20200924_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='api.categories'),
        ),
    ]
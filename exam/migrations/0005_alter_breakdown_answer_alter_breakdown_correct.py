# Generated by Django 5.0.1 on 2024-02-27 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_exam_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakdown',
            name='answer',
            field=models.CharField(default='-', max_length=5),
        ),
        migrations.AlterField(
            model_name='breakdown',
            name='correct',
            field=models.CharField(default='-', max_length=5),
        ),
    ]

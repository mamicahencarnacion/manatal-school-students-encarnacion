# Generated by Django 4.0.1 on 2022-02-09 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school_students_info", "0011_school_students_counter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="school",
            name="students_counter",
            field=models.PositiveBigIntegerField(editable=False),
        ),
    ]
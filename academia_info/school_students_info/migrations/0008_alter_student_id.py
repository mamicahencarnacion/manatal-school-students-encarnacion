# Generated by Django 4.0.1 on 2022-02-09 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school_students_info", "0007_alter_student_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.0.1 on 2022-02-09 02:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("school_students_info", "0002_alter_student_student_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="student_id",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]

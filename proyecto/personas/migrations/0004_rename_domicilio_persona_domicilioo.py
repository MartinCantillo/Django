# Generated by Django 5.0 on 2024-01-06 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0003_domicilio_persona_domicilio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='domicilio',
            new_name='domicilioo',
        ),
    ]

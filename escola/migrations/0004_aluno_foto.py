# Generated by Django 3.1 on 2023-07-01 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_auto_20230630_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, default='', upload_to='foto-aluno'),
        ),
    ]

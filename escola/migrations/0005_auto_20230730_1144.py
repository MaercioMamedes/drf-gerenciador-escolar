# Generated by Django 3.1 on 2023-07-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0004_aluno_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(blank=True, default='', null=True, upload_to='foto-aluno'),
        ),
    ]

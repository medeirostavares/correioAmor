# Generated by Django 2.1.1 on 2018-09-14 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0003_auto_20180911_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='recado',
            name='comentario_pendente',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', max_length=1, verbose_name='Comentários'),
        ),
    ]

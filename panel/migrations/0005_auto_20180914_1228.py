# Generated by Django 2.1.1 on 2018-09-14 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_recado_comentario_pendente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recado',
            name='comentario_pendente',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], default='N', editable=False, max_length=1, verbose_name='Comentário'),
        ),
    ]

# Generated by Django 2.1.1 on 2018-09-12 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentariosinline',
            name='cod_recado',
        ),
        migrations.RemoveField(
            model_name='recado',
            name='cod_recado',
        ),
        migrations.AddField(
            model_name='recado',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]

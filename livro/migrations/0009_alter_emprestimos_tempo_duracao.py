# Generated by Django 4.0.6 on 2022-08-06 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0008_alter_emprestimos_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='tempo_duracao',
            field=models.TimeField(blank=True, null=True),
        ),
    ]

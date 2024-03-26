# Generated by Django 5.0.3 on 2024-03-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_autor_site_autor_cidade_editora_cidade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimo',
            name='datadevolucao',
            field=models.DateField(max_length=8),
        ),
        migrations.AlterField(
            model_name='emprestimo',
            name='dataemprestimo',
            field=models.DateField(max_length=8),
        ),
        migrations.AlterField(
            model_name='livro',
            name='datapublicao',
            field=models.DateField(max_length=8),
        ),
        migrations.AlterField(
            model_name='livro',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
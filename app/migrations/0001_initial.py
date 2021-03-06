# Generated by Django 3.2.7 on 2021-09-26 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cnpj', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=2048)),
                ('cep', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=1000)),
                ('qtde_estoque', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=9)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categorias')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.empresas')),
            ],
        ),
    ]

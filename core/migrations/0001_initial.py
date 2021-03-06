# Generated by Django 3.2.3 on 2021-06-17 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('patente', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Patente')),
                ('marca', models.CharField(max_length=20, verbose_name='Marca vehiculo')),
                ('modelo', models.CharField(blank=True, max_length=20, null=True, verbose_name='Modelo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]

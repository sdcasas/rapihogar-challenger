# Generated by Django 4.2.10 on 2024-02-14 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Técnico',
                'ordering': ('apellido', 'nombre'),
            },
        ),
        migrations.AddField(
            model_name='pedido',
            name='tecnico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='core.tecnico'),
            preserve_default=False,
        ),
    ]
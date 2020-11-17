# Generated by Django 2.2.8 on 2020-11-17 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_auto_20201031_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='ciudad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='autor_ciudad', to='table.Ciudad', verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='perfil',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.Perfil', verbose_name='Autores'),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='distribuidor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Editoriales', to='table.Distribuidor'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='editorial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='perfiles', to='table.Editorial'),
        ),
    ]
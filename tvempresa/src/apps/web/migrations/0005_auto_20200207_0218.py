# Generated by Django 2.2.4 on 2020-02-07 07:18

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200127_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='capitulos',
            name='logo_titulo',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='logos_titulos/', verbose_name='Logo Titulo'),
        ),
        migrations.AlterField(
            model_name='capitulos',
            name='titulo',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Titulo'),
        ),
        migrations.AlterField(
            model_name='principal',
            name='nombre_video_principal',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre Video Principal'),
        ),
    ]
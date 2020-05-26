# Generated by Django 3.0.6 on 2020-05-26 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20200526_1117'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=None, verbose_name='Data'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='height',
            field=models.FloatField(verbose_name='Altura'),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='weight',
            field=models.FloatField(verbose_name='Volume'),
        ),
        migrations.AlterField(
            model_name='merchandise',
            name='width',
            field=models.FloatField(verbose_name='Largura'),
        ),
        migrations.AlterField(
            model_name='order',
            name='destiny',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_destiny', to='register.Address', verbose_name='Destino'),
        ),
        migrations.AlterField(
            model_name='order',
            name='merchandises',
            field=models.ManyToManyField(to='order.Merchandise', verbose_name='Mercadoria'),
        ),
        migrations.AlterField(
            model_name='order',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_origin', to='register.Address', verbose_name='Origem'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.User', verbose_name='Cliente'),
        ),
    ]

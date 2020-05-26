# Generated by Django 3.0.6 on 2020-05-26 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchandise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField()),
                ('width', models.FloatField()),
                ('weight', models.FloatField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destiny', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_destiny', to='register.Address')),
                ('merchandises', models.ManyToManyField(to='order.Merchandise')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order_origin', to='register.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.User')),
            ],
        ),
    ]

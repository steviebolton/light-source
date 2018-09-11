# Generated by Django 2.0.6 on 2018-09-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bulb',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='cri',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='energy_label',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='kelvin',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='lumens',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='fitting',
            field=models.CharField(blank=True, choices=[('fitting', 'fitting'), ('E27', 'E27'), ('E16', '16'), ('GU10', 'GU10'), ('LED built in', 'LED built in')], default='X', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(blank=True, choices=[('choose material', 'choose material'), ('metal sprayed copper', 'metal sprayed copper'), ('metal sprayed silver', 'metal sprayed silver'), ('metal', 'metal'), ('aluminium', 'aluminium'), ('copper', 'copper'), ('vineer', 'vineer'), ('fibreglass', 'fibreglass')], default='X', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(choices=[('choose type', 'choose type'), ('suspension', 'suspension'), ('floor', 'floor'), ('table', 'table'), ('wall-ceiling', 'wall-ceiling'), ('recessed', 'recessed'), ('outside', 'outside')], default='X', max_length=15),
        ),
    ]

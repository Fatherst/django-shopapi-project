# Generated by Django 4.2.6 on 2023-10-10 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_alter_product_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopapp.comment'),
        ),
    ]

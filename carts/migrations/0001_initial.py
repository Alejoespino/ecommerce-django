# Generated by Django 4.2.3 on 2024-01-10 19:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0002_rename_product_name_product_product_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.CharField(blank=True, max_length=250)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('Cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carts.cart')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
# Generated by Django 4.1.7 on 2023-02-25 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_property_rentedtable_reviews_user_delete_order_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='shop_user',
        ),
    ]

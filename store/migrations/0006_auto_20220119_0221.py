# Generated by Django 4.0.1 on 2022-01-19 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_customer_store_custo_last_na_e6a359_idx_and_more'),
    ]

    operations = [
        migrations.RunSQL("""
        INSERT INTO store_colletion (title)
        VALUES ('collection1')
        ""","""
        DELETE FROM store_collection
        WHERE title='collection1'
        """)
    ]

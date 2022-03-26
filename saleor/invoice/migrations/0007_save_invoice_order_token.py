# Generated by Django 3.2.12 on 2022-02-24 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0127_add_order_number_and_alter_order_token"),
        ("invoice", "0006_invoiceevent_app"),
    ]

    operations = [
        migrations.AddField(
            model_name="invoice",
            name="order_token",
            field=models.UUIDField(null=True),
        ),
        migrations.RunSQL(
            """
            UPDATE invoice_invoice
            SET order_token = (
                SELECT token
                FROM order_order
                WHERE invoice_invoice.order_id = order_order.id
            )
            WHERE order_id IS NOT NULL;
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.AddField(
            model_name="invoiceevent",
            name="order_token",
            field=models.UUIDField(null=True),
        ),
        migrations.RunSQL(
            """
            UPDATE invoice_invoiceevent
            SET order_token = (
                SELECT token
                FROM order_order
                WHERE invoice_invoiceevent.order_id = order_order.id
            )
            WHERE order_id IS NOT NULL;
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.AlterField(
            model_name="invoice",
            name="order",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="invoices",
                to="order.order",
                to_field="number",
            ),
        ),
        migrations.AlterField(
            model_name="invoiceevent",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="invoice_events",
                to="order.order",
                to_field="number",
            ),
        ),
    ]

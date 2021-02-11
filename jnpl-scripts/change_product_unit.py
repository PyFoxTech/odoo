#!/usr/bin/env python
from __future__ import print_function

from typing import List

import click
import click_odoo

from addons.product.models.product import ProductProduct
from addons.product.models.product_attribute import \
    ProductTemplateAttributeValue
from addons.product.models.product_template import ProductTemplate


@click.command()
@click_odoo.env_options(default_log_level='error')
def main(env):
    raise Exception('Running this script is dangerous')

    changes = [
        {
            'old_uom_name': 'Units',
            'new_uom_name': 'kg',
            'product_ids': [
                2100,
                1614,
                2101,
                2128,
                2117,
                2140,
                2142,
                1843,
                1553,
                2198,
                2202,
                2136,
                2175,
                2184,
                1847,
                2188,
                1736,
            ],
        },
        {
            'old_uom_name': 'units',
            'new_uom_name': 'liter',
            'product_ids': [1678],
        },
        {
            'old_uom_name': 'liter',
            'new_uom_name': 'kg',
            'product_ids': [
                1629,
                1631,
                1639,
                1634,
                1637,
                1652,
                1647,
                1649,
                1635,
                1642,
                1640,
                1646,
                1644,
                1654,
            ],
        },
        # {
        #     'old_uom_name': 'Units',
        #     'new_uom_name': 'kg',
        #     'product_ids': [],
        # },
    ]

    for change in changes:
        all_products: List[ProductProduct] = env['product.product'].browse(
            change['product_ids'])

        old_uom = env['uom.uom'].search([
            ['name', 'ilike', '%%' + change['old_uom_name'] + '%%'],
        ])[0]
        new_uom = env['uom.uom'].search([
            ['name', 'ilike', '%%' + change['new_uom_name'] + '%%'],
        ])[0]

        print(f'new_uom.id {new_uom.id}')

        # all_products: List[ProductProduct] = env['product.product'].search([
        #     ['name', 'ilike', '%%BULK%%'],
        #     ['uom_id', '=', old_uom.id],
        # ])

        for product in all_products:

            product_template: ProductTemplate = product.product_tmpl_id
            print(product.uom_id)
            print(product.id, "=", product_template.name)
            # product_template.type = 'product'
            # env.cr.commit()

            # print(product.stock_move_ids)
            for stock_move in product.stock_move_ids:
                stock_move.state = 'draft'
                env.cr.commit()
                stock_move.unlink()
                env.cr.commit()

            # product_template.uom_po_id = new_uom
            # product_template.uom_id = new_uom
            # product.update({'uom_po_id': new_uom.id, 'uom_id':new_uom.id})
            product_template.write(
                {'uom_po_id': new_uom.id, 'uom_id': new_uom.id})
            env.cr.commit()


if __name__ == '__main__':
    main()  # noqa

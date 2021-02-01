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

    all_products: List[ProductProduct] = env['product.product'].search([
        # ['name', 'ilike', '%%Ghee%%']
    ])

    for product in all_products:
        product_template: ProductTemplate = product.product_tmpl_id
        print(product_template.name, product_template.type)
        product_template.type = 'product'
        env.cr.commit()

if __name__ == '__main__':
    main()  # noqa

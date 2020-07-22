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

    # all_products: List[ProductProduct] = env['product.product'].search([
    #     # ['name', 'ilike', '%%Laung%%']

    # ])

    # all_gst_taxes = env['account.tax'].search([
    #     ['name', 'ilike', '%%GST%%']
    # ])

    # for gst_tax in all_gst_taxes:
    #     gst_tax.price_include = False
    #     env.cr.commit()

    # for product in all_products:
    #     product_template: ProductTemplate = product.product_tmpl_id

    #     product_template_attribute_values: List[ProductTemplateAttributeValue] = product.product_template_attribute_value_ids.search([
    #         ['product_tmpl_id', '=', product_template.id]
    #     ])

    #     account_tax = env['account.tax'].browse(
    #         product_template.taxes_id.ids)[0]

    #     new_list_price = round(account_tax.compute_all(
    #         product_template.list_price)['total_included'])
    #     product_template.list_price = new_list_price
    #     env.cr.commit()

    #     if product_template_attribute_values:
    #         for ptav in product_template_attribute_values:
    #             new_price_extra = round(account_tax.compute_all(
    #                 ptav.price_extra)['total_included'])

    #             total_price = new_list_price + new_price_extra

    #             ptav.price_extra = new_price_extra
    #             env.cr.commit()

    #             print(product_template.name,  ptav.name,
    #                   new_list_price, new_price_extra, total_price)
    #     else:
    #         print(product_template.name, new_list_price)

    # for gst_tax in all_gst_taxes:
    #     gst_tax.price_include = True
    #     env.cr.commit()


if __name__ == '__main__':
    main()  # noqa

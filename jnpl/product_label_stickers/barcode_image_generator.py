import os
import pathlib
import tempfile
import uuid

import barcode
from barcode.writer import ImageWriter

from addons.product.models.product_template import ProductTemplate


class BarcodeImageGenerator():
    '''
    from jnpl.product_label_stickers.barcode_image_generator import BarcodeImageGenerator

    generator = BarcodeImageGenerator(self.env['product.product'].browse([509]))
    print(generator.get_output_image_filepath())
    '''
    def __init__(self, product_template: ProductTemplate):
        self.product_template = product_template
        self.output_path = None

    def get_output_image_filepath(self):
        if not self.output_path:
            self.create_image()
        return self.output_path

    def create_image(self):
        filename = str(pathlib.Path(tempfile.gettempdir(), f'{uuid.uuid4()}').absolute())
        ean = barcode.get('ean13', self.product_template.barcode, writer=ImageWriter())
        self.output_path = ean.save(filename)

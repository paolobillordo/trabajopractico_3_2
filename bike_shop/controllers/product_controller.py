from flask import request
from ..models.product_model import Product

class ProductController:

#Ejercicio 2.1    
    @classmethod
    def show_product(cls, product_id):
        result = Product.show_product(product_id)
        return result
    
#Ejercicio 2.2
    @classmethod
    def show_products(cls, brand_id = None, category_id = None):
        brand_filter = request.args.get('brand_id')
        category_filter = request.args.get('category_id')
        result = Product.show_products(brand_filter, category_filter)
        return result
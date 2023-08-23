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
    
#Ejercicio 2.3
    @classmethod
    def create_product(cls):
        product = Product(            
            product_name = request.args.get('product_name', ''),
            brand_id = int(request.args.get('brand_id', '')),
            category_id = int(request.args.get('category_id', '')),
            model_year = int(request.args.get('model_year', '')),
            list_price = float(request.args.get('list_price', ''))
        )                
        return Product.create_product(product)
    
#Ejercicio 2.4
    @classmethod
    def update_product(cls, product_id):
        product = Product( 
            product_id = request.args.get('product_id', ''),           
            product_name = request.args.get('product_name', ''),
            brand_id = int(request.args.get('brand_id', '0')),
            category_id = int(request.args.get('category_id', '0')),
            model_year = int(request.args.get('model_year', '0')),
            list_price = float(request.args.get('list_price', '0'))
        )                
        return Product.update_product(product_id, product)
    
#Ejercicio 2.5
    @classmethod    
    def delete_product(cls, product_id):
        results = Product.delete_product(product_id)
        return results
from flask import Blueprint
from ..controllers.product_controller import ProductController

product_bp = Blueprint('product_bp',__name__)

product_bp.route('/products/<int:product_id>', methods = ['GET'])(ProductController.show_product) #Ejercicio 2.1
product_bp.route('/products', methods = ['GET'])(ProductController.show_products) #Ejercicio 2.2
product_bp.route('/products', methods = ['POST'])(ProductController.create_product) #Ejercicio 2.3
product_bp.route('/products/<int:product_id>', methods = ['PUT'])(ProductController.update_product) #Ejercicio 2.4
product_bp.route('/products/<int:product_id>', methods = ['DELETE'])(ProductController.delete_product) #Ejercicio 2.5

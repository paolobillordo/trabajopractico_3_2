from flask import Blueprint
from ..controllers.customer_controller import CustomersController

customer_bp = Blueprint('customer_bp',__name__)


customer_bp.route('/customers/<int:customer_id>', methods = ['GET'])(CustomersController.show_customer) #Ejercicio 1
customer_bp.route('/customers', methods = ['GET'])(CustomersController.show_customers) #Ejercicio 2
customer_bp.route('/customers', methods = ['POST'])(CustomersController.create_customer) #Ejercicio 3
customer_bp.route('/customers/<int:customer_id>', methods = ['PUT'])(CustomersController.update_customer) #Ejercicio 4
customer_bp.route('/customers/<int:customer_id>', methods = ['DELETE'])(CustomersController.delete_customer)
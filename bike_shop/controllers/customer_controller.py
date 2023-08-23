from flask import request
from ..models.customer_model import Customers


class CustomersController:

#Ejercicio 1.1
    @classmethod
    def show_customer(cls, customer_id):
        results = Customers.show_customer(customer_id)
        return results

#Ejercicio 1.2
    @classmethod
    def show_customers(cls, state = None):
        state_filter = request.args.get('state')
        results = Customers.show_customers(state_filter)
        return results

#Ejercicio 1.3
    @classmethod
    def create_customer(cls):
        customer = Customers(
            customer_id = request.args.get('customer_id',''),
            first_name = request.args.get('first_name',''),
            last_name = request.args.get('last_name',''),
            phone = request.args.get('phone',''),
            email = request.args.get('email',''),
            street = request.args.get('street',''),
            city = request.args.get('city',''),
            state = request.args.get('state',''),
            zip_code = request.args.get('zip_code',''),
            )
        return Customers.creat_customer(customer)

#Ejercicio 1.4
    @classmethod
    def update_customer(cls, customer_id):
        customer = Customers(
            customer_id = request.args.get('customer_id',''),
            first_name = request.args.get('first_name',''),
            last_name = request.args.get('last_name',''),
            phone = request.args.get('phone',''),
            email = request.args.get('email',''),
            street = request.args.get('street',''),
            city = request.args.get('city',''),
            state = request.args.get('state',''),
            zip_code = request.args.get('zip_code',''),
            )
                
        return Customers.update_customer(customer_id, customer)

#Ejercicio 1.5
    @classmethod    
    def delete_customer(cls, customer_id):
        results = Customers.delete_customer(customer_id)
        return results
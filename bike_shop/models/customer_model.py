from ..database import DatabaseConnection
from flask import jsonify
class Customers:
    def __init__(self, customer_id = None ,first_name = None, last_name = None, phone = None, email = None, street = None, city = None, state = None, zip_code = None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __repr__(self):
        return str(self.__dict__)


#Ejercicio 1.1
    @classmethod
    def show_customer(cls, customer_id):
        params = customer_id,
        query = "SELECT * FROM customers WHERE customer_id = %s"
        results = DatabaseConnection.fetch_one("sales", query, params)
        
        if results:
            customer = Customers(results[0],results[1],results[2],results[3],results[4],results[5],results[6],results[7],results[8])
            return jsonify(customer.__dict__)
            # return {
            #     'customer_id': results[0],
            #     'first_name': results[1],
            #     'last_name': results[2],
            #     'phone': results[3],
            #     'email': results[4],
            #     'street': results[5],
            #     'city': results[6],
            #     'state': results[7],
            #     'zip_code': results[8]
            # }, 200        
        return jsonify({"error": "Customer not found"}), 404

#Ejercicio 1.2
    @classmethod
    def show_customers(cls, state_filter = None):
        query = "SELECT * FROM customers"
        params = ""
        if state_filter:
            query += " WHERE state = %s"
            params = (state_filter,)
        results = DatabaseConnection.fetch_all("sales", query, params)
        customers = []
        for i in results:
            customer = Customers(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8])
            customers.append(customer.__dict__)
        total = len(customers)

        return jsonify({"customers": customers, "total" : total}), 200
    
#Ejercicio 1.3
    @classmethod
    def creat_customer(cls, customer):
        params = (customer.first_name, customer.last_name, customer.phone, customer.email, customer.street, customer.city, customer.state, customer.zip_code)
        query = "INSERT INTO customers (first_name, last_name, phone, email, street, city, state, zip_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        DatabaseConnection.execute_query("sales", query, params)
        
        return jsonify({"mensaje": "Customer creado"}), 201
    
#Ejercicio 1.4
    @classmethod
    def update_customer(cls, customer_id, customer):        
        dict = customer.__dict__
        campos = []
        params = []
        for clave in dict:                                        
            if dict[clave] != "":
                params.append(dict[clave])
                campos.append(clave + " = %s")
        campos_str = ", ".join(campos)
        params.append(customer_id)                
        query = f"UPDATE customers SET {campos_str} WHERE customer_id = %s"
        if campos:
            DatabaseConnection.execute_query("sales", query, params)
            return jsonify({"mensaje": "Customer modificado"}), 200
        return jsonify({"mensaje": "No hay campos para modificar"}), 400

        
#Ejercicio 1.5
    @classmethod
    def delete_customer(cls, customer_id):
        query = "DELETE FROM customers WHERE customer_id = %s;"
        params = customer_id,
        result = DatabaseConnection.execute_query("sales", query, params)        
        if result:
            return jsonify({"mensaje": "Customer eliminado con éxito"}), 204
        
        return jsonify({"error": "Customer not found"}), 404

       
           
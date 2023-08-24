from ..database import DatabaseConnection
from flask import jsonify

class Product:

    def __init__(self, product_id = None, brand_id = None, category_id = None, list_price = None, model_year = None, product_name = None):
        self.brand_id = brand_id       
        self.category_id = category_id        
        self.list_price = list_price
        self.model_year = model_year        
        self.product_name = product_name
        self.product_id = product_id

#Ejercicio 2.1
    @classmethod
    def show_product(cls, product_id):
        params = product_id,
        query = ("SELECT A.brand_id, A.brand_name, C.category_id, C.category_name, "
         "B.list_price, B.model_year, B.product_id, B.product_name "
         "FROM brands as A "
         "INNER JOIN products as B on A.brand_id = B.brand_id "
         "INNER JOIN categories as C on B.category_id = C.category_id "
         "WHERE B.product_id = %s")
        results = DatabaseConnection.fetch_one("production",query, params)
        if results:
            product = {
                'brand': {
                    'brand_id': results[0],
                    'brand_name': results[1]
                },
                'category': {
                    'category_id': results[2],
                    'category_name': results[3]
                },
                'list_price': results[4],
                'model_year': results[5],
                'product_id': results[6],
                'product_name': results[7]
            }
            return jsonify(product), 200
        else:
            return jsonify({"error": "Product not found"}), 404
        
#Ejercicio 2.2
    @classmethod
    def show_products(cls, brand_filter, category_filter):
        query = ("SELECT A.brand_id, A.brand_name, C.category_id, C.category_name, "
         "B.list_price, B.model_year, B.product_id, B.product_name "
         "FROM brands as A "
         "INNER JOIN products as B on A.brand_id = B.brand_id "
         "INNER JOIN categories as C on B.category_id = C.category_id ")
        params = ()
        if brand_filter:
            params += (brand_filter,)
            query += "WHERE A.brand_id = %s"
            if category_filter:
                params += (category_filter,)
                query += " AND B.category_id = %s"
        if category_filter and (category_filter not in params):
            params += (category_filter,)
            query += "WHERE B.category_id = %s"            
        result = DatabaseConnection.fetch_all('production', query, params)
        if result:
            products = []
            for i in result:
                product = {
                    "brand": {
                        "brand_id": i[0],
                        "brand_name": i[1]
                    },
                    "category": {
                        "category_id": i[2],
                        "category_name": i[3]
                    },
                    "list_price": i[4],
                    "model_year": i[5],
                    "product_id": i[6],
                    "product_name": i[7]
                }
                products.append(product)
            total = len(products)
            return jsonify({"Products": products, "Total": total}), 200
        else:
            return jsonify({"error": "Products not found"}), 404
        
#Ejercicio 2.3
    @classmethod
    def create_product(cls, product):
        params = (product.product_name, product.brand_id, product.category_id, product.model_year, product.list_price)
        query = "INSERT INTO products (product_name, brand_id, category_id, model_year, list_price) VALUES (%s,%s,%s,%s,%s)"
        DatabaseConnection.execute_query('production', query, params)
        return jsonify({'mensaje': 'Producto creado con éxito'}), 201
    
#Ejercicio 2.4
    @classmethod
    def update_product(cls, product_id, product):
        dict = product.__dict__
        campos = []
        params = []
        for clave in dict:                                        
            if dict[clave] != "":
                params.append(dict[clave])
                campos.append(clave + " = %s")
        campos_str = ", ".join(campos)
        params.append(product_id)                
        query = f"UPDATE products SET {campos_str} WHERE product_id = %s"
        if campos:
            DatabaseConnection.execute_query('production', query, params)
            return jsonify({"mensaje": "Producto modificado"}), 200
        return jsonify({"mensaje": "No hay campos para modificar"}), 400
    
#Ejercicio 2.5
    @classmethod
    def delete_product(cls, product_id):
        query = "DELETE FROM products WHERE product_id = %s;"
        params = product_id,
        result = DatabaseConnection.execute_query('production', query, params)        
        if result:
            return jsonify({"mensaje": "Producto eliminado con éxito"}), 204
        
        return jsonify({"error": "Product not found"}), 404

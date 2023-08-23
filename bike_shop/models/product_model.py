from ..database import DatabaseConnection
from flask import jsonify

class Product:

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
        return result
        

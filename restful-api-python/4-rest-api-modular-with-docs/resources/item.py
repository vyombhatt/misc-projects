# Instead of including the routes in app.py, we create a separate class for them
from flask import request
import uuid
from db import items # input data is brought from another python file
from flask.views import MethodView
from flask_smorest import Blueprint

# The modularization is done by creating a blueprint for your api
blp = Blueprint("items", __name__, description="Operations on items")

# We route the "/items" to pass through the blueprint
# Inside it, a class is created with functions for the different api operations 
# The logic for each function is the same as before in the non-modular codes 
@blp.route("/item")
class Item(MethodView):
    def get(self):
        if bool(request.args.get('id')) == True:
            id = request.args.get('id')
            try:
                return items[id]
            except KeyError:
                return {"message" : "Record does not exist!"}, 404 # like mentioned above, it's a good practice to send status code
        else:
            return {"items": items}, 200
        
    def put(self):
        request_data = request.get_json()
        update_id = request.args.get('id')
        # adding additional validation
        if "name" not in request_data or "price" not in request_data:
            return {'message':"'name' and 'price' must be included in body"}, 404 # bad request code
        if update_id in list(items.keys()):
            items[update_id] = request_data
            return {"message":"item updated successfully!"}, 200 # along with dictionary, you can return a specific status code if needed
        return {"message" : "Record does not exist!"}, 404

    def post(self):
        request_data = request.get_json()
        # adding additional validation to handle exceptions
        if "name" not in request_data or "price" not in request_data:
            return {'message':"'name' and 'price' must be included in body"}, 404 # bad request code
        id = uuid.uuid4().hex
        items[id] = request_data
        return {"message":"item added successfully!"}, 201 # along with dictionary, you can return a specific status code if needed

    def delete(self):
        delete_id = request.args.get('id')
        if delete_id in list(items.keys()):
            del items[delete_id]
            return {'message': "item deleted successfully!"}, 200
        return {"message" : "Record does not exist!"}, 404 # like mentioned above, it's a good practice to send status code


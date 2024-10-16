# Instead of including the routes in app.py, we create a separate class for them
from flask import request
import uuid
from db import items # input data is brought from another python file
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas import ItemSchema

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
                for item in items:
                    if item['id'] == id:
                        return {'items':[item]} # We return individual item as a list to keep it consistent with the case when all items are returned, since all items are a list
            except KeyError:
                return {"message" : "Record does not exist!"}, 404 # like mentioned above, it's a good practice to send status code
        else:
            return {"items": items}, 200
    
    @blp.arguments(ItemSchema)
    def put(self, request_data):
        # request_data = request.get_json() # This is now passed as a parameter in the function, no need to create it
        update_id = request.args.get('id')
        # previously included manual validation is not needed as schemas.py does it 
        for item in items:
            if item['id'] == update_id:
                item['item']['name'] = request_data['name']
                item['item']['price'] = request_data['price']
                return {"message":"item updated successfully!"}, 200 # along with dictionary, you can return a specific status code if needed
        return {"message" : "Record does not exist!"}, 404

    @blp.arguments(ItemSchema)
    def post(self, request_data):
        # request_data = request.get_json() # This is now passed as a parameter in the function, no need to create it
        # request_data = request.get_json()
        # previously included manual validation is not needed as schemas.py does it 
        id = uuid.uuid4().hex
        items.append({'id':id, 'item':{'name':request_data['name'], 'price':request_data['price']}})
        return {"message":"item added successfully!"}, 201 # along with dictionary, you can return a specific status code if needed

    def delete(self):
        delete_id = request.args.get('id')
        del_index = None
        for i, item in enumerate(items):
            if item['id'] == delete_id:
                del_index = i
        if del_index is not None:
            del items[del_index]
            return {'message': "item deleted successfully!"}, 200
        return {"message" : "Record does not exist!"}, 404 # like mentioned above, it's a good practice to send status code


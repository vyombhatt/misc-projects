# $flask run (to run this file)
# The .flasenv file with FLASK_DEBUG=1 ensures that flask app reruns automatically when a change is made

from flask import Flask, request
import uuid
from db import items # input data is brought from another python file

app = Flask(__name__)
# app opens in this url: http://127.0.0.1:5000

# In rest api's, unlike normal api's, the difference is that all api tasks will share the same interface
# The api will differentite tasks based on the api commands i.e. get/put/delete/post

# @app.get('/items') # pass route inside @app.get
# def get_items():
#     return {"items": items}  # always return a dictionary that is eventually considered as a json file

@app.get('/item')
def get_item():
    if bool(request.args.get('id')) == True:
        id = request.args.get('id')
        try:
            return items[id]
        except KeyError:
            return {"message" : "Record does not exist!"}, 404 # like mentioned above, it's a good practice to send status code
    else:
        return {"items": items}, 200

# Adding an item
@app.post('/item')
def add_item():
    request_data = request.get_json()
    # adding additional validation
    if "name" not in request_data or "price" not in request_data:
        return {'message':"'name' and 'price' must be included in body"}, 404 # bad request code
    id = uuid.uuid4().hex
    items[id] = request_data
    return {"message":"item added successfully!"}, 201 # along with dictionary, you can return a specific status code if needed

# Updating an item using put request
@app.put('/item')
def update_item():
    request_data = request.get_json()
    update_id = request.args.get('id')
    # adding additional validation
    if "name" not in request_data or "price" not in request_data:
        return {'message':"'name' and 'price' must be included in body"}, 404 # bad request code
    if update_id in list(items.keys()):
        items[update_id] = request_data
        return {"message":"item updated successfully!"}, 200 # along with dictionary, you can return a specific status code if needed
    return {"message" : "Record does not exist!"}, 404

# Deleting an item
@app.delete('/item')
def delete_item():
    delete_id = request.args.get('id')
    if delete_id in list(items.keys()):
        del items[delete_id]
        return {'message': "item deleted successfully!"}, 200
    return {"message" : "Record does not exist!"}, 404 # like mentioned above, it's a good practice to send status code

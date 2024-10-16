# $flask run (to run this file)
# The .flasenv file with FLASK_DEBUG=1 ensures that flask app reruns automatically when a change is made

from flask import Flask, request

app = Flask(__name__)
# app opens in this url: http://127.0.0.1:5000

items = [
    {
        "name" : "Green Apple Mojito",
        "price" : 160
    },
    {
        "name" : "Momos",
        "price" : 60
    },
    {
        "name" : "Fries",
        "price" : 80
    }
]

# In rest api's, unlike normal api's, the difference is that all api tasks will share the same interface
# The api will differentite tasks based on the api commands i.e. get/put/delete/post

# @app.get('/items') # pass route inside @app.get
# def get_items():
#     return {"items": items}  # always return a dictionary that is eventually considered as a json file

@app.get('/item')
def get_item():
    if bool(request.args.get('name')) == True:
        name = request.args.get('name')
        for item in items:
            if item['name'] == name:
                return item
        return {"message" : "Record does not exist!"}, 404 # like mentioned above, it's a good practice to send status code
    else:
        return {"items": items}, 200

@app.post('/item')
def add_item():
    request_data = request.get_json()
    items.append(request_data)
    return {"message":"item added successfully!"}, 201 # along with dictionary, you can return a specific status code if needed

# Updating an item using put request
@app.put('/item')
def update_item():
    request_data = request.get_json()
    for item in items:
        if item['name']==request_data['name']:
            item['price']=request_data['price']
            return {"message":"item updated successfully!"}, 200 # along with dictionary, you can return a specific status code if needed
    return {"message" : "Record does not exist!"}, 404

# Deleting an item
@app.delete('/item')
def delete_item():
    name = request.args.get('name')
    for item in items:
        if item['name'] == name:
            items.remove(item)
            return {'message': "item deleted successfully!"}, 200
    return {"message" : "Record does not exist!"}, 404 # like mentioned above, it's a good practice to send status code

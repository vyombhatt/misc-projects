# $flask run (to run this file)

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
    }
]

# http://127.0.0.1:5000/get-items
@app.get('/get-items') # pass route inside @app.get
def get_items():
    return {"items": items}  # always return a dictionary that is eventually considered as a json file

@app.post('/add-item')
def add_item():
    request_data = request.get_json()
    items.append(request_data)
    return {"message":"item added successfully!"}, 201 # along with dictionary, you can return a specific status code if needed

# There are  ways to raise a get request
# # 1. Using a Dynamic URL
# #  http://127.0.0.1:5000/get-item/Bloody Mary
# @app.get('/get-item/<string:name>') 
# # <string:name> tells the api to expect a string at the end of url and save it in variable name
# def get_item(name):
#     for item in items:
#         if item['name'] == name:
#             return item
#     return {"message" : "Record does not exist!"}

# 2. Using a paramter
# http://127.0.0.1:5000/get-item/?name=Momos
@app.get('/get-item')
def get_item():
    name = request.args.get('name')
    for item in items:
        if item['name'] == name:
            return item
    return {"message" : "Record does not exist!"}, 404 # like mentioned above, it's a good practice to send status code

# Updating an item using put request
@app.put('/update-item')
def update_item():
    request_data = request.get_json()
    for item in items:
        if item['name']==request_data['name']:
            item['price']=request_data['price']
            return {"message":"item updated successfully!"}, 200 # along with dictionary, you can return a specific status code if needed
    return {"message" : "Record does not exist!"}, 404

# Deleting an item
@app.delete('/delete-item')
def delete_item():
    name = request.args.get('name')
    for item in items:
        if item['name'] == name:
            items.remove(item)
            return {'message': "item deleted successfully!"}, 200
    return {"message" : "Record does not exist!"}, 404 # like mentioned above, it's a good practice to send status code

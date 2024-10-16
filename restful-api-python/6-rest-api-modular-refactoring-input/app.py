# $flask run (to run this file)
# The .flasenv file with FLASK_DEBUG=1 ensures that flask app reruns automatically when a change is made

from flask import Flask
from resources.item import blp as ItemBluePrint
from flask_smorest import Api

app = Flask(__name__)
# app opens in this url: http://127.0.0.1:5000

# All the api routing codes have been moved to resources/items.py
# We call the class from there in line 5

# For documentation purposes, we set a few config paramenters
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Items Rest Api"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

# Implement the blueprint that we fetched from resources/items.py
# We need to pass the app through Api class (imported in line 6)
# Then we register out item blueprint with that api
api = Api(app)
api.register_blueprint(ItemBluePrint)

# The api documentation can now be found on http://127.0.0.1:5000/swagger-ui
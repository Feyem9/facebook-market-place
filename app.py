from firebase_admin import credentials, firestore
from flask import Flask 
from firebase_config import db  

from Routes.image_routes import image 


app = Flask(__name__)



app.register_blueprint(image, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)
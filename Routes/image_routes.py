from flask import Blueprint 

from controllers.image_controller import add_image, get_images

image = Blueprint('image', __name__)

image.route('/images', methods=['POST'])(add_image)
image.route('/images', methods=['GET'])(get_images)

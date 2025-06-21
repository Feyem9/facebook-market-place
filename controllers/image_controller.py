from flask import request, jsonify
from models.image_model import Image
from firebase_config import db
from firebase_admin import storage
import requests, tempfile, os
from firebase_config import db  
from response import success_response, error_response


def add_image():
    data = request.get_json()

    if 'nom' not in data or 'url' not in data:
        return jsonify({"error": "Champs 'nom' et 'url' requis"}), 400

    try:
       
        response = requests.get(data['url'])
        response.raise_for_status()
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        temp_file.write(response.content)
        temp_file.close()

        
        nom_fichier = f"images/{data['nom']}.jpg"
        bucket = storage.bucket()
        blob = bucket.blob(nom_fichier)
        blob.upload_from_filename(temp_file.name)
        blob.make_public()

        
        image = Image(
            nom=data['nom'],
            original_url=data['url'],
            firebase_url=blob.public_url
        )

       
        doc_ref = db.collection("images").add(image.to_dict())

        
        os.remove(temp_file.name)

        return jsonify(success_response("Image ajoutée avec succès", {
        "id": doc_ref[1].id,
        "firebase_url": image.firebase_url
    })), 201

    except Exception as e:
        return jsonify(error_response("Erreur lors de l’ajout de l’image", e)), 500


def get_images():
    docs = db.collection("images").stream()
    images = [{"id": doc.id, **doc.to_dict()} for doc in docs]
    return jsonify(images), 200

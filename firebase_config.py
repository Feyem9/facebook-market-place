import firebase_admin 
from firebase_admin import credentials, firestore, storage 

cred = credentials.Certificate("../../Downloads/facebook-market-place-fv-firebase-adminsdk-fbsvc-1e3dae4521.json")

bucket_name = "facebook-market-place-fv.firebasestorage.app"

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        "storageBucket": bucket_name
    })

db = firestore.client()
bucket = storage.bucket()

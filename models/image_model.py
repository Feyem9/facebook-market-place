from datetime import datetime

class Image:
    def __init__(self, nom, original_url, firebase_url, uploaded_at=None):
        self.nom = nom
        self.original_url = original_url
        self.firebase_url = firebase_url
        self.uploaded_at = uploaded_at or datetime.utcnow()

    def to_dict(self):
        return {
            "nom": self.nom,
            "original_url": self.original_url,
            "firebase_url": self.firebase_url,
            "uploaded_at": self.uploaded_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            nom=data.get("nom"),
            original_url=data.get("original_url"),
            firebase_url=data.get("firebase_url"),
            uploaded_at=datetime.fromisoformat(data.get("uploaded_at"))
        )

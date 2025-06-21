def success_response(message, data=None):
    return {
        "status_code": 200,
        "message": message,
        "data": data or {}
    }

def error_response(message="Une erreur s'est produite", error=None, code=500):
    return {
        "status_code": code,
        "message": message,
        "error": str(error) if error else None
    }

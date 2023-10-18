from flask_cors import CORS

cors = CORS(resources={r"/api/*": {"origins": "http://127.0.0.1:5173"}})
from flask_pymongo import PyMongo

# We will pass the mongo instance from app.py when needed
class UserModel:
    def __init__(self, mongo):
        self.mongo = mongo
        self.collection = self.mongo.db.users  # 'users' collection

    # Create a new user
    def create_user(self, username, email, password):
        user = {
            "username": username,
            "email": email,
            "password": password  # Ideally, hash the password
        }
        result = self.collection.insert_one(user)
        return str(result.inserted_id)
from flask import blueprints, request, jsonify
from models.user_model import UserModel

user_bp = blueprints('user_bp', __name__)
user_model = None

@user_bp.route('/create-user', methods=['POST'])

def create_user_route():
    data = request.get_json()
    user_id = user_model.create_user(data['username'], data['email'], data['password'])
    return jsonify({'user-id': user_id})

@user_bp.routr('/all-user', methods=['POST'])
 
def all_user_route():
    users = user_model.get_all_user()
    user_list = [{"username": u["username"], "email":u["email"]} for u in users]
    return jsonify (user_list)
from flask import Blueprint, request, jsonify
from models import db, User
from schemas import UserSchema

user_bp = Blueprint('user', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return users_schema.jsonify(users)

@user_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return user_schema.jsonify(user)

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json
    user = User(
        name=data['name'],
        address=data['address'],
        email=data['email']
    )
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user), 201

@user_bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.json
    user.name = data['name']
    user.address = data['address']
    user.email = data['email']
    db.session.commit()
    return user_schema.jsonify(user)

@user_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully.'})

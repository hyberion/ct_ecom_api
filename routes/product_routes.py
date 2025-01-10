from flask import Blueprint, request, jsonify
from models import db, Product
from schemas import ProductSchema

# Initialize Blueprint for Product routes
product_bp = Blueprint('product', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# GET /products: Retrieve all products
@product_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

# GET /products/<id>: Retrieve a product by ID
@product_bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return product_schema.jsonify(product)

# POST /products: Create a new product
@product_bp.route('/', methods=['POST'])
def create_product():
    data = request.json
    product = Product(
        product_name=data['product_name'],
        price=data['price'],
        description=data.get('description')
    )
    db.session.add(product)
    db.session.commit()
    return product_schema.jsonify(product), 201

# PUT /products/<id>: Update a product by ID
@product_bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.json
    product.product_name = data['product_name']
    product.price = data['price']
    db.session.commit()
    return product_schema.jsonify(product)

# DELETE /products/<id>: Delete a product by ID
@product_bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully.'})


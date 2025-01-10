from flask import Blueprint, request, jsonify
from models import db, Order, Product, OrderProduct
from schemas import OrderSchema, ProductSchema, OrderProductSchema

# Initialize Blueprint for Order routes
order_bp = Blueprint('order', __name__)
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

# POST /orders: Create a new order
@order_bp.route('/', methods=['POST'])
def create_order():
    data = request.json
    order = Order(
        user_id=data['user_id'],
        order_date=data['order_date'],
        status=data.get('status', 'pending')  # Default status is 'pending'
    )
    db.session.add(order)
    db.session.commit()
    return order_schema.jsonify(order), 201

# POST /orders/<order_id>/add_products: Add multiple products to an order
@order_bp.route('/<int:order_id>/add_products', methods=['POST'])
def add_products_to_order(order_id):
    order = Order.query.get_or_404(order_id)
    data = request.json

    if 'product_ids' not in data or not isinstance(data['product_ids'], list):
        return jsonify({'error': 'A list of product_ids is required'}), 400

    added_products = []
    for product_id in data['product_ids']:
        product = Product.query.get(product_id)
        if not product:
            continue

        # Prevent duplicate products in the same order
        existing_entry = OrderProduct.query.filter_by(order_id=order.id, product_id=product.id).first()
        if existing_entry:
            continue

        order_product = OrderProduct(order_id=order.id, product_id=product.id)
        db.session.add(order_product)
        added_products.append({'id': product.id, 'product_name': product.product_name})

    db.session.commit()
    return jsonify({'message': 'Products added to order successfully.', 'added_products': added_products}), 201

# DELETE /orders/<order_id>/remove_product/<product_id>: Remove a product from an order
@order_bp.route('/<int:order_id>/remove_product/<int:product_id>', methods=['DELETE'])
def remove_product_from_order(order_id, product_id):
    order_product = OrderProduct.query.filter_by(order_id=order_id, product_id=product_id).first()
    if not order_product:
        return jsonify({'message': 'Product not found in the order.'}), 404

    db.session.delete(order_product)
    db.session.commit()
    return jsonify({'message': 'Product removed from order successfully.'})

# GET /orders/user/<user_id>: Get all orders for a user with pagination
@order_bp.route('/user/<int:user_id>', methods=['GET'])
def get_orders_for_user(user_id):
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    orders = Order.query.filter_by(user_id=user_id).paginate(page=page, per_page=per_page)
    return jsonify({
        'orders': orders_schema.dump(orders.items),
        'total': orders.total,
        'pages': orders.pages,
        'current_page': orders.page
    })

# GET /products: Get all products with pagination
@order_bp.route('/products', methods=['GET'])
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    products = Product.query.paginate(page=page, per_page=per_page)
    return jsonify({
        'products': products_schema.dump(products.items),  # Corrected to products.items
        'total': products.total,
        'pages': products.pages,
        'current_page': products.page
    })


# PUT /orders/<order_id>/status: Update the status of an order
@order_bp.route('/<int:order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    order = Order.query.get_or_404(order_id)
    data = request.json
    if 'status' not in data:
        return jsonify({'error': 'Status field is required'}), 400

    order.status = data['status']
    db.session.commit()
    return jsonify({'message': f"Order {order_id} status updated to '{order.status}'"})


# GET /orders/<order_id>: Retrieve a single order by ID
@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get_or_404(order_id)
    return order_schema.jsonify(order)


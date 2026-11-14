
from flask import Flask, jsonify, request

app = Flask(__name__)

# sample orders
orders = [
    {"order_id": 1, "item": "Adobo", "paid": True},
    {"order_id": 2, "item": "Pancit", "paid": False},
]


def find_order(order_id):
    return next((order for order in orders if order["order_id"] == order_id), None)


# Rowel Dulu
@app.get("/orders")
def get_orders():
    return jsonify(orders), 200


# Gideon Fernandez
@app.get("/orders/<int:order_id>")
def get_order(order_id):
    order = find_order(order_id)
    if order is None:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order), 200


# John Andhrie Mercado



# Kimber John Patio



if __name__ == "__main__":
    app.run(debug=True)

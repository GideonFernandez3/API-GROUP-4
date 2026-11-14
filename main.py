
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



# John Andhrie Mercado



# Kimber John Patio



if __name__ == "__main__":
    app.run(debug=True)

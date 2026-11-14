
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



# Gideon Fernandez



# John Andhrie Mercado
@app.post("/orders")

def create_order():
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not isinstance(data.get("item"), str) or not data["item"].strip():
        
        return jsonify({"error": "A non-empty item is required"}), 400

    if "paid" in data and not isinstance(data["paid"], bool):
        return jsonify({"error": "paid must be true or false"}), 400

    next_id = max((order["order_id"] for order in orders), default=0) + 1
    order = {"order_id": next_id, "item": data["item"].strip(), "paid": data.get("paid", False)}
    orders.append(order)
        return jsonify(order), 201
 


# Kimber John Patio



if __name__ == "__main__":
    app.run(debug=True)

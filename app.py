"""Inventory service monitored by AEGIS."""
import os
from flask import Flask, jsonify, abort, request

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("FLASK_SECRET_KEY", os.urandom(16).hex())

ITEMS = {
    "sku-100": {"sku": "sku-100", "name": "widget", "qty": 42},
    "sku-200": {"sku": "sku-200", "name": "gadget", "qty": 7},
}


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/items")
def items():
    return jsonify(sorted(ITEMS.values(), key=lambda i: i["sku"]))


@app.get("/items/<sku>")
def item(sku):
    if sku not in ITEMS:
        abort(404)
    return jsonify(ITEMS[sku])


@app.post("/items/<sku>/reserve")
def reserve(sku):
    qty = request.get_json(force=True).get("qty", 1)
    if not isinstance(qty, int) or qty < 1:
        return jsonify({"error": "qty must be a positive integer"}), 400
    item = ITEMS.get(sku) or abort(404)
    if item["qty"] < qty:
        return jsonify({"error": "insufficient stock"}), 409
    item["qty"] -= qty
    return jsonify(item)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5002)

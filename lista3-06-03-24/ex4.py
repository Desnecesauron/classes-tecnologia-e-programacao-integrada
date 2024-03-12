# Crie uma API para gerenciar produtos de um e-commerce, permitindo adicionar, listar,
# atualizar estoque, deletar produtos e gerenciar um carrinho de compras.
# Obs: Utilize arquivos (txt ou JSON) para simular cada operação de persistência de dados.

from flask import Flask, request
import json
import os


app = Flask(__name__)


def load_products():
    if os.path.exists('products.json'):
        with open('products.json', 'r') as file:
            return json.load(file)
    return []


def save_products(products):
    with open('products.json', 'w') as file:
        json.dump(products, file)


def load_cart():
    if os.path.exists('cart.json'):
        with open('cart.json', 'r') as file:
            return json.load(file)
    return []


def save_cart(cart):
    with open('cart.json', 'w') as file:
        json.dump(cart, file)


@app.route('/products', methods=['POST'])
def create_product():
    products = load_products()
    data = request.json
    products.append(data)
    save_products(products)
    return {'result': 'Product created'}


@app.route('/products', methods=['GET'])
def list_products():
    products = load_products()
    return {'products': products}


@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    products = load_products()
    data = request.json
    for product in products:
        if product['id'] == product_id:
            product.update(data)
            save_products(products)
            return {'result': 'Product updated'}
    return {'result': 'Product not found'}


@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    products = load_products()
    for product in products:
        if product['id'] == product_id:
            products.remove(product)
            save_products(products)
            return {'result': 'Product deleted'}
    return {'result': 'Product not found'}


@app.route('/cart', methods=['POST'])
def add_to_cart():
    cart = load_cart()
    data = request.json
    cart.append(data)
    save_cart(cart)
    return {'result': 'Product added to cart'}


@app.route('/cart', methods=['GET'])
def list_cart():
    cart = load_cart()
    return {'cart': cart}


@app.route('/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    cart = load_cart()
    for product in cart:
        if product['id'] == product_id:
            cart.remove(product)
            save_cart(cart)
            return {'result': 'Product removed from cart'}
    return {'result': 'Product not found'}


app.run(port=5004)

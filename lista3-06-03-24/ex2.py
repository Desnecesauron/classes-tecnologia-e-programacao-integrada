# Crie uma API para cadastro de usuários, permitindo
# a inclusão, consulta, atualização e exclusão de usuários.
# Obs: Utilize arquivos (txt ou JSON) para simular cada operação de persistência de dados.

from flask import Flask, request
import json
import os

app = Flask(__name__)


def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as file:
            return json.load(file)
    return []


def save_users(users):
    with open('users.json', 'w') as file:
        json.dump(users, file)


@app.route('/users', methods=['POST'])
def create_user():
    users = load_users()
    data = request.json
    users.append(data)
    save_users(users)
    return {'result': 'User created'}


@app.route('/users', methods=['GET'])
def list_users():
    users = load_users()
    return {'users': users}


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    users = load_users()
    data = request.json
    for user in users:
        if user['id'] == user_id:
            user.update(data)
            save_users(users)
            return {'result': 'User updated'}
    return {'result': 'User not found'}


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = load_users()
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            save_users(users)
            return {'result': 'User deleted'}
    return {'result': 'User not found'}


app.run(port=5002)

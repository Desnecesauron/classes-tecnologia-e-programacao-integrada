# Crie uma API para gerenciar uma lista de tarefas, permitindo adicionar, listar, marcar
# como concluída e excluir tarefas.
# Obs: Utilize arquivos (txt ou JSON) para simular cada operação de persistência de dados

from flask import Flask, request
import json
import os


app = Flask(__name__)


def load_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)


@app.route('/tasks', methods=['POST'])
def create_task():
    tasks = load_tasks()
    data = request.json
    tasks.append(data)
    save_tasks(tasks)
    return {'result': 'Task created'}


@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = load_tasks()
    return {'tasks': tasks}


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tasks = load_tasks()
    data = request.json
    for task in tasks:
        if task['id'] == task_id:
            task.update(data)
            save_tasks(tasks)
            return {'result': 'Task updated'}
    return {'result': 'Task not found'}


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return {'result': 'Task deleted'}
    return {'result': 'Task not found'}


app.run(port=5003)

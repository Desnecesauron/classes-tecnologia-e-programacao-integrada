# Crie uma API que aceite dois números e realize operações básicas de uma calculadora
# (adição, subtração, multiplicação e divisão).

from flask import Flask, request

app = Flask(__name__)


@app.route('/calc', methods=['POST'])
def calc():
    data = request.json
    num1 = data['num1']
    num2 = data['num2']
    op = data['op']
    if op == '+':
        return {'result': num1 + num2}
    elif op == '-':
        return {'result': num1 - num2}
    elif op == '*':
        return {'result': num1 * num2}
    elif op == '/':
        return {'result': num1 / num2}
    else:
        return {'result': 'Invalid operation'}


app.run(port=5001)

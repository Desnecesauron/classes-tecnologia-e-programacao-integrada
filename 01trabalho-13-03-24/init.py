from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/test'
db = SQLAlchemy(app)


class Enquete(db.Model):
    __tablename__ = 'enquete'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(80), nullable=False)
    opcoes = relationship('Opcao', backref='enquete', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'opcoes': [opcao.to_dict() for opcao in self.opcoes]
        }


class Opcao(db.Model):
    __tablename__ = 'opcao'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(80), nullable=False)
    votos = Column(Integer, default=0)
    enquete_id = Column(Integer, ForeignKey('enquete.id'), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'descricao': self.descricao,
            'votos': self.votos,
            'enquete_id': self.enquete_id
        }


@app.route('/api/enquetes', methods=['POST'])
def criar_enquete():
    if not request.json or not 'descricao' in request.json:
        abort(400, description="Missing descricao in request data.")
    opc = request.json.get('opcoes', [])
    opcoes = [Opcao(**opcao) for opcao in opc]
    enquete = Enquete(descricao=request.json['descricao'], opcoes=opcoes)
    db.session.add(enquete)
    db.session.commit()
    return jsonify({'enquete': enquete.to_dict()}), 201


@app.route('/api/enquetes', methods=['GET'])
def listar_enquetes():
    enquetes = Enquete.query.all()
    return jsonify({'enquetes': [enquete.to_dict() for enquete in enquetes]})


@app.route('/api/enquetes/<int:id>', methods=['GET'])
def obter_detalhes_enquete(id):
    enquete = Enquete.query.get(id)
    if enquete is None:
        abort(404, description="Enquete not found.")
    return jsonify({'enquete': enquete.to_dict()})


@app.route('/api/enquetes/<int:id>/votar', methods=['POST'])
def votar_opcao_enquete(id):
    if not request.json or not 'id_opcao' in request.json:
        abort(400, description="Missing 'id_opcao' in request data.")
    opcao = Opcao.query.filter_by(id=request.json['id_opcao'], enquete_id=id).first()
    if opcao is None:
        abort(404, description="Opcao not found.")
    opcao.votos += 1
    db.session.commit()
    enquete = Enquete.query.get(id)
    return jsonify({'resultado': 'sucesso', 'enquete': enquete.to_dict()})


@app.route('/api/enquetes/<int:id>/resultados', methods=['GET'])
def resultados_enquete(id):
    enquete = Enquete.query.get(id)
    if enquete is None:
        abort(404, description="Enquete not found.")
    return jsonify({'resultados': [opcao.to_dict() for opcao in enquete.opcoes]})


@app.route('/api/enquetes/<int:id>/opcoes', methods=['GET'])
def visualizar_opcoes_enquete(id):
    enquete = Enquete.query.get(id)
    if enquete is None:
        abort(404, description="Enquete not found.")
    return jsonify({'opcoes': [opcao.to_dict() for opcao in enquete.opcoes]})


@app.route('/api/enquetes/<int:id>/opcoes', methods=['POST'])
def adicionar_opcao_enquete(id):
    if not request.json or not 'descricao' in request.json:
        abort(400, description="Missing 'descricao' in request data.")
    enquete = Enquete.query.get(id)
    if enquete is None:
        abort(404, description="Enquete not found.")
    opcao = Opcao(descricao=request.json['descricao'], enquete_id=id)
    db.session.add(opcao)
    db.session.commit()
    return jsonify({'enquete': enquete.to_dict()}), 201


@app.route('/api/enquetes/<int:id>', methods=['DELETE'])
def deletar_enquete(id):
    enquete = Enquete.query.get(id)
    if enquete is None:
        abort(404, description="Enquete not found.")
    Opcao.query.filter_by(enquete_id=id).delete()
    Enquete.query.filter_by(id=id).delete()
    db.session.commit()
    return jsonify({'resultado': 'sucesso'})


@app.route('/api/enquetes/<int:id_enquete>/opcoes/<int:id_opcao>', methods=['DELETE'])
def deletar_opcao_enquete(id_enquete, id_opcao):
    opcao = Opcao.query.filter_by(id=id_opcao, enquete_id=id_enquete).first()
    if opcao is None:
        abort(404, description="Opcao not found.")
    db.session.delete(opcao)
    db.session.commit()
    return jsonify({'resultado': 'sucesso'})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)

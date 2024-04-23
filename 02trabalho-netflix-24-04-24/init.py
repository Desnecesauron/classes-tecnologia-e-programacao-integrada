from flask import Flask, request, jsonify, abort
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/test'
db = SQLAlchemy(app)
bcrypt = Bcrypt()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    histories = db.relationship('ViewingHistory', backref='user', lazy=True)
    playlists = db.relationship('Playlist', backref='user', lazy=True)

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    synopsis = db.Column(db.Text, nullable=False)
    cast = db.Column(db.String(200), nullable=True)
    director = db.Column(db.String(100), nullable=True)
    average_rating = db.Column(db.Float, nullable=True)
    genre = db.Column(db.String(100), nullable=True)
    year = db.Column(db.Integer, nullable=True)
    classification = db.Column(db.String(10), nullable=True)
    histories = db.relationship('ViewingHistory', backref='content', lazy=True)
    playlists = db.relationship('Playlist', backref='content', lazy=True)


class ViewingHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)


class Playlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)


# Cadastro de Usuários: Os usuários devem poder se cadastrar no sistema fornecendo
# informações básicas, como nome de usuário, email e senha.
@app.route('/api/register', methods=['POST'])
def register():
    if not request.json or not 'username' in request.json or not 'email' in request.json or not 'password' in request.json:
        abort(400, description="Missing username, email or password in request data.")
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    user = User.query.filter_by(username=username).first()
    if user:
        abort(400, description="User already exists.")
    new_user = User(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully.'}), 201


# Autenticação de Usuários: Os usuários registrados devem poder fazer login no
# sistema usando suas credenciais.
@app.route('/api/login', methods=['POST'])
def login():
    if not request.json or not 'username' in request.json or not 'password' in request.json:
        abort(400, description="Missing username or password in request data.")
    username = request.json['username']
    password = request.json['password']
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        abort(401, description="Invalid username or password.")
    return jsonify({'message': 'User logged in successfully.'}), 200


def content_to_dict(content_row):
    return {
        'id': content_row.id,
        'title': content_row.title,
        'synopsis': content_row.synopsis,
        'cast': content_row.cast,
        'director': content_row.director,
        'average_rating': content_row.average_rating,
        'genre': content_row.genre,
        'year': content_row.year,
        'classification': content_row.classification
    }


# Catálogo de Conteúdo: Os usuários devem poder navegar pelo catálogo de filmes e
# séries disponíveis no sistema.
@app.route('/api/content', methods=['GET'])
def content():
    contents = Content.query.all()
    contents_list = [content_to_dict(content) for content in contents]
    return jsonify(contents_list), 200


# Visualização de Detalhes do Título: Os usuários devem poder ver informações
# detalhadas sobre um título específico, incluindo título, sinopse, elenco, diretor,
# avaliação média, entre outros.
@app.route('/api/content/<int:content_id>', methods=['GET'])
def content_detail(content_id):
    contentObj = db.session.get(Content, content_id)
    if not contentObj:
        abort(404, description="Content not found.")
    return content_to_dict(contentObj), 200


# Reprodução de Vídeo: Os usuários devem poder reproduzir vídeos diretamente na
# plataforma (aqui, você deverá considerar só acesso ao vídeo, sem reprodução)
@app.route('/api/play/<int:content_id>/<int:user_id>', methods=['GET'])
def play(content_id, user_id):
    contentObj = db.session.get(Content, content_id)
    if not contentObj:
        abort(404, description="Content not found.")
    userObj = db.session.get(User, user_id)
    if not userObj:
        abort(404, description="User not found.")
    new_history = ViewingHistory(user_id=user_id, content_id=content_id)
    db.session.add(new_history)
    db.session.commit()
    return jsonify({'message': 'Playing content: ' + contentObj.title}), 200


# Histórico de Visualização: O sistema deve manter um histórico de visualização para
# cada usuário, registrando quais filmes e episódios de séries foram assistidos.
@app.route('/api/history/<int:user_id>', methods=['GET'])
def history(user_id):
    histories = ViewingHistory.query.filter_by(user_id=user_id).all()
    history_list = []
    for historyObj in histories:
        contentObj = db.session.get(Content, historyObj.content_id)
        history_list.append(content_to_dict(contentObj))
    return jsonify(history_list), 200


# Busca e Filtros: Os usuários devem poder buscar por títulos específicos e filtrar o
# catálogo por gênero, ano de lançamento, classificação indicativa, entre outros
# critérios.
@app.route('/api/search', methods=['GET'])
def search():
    title = request.args.get('title')
    genre = request.args.get('genre')
    year = request.args.get('year')
    classification = request.args.get('classification')
    if title is None and genre is None and year is None and classification is None:
        abort(400, description="Missing search parameters.")

    query = Content.query

    if title:
        query = query.filter(Content.title.like(f'%{title}%'))
    if genre:
        query = query.filter(Content.genre.like(f'%{genre}%'))
    if year:
        query = query.filter(Content.year.like(f'%{year}%'))
    if classification:
        query = query.filter(Content.classification.like(f'%{classification}%'))

    contents = query.all()
    content_list = [content_to_dict(content) for content in contents]
    return jsonify(content_list), 200


# Listas de Reprodução: Os usuários devem poder criar listas de reprodução
# personalizadas para organizar seu conteúdo favorito.
@app.route('/api/playlist', methods=['POST'])
def create_playlist():
    if not request.json or not 'user_id' in request.json or not 'content_id' in request.json:
        abort(400, description="Missing user_id or content_id in request data.")
    user_id = request.json['user_id']
    content_id = request.json['content_id']
    new_playlist = Playlist(user_id=user_id, content_id=content_id)
    db.session.add(new_playlist)
    db.session.commit()
    return jsonify({'message': 'Playlist created successfully.'}), 201


# Todas as playlists de um usuário
@app.route('/api/playlist/<int:user_id>', methods=['GET'])
def get_playlist(user_id):
    playlists = Playlist.query.filter_by(user_id=user_id).all()
    playlist_list = []
    for playlistObj in playlists:
        contentObj = db.session.get(Content, playlistObj.content_id)
        playlist_list.append(content_to_dict(contentObj))
    return jsonify(playlist_list), 200


def create_content():
    print('Creating content...')
    content1 = Content(title='The Shawshank Redemption',
                       synopsis='Two imprisoned',
                       cast='Tim Robbins, Morgan Freeman',
                       director='Frank Darabont',
                       average_rating=9.3,
                       genre='Drama',
                       year=1994,
                       classification='R'
                       )
    content2 = Content(title='The Godfather',
                       synopsis='The aging patriarch',
                       cast='Marlon Brando, Al Pacino',
                       director='Francis Ford Coppola',
                       average_rating=9.2,
                       genre='Crime',
                       year=1972,
                       classification='R'
                       )
    content3 = Content(title='Matrix',
                          synopsis='A computer hacker learns',
                          cast='Keanu Reeves, Laurence Fishburne',
                          director='Lana Wachowski, Lilly Wachowski',
                          average_rating=8.7,
                          genre='Action',
                          year=1999,
                          classification='R'
                          )
    db.session.add_all({content1, content2, content3})
    db.session.commit()
    print('Content created successfully.')


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        create_content()

    app.run(debug=True)

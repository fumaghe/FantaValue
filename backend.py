from flask import Flask, request, jsonify, redirect, url_for, session
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from pymongo import MongoClient, errors
from flask_cors import CORS
from authlib.integrations.flask_client import OAuth
import secrets
import os

app = Flask(__name__)

# Imposta la chiave segreta per le sessioni Flask utilizzando una variabile d'ambiente
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'Letsgoskiecosichesifa1209348756')

# Configurazione delle chiavi di sicurezza utilizzando variabili d'ambiente
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'Principino12345678')
app.config['GOOGLE_CLIENT_ID'] = os.environ.get('GOOGLE_CLIENT_ID', '975646903047-kk51nbik9d723eqg91tcl43msllaomgl.apps.googleusercontent.com')
app.config['GOOGLE_CLIENT_SECRET'] = os.environ.get('GOOGLE_CLIENT_SECRET', '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')

# Inizializza bcrypt, JWT e CORS
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app, resources={r"/*": {"origins": "*"}})

# Configurazione di OAuth
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id=app.config['GOOGLE_CLIENT_ID'],
    client_secret=app.config['GOOGLE_CLIENT_SECRET'],
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid email profile'},
)

# Connessione a MongoDB
client = MongoClient(os.environ.get('MONGODB_URI', 'mongodb+srv://fumaghe:1909,Andre@fantavaluecluster.wom6a.mongodb.net/FantaValue?retryWrites=true&w=majority'))
db = client['FantaValue']
users = db['users']

@app.route('/')
def home():
    return jsonify({'msg': 'Benvenuto nel backend dell\'applicazione!'}), 200

# Endpoint per la registrazione
@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email or not password:
        return jsonify({'msg': 'Email o password mancanti.'}), 400

    if users.find_one({'email': email}):
        return jsonify({'msg': 'Email già registrata'}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    try:
        users.insert_one({'email': email, 'password': hashed_password})
        return jsonify({'msg': 'Registrazione avvenuta con successo'}), 201
    except errors.PyMongoError as e:
        return jsonify({'msg': 'Errore durante la registrazione', 'error': str(e)}), 500

# Endpoint per il login normale
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    user = users.find_one({'email': email})

    if user and bcrypt.check_password_hash(user['password'], password):
        access_token = create_access_token(identity={'email': user['email']})
        return jsonify({'token': access_token}), 200

    return jsonify({'msg': 'Credenziali non valide'}), 401

# Endpoint per il login con Google
@app.route('/login/google', methods=['GET'])
def login_google():
    redirect_uri = url_for('authorize_google', _external=True)
    nonce = secrets.token_urlsafe(16)  # Genera un nonce casuale
    session['oauth_nonce'] = nonce  # Salva il nonce nella sessione
    return google.authorize_redirect(redirect_uri, nonce=nonce)

# Callback per Google OAuth
@app.route('/authorize/google')
def authorize_google():
    try:
        token = google.authorize_access_token()
        nonce = session.pop('oauth_nonce', None)
        if not nonce:
            return jsonify({'msg': 'Nonce non trovato in sessione, riprovare'}), 400
        
        user_info = google.parse_id_token(token, nonce=nonce)
        
        # Verifica se l'utente esiste già nel database
        user = users.find_one({'email': user_info['email']})
        
        if not user:
            # Se l'utente non esiste, registralo
            users.insert_one({'email': user_info['email'], 'password': None})

        # Genera un token JWT
        access_token = create_access_token(identity={'email': user_info['email']})
        return jsonify({'token': access_token}), 200

    except Exception as e:
        print(f"Errore durante l'autenticazione con Google: {e}")
        return jsonify({'msg': 'Errore durante l\'autenticazione con Google', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

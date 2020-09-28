from flask import Flask, jsonify, request
from flask_cors import CORS
import domain

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

CORS(app)

@app.route('/')
def home():
    return 'Server je pokrenut.'

@app.route('/signup', methods=['POST'])
def signup():
    post_data = request.get_json()
    username = post_data.get('username')
    password = post_data.get('pass')

    k = domain.prijava(username, password)
    if k:
        return jsonify({
            'status': 'success',
            'korisnik': k
        })
    else:
        return jsonify({
            'status': 'not successful'
        })

@app.route('/registracija', methods=['POST'])
def registracija():
    post_data = request.get_json()
    ime = post_data.get('ime')
    prezime = post_data.get('prezime')
    username = post_data.get('username')
    password = post_data.get('pass')
    email = post_data.get('email')
    k = domain.registracija(ime, prezime, username, password, email)
    if k:
        return jsonify({
            'status': 'success'
        })
    else:
        return jsonify({
            'status': 'not successful'
        })



@app.route('/pitanja/<kategorija_id>', methods=['GET'])
def pitanja(kategorija_id):
    _pitanja = domain.dohvatiPitanja(kategorija_id)
    pitanja = []
    for _p in _pitanja:
        p = list(_p)
        odg = domain.dohvatiOdgovore(p[0])
        p.append(odg)
        pitanja.append(p)
    return jsonify({
        'status': 'success',
        'pitanja': pitanja
    })

if __name__ == '__main__':
    app.run(debug=True)

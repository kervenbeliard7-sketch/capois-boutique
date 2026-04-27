from flask import Flask, render_template, url_for

app = Flask(__name__)

# Fonksyon pou jwenn pri a fasil san repete kòd
def jwenn_pri(id):
    if id == 1: return "1500 HTG"
    if id == 2: return "1750 HTG"
    return "2000 HTG"

@app.route('/')
def home():
    liste_produits = [
        {"id": 1, "nom": "T-shirt Capois Classic", "pri": "1500 HTG", "image": "t-shirt.jpg"},
        {"id": 2, "nom": "T-shirt Capois Style", "pri": "1750 HTG", "image": "t-shirt 2.jpg"},
        {"id": 3, "nom": "T-shirt Capois Premium", "pri": "2000 HTG", "image": "t-shirt 3.jpg"}
    ]
    return render_template('index.html', produits=liste_produits)

@app.route('/payer/moncash/<int:id>')
def payer_moncash(id):
    pri_final = jwenn_pri(id)
    return render_template('paiement_moncash.html', prix=pri_final)

@app.route('/payer/natcash/<int:id>')
def payer_natcash(id):
    pri_final = jwenn_pri(id)
    return render_template('paiement_natcash.html', prix=pri_final)

if __name__ == '__main__':
    app.run(debug=True)
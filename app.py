from flask import Flask, render_template, request, url_for

app = Flask(__name__, template_folder='templates', static_folder='static')

# Lojik pou kalkile pri promo yo selon chak pwodwi
def kalkile_pri(id_pwodwi, kantite):
    k = int(kantite)
    
    # 1. T-shirt Simple
    if id_pwodwi == 1:
        if k >= 12: return 4500 * (k // 12) + (750 * (k % 12))
        if k >= 6: return 2500
        if k >= 3: return 1500
        return 750 * k
        
    # 2. Parfum Lattafa
    elif id_pwodwi == 2:
        if k >= 12: return 8000
        if k >= 3: return 2500
        return 1250 * k
        
    # 3. Montre Elegance
    if id_pwodwi == 3:
        if k >= 12: return 9000
        if k >= 3: return 2500
        if k >= 2: return 1700
        return 900 * k
        
    # 4. Kneia Backup
    elif id_pwodwi == 4:
        if k >= 3: return 4500
        if k >= 2: return 3250
        return 1750 * k
        
    # 5. Sandales (Pa vann pa grenn - Min 3)
    elif id_pwodwi == 5:
        if k >= 12: return 5500
        return 1750  # Pri pou 3 a
        
    # 6. Valise (Pa vann pa grenn - Min 3)
    elif id_pwodwi == 6:
        if k >= 3: return 2500
        return 2500  # Pri pou 3 a
        
    return 0

@app.route('/')
def home():
    # Lis tout pwodwi yo ak estati disponiblite yo
    liste_produits = [
        {
            "id": 1, "nom": "T-shirt Simple", "pri": " 1 pou 750 HTG", 
            "promo": "3 pou 1500 HTG | 6 pou 2500 HTG | 12 pou 4500 HTG", 
            "images": ["t-shirt simple (1).jpg", "t-shirt simple (2).jpg"], 
            "disponible": True
        },
        {
            "id": 2, "nom": "Parfum Lattafa", "pri": "1 pou 1250 HTG", 
            "promo": "3 pou 2500 HTG | 12 pou 8000 HTG", 
            "images": ["lattafa.jpg", "lattafa (1).jpg"], 
            "disponible": False  # FINI
        },
        {
            "id": 3, "nom": "Montre Elegance", "pri": " 1 pou 900 HTG", 
            "promo": "2 pou 1700 HTG | 3 pou 2500 HTG | 12 pou 9000 HTG", 
            "images": ["Montre.jpg"], 
            "disponible": True
        },
        {
            "id": 4, "nom": "Kneia Backup", "pri": " 1 pou 1750 HTG", 
            "promo": "2 pou 3250 HTG | 3 pou 4500 HTG", 
            "images": ["kneia backup.jpg"], 
            "disponible": True
        },
        {
            "id": 5, "nom": "Sandales Collection", "pri": "1750 HTG pou 3", 
            "promo": "3 pou 1750 HTG | 12 pou 5500 HTG", 
            "images": ["Sandales.jpg", "sandales f.jpg"], 
            "disponible": False  # FINI
        },
        {
            "id": 6, "nom": "Valise Élégance", "pri": "2500 HTG pou 3", 
            "promo": "6 pou 4500 HTG | 12 pou 8000 HTG", 
            "images": ["sac.jpg", "sac1.jpg", "sac2.jpg", "sac3.png"], 
            "disponible": True
        }
    ]
    return render_template('index.html', produits=liste_produits)

@app.route('/commander/<int:id>')
def commander(id):
    dokiman_pwodwi = {
        1: {"id": 1, "nom": "T-shirt Simple", "limit": 12, "min": 1},
        2: {"id": 2, "nom": "Parfum Lattafa", "limit": 12, "min": 1},
        3: {"id": 3, "nom": "Montre Elegance", "limit": 12, "min": 1},
        4: {"id": 4, "nom": "Kneia Backup", "limit": 3, "min": 1},
        5: {"id": 5, "nom": "Sandales Collection", "limit": 12, "min": 3},
        # Valiz la kounye a limite a 3 sèlman (min ak limit se 3)
        6: {"id": 6, "nom": "Valise Élégance", "limit": 3, "min": 3} 
    }
    pwodwi = dokiman_pwodwi.get(id)
    return render_template('choisir_kantite.html', pwodwi=pwodwi)

@app.route('/paiement', methods=['POST'])
def paiement():
    id_pwodwi = int(request.form.get('id'))
    kantite = int(request.form.get('kantite'))
    metode = request.form.get('metode')
    
    pri_final = kalkile_pri(id_pwodwi, kantite)
    
    if metode == 'moncash':
        return render_template('paiement_moncash.html', prix=f"{pri_final} HTG", kantite=kantite)
    else:
        return render_template('paiement_natcash.html', prix=f"{pri_final} HTG", kantite=kantite)

if __name__ == '__main__':
    app.run(debug=True)
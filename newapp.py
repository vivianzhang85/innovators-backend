from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'
CORS(app)

# Define shopping areas mapping
SHOPPING_AREAS = {
    'sarabeths': {
        'name': 'Columbus Circle',
        'area': 'Upper West Side',
        'description': 'Luxury shopping in the heart of Manhattan',
        'stores': ['Tiffany & Co.', 'Saks Fifth Avenue', 'Whole Foods', 'Various Boutiques']
    },
    'jacks': {
        'name': 'SoHo Shopping District', 
        'area': 'SoHo',
        'description': 'Trendy boutiques and designer flagship stores',
        'stores': ['Chanel', 'Prada', 'Apple Store', 'Art Galleries']
    },
    'ess': {
        'name': 'Fifth Avenue',
        'area': 'Midtown East',
        'description': 'World-famous luxury shopping corridor', 
        'stores': ['Bergdorf Goodman', 'Cartier', 'Van Cleef & Arpels', 'Harry Winston']
    },
    'shuka': {
        'name': 'East Village Boutiques',
        'area': 'East Village', 
        'description': 'Unique vintage shops and independent designers',
        'stores': ['Vintage Shops', 'Record Stores', 'Artisan Boutiques', 'Local Designers']
    }
}

@app.route('/')
def home():
    return redirect(url_for('breakfast'))

@app.route('/new-york/breakfast/')
def breakfast():
    return render_template('breakfast.html')

# NEW ROUTE: Handle breakfast completion and redirect to shopping
@app.route('/complete-breakfast', methods=['POST'])
def complete_breakfast():
    breakfast_spot = request.form.get('breakfast_spot')
    if breakfast_spot in SHOPPING_AREAS:
        session['selected_breakfast'] = breakfast_spot
        session['shopping_area'] = SHOPPING_AREAS[breakfast_spot]
        return redirect(url_for('shopping'))
    return redirect(url_for('breakfast'))

@app.route('/new-york/shopping/')
def shopping():
    shopping_data = session.get('shopping_area', SHOPPING_AREAS['sarabeths'])
    breakfast_spot = session.get('selected_breakfast', 'sarabeths')
    return render_template('shopping.html', shopping_area=shopping_data, breakfast_spot=breakfast_spot)

@app.route('/api/post-outfit', methods=['POST'])
def post_outfit():
    data = request.get_json()
    print("Outfit data received:", data)
    return {'success': True, 'message': 'Outfit posted successfully!'}

if __name__ == '__main__':
    app.run(debug=True, port=5002)
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_currency():
    data = request.get_json()

    if 'amount_inr' in data:
        amount_inr = float(data['amount_inr'])
        # Assuming 1 INR = 0.014 USD (for example)
        amount_usd = amount_inr * 0.014

        return jsonify({'amount_usd': amount_usd})
    else:
        return jsonify({'error': 'Amount in INR not provided'})
    
if __name__ == ('__main__'):
    app.run(debug=True)
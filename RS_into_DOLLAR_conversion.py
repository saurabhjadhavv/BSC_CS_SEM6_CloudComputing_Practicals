from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods =['POST'])

def convert():
    
    req_data = request.get_json()    
    
    if 'amount' not in req_data:
        return jsonify({'error': 'Amount not provided'}), 400
    
    amount_in_rupees = req_data['amount']
    
    usd_conversion_rate = 0.014
    
    converted_amount = amount_in_rupees * usd_conversion_rate
    
    return jsonify({'converted_amount': converted_amount}), 200

if __name__ == "__main__":
    app.run(debug=True)
    
# run the code 
#add thunder client and add new request then 
# select POST add
# link from the terminal ex : like - http://127.0.0.1:5000/convert
# make sure to add the JSON format like
# { "amount": 12 } inside the body
# then click on the SEND 

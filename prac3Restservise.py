from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample Data
data = [
    {
        'id': 1, 
        'Name': 'Anshu Tiwari'
    },
    {
        'id': 2, 
        'Name': 'Saurabh Jadhav'
    },
    {
        'id': 3, 
        'Name': 'Vishal More'
    },
    {
        'id': 4, 
        'Name': 'Rohan Pandey'
    },
]

# EndPoint to get all data
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({'data': data})

# EndPoint to get a specific user by ID
@app.route('/data/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in data if user['id'] == user_id), None)

    if user:
        return jsonify({'user': user})
    else:
        return jsonify({'message': 'User not found'}), 
    
    
@app.route('/data', methods=['POST'])
def add_user():
    new_user = {'id':len(data) + 1, 'Name':request.json['Name']}

    data.append(new_user)

    return jsonify({'message':'user added succesfully', 'user': new_user}), 201

if __name__ == "__main__":
    app.run(debug=True)

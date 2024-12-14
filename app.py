from flask import Flask, jsonify

app = Flask(__name__)

# Define a simple route
@app.route('/')
def home():
    return jsonify({"message": "Hello, World! Welcome to Flask on localhost:8080!. Is this thing working?"})

# Another example route
@app.route('/api/data')
def api_data():
    return jsonify({"data": [1, 2, 3, 4, 5]})

if __name__ == '__main__':
    # Run the Flask app on localhost at port 8080
    app.run(host='0.0.0.0', port=8080, debug=True)

from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/fetch-response', methods=['POST'])
@cross_origin()
def fetch_response():
    
    # Get the email and password from the request
    email = request.json.get('emailid')
    password = request.json.get('password')
    
    

    # Call the ai_responder.py script and capture its output
    result = subprocess.run(['python', 'ai_responder.py', email, password], capture_output=True, text=True)
    # Assuming the script prints the response
    response = result.stdout.strip()
    print(response)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

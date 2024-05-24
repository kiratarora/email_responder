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
    notes = request.json.get('notes')
    
    

    # Call the ai_responder.py script and capture its output
    result = subprocess.run(['python', 'ai_responder.py', email, password, notes], capture_output=True, text=True)
    # Assuming the script prints the response
    response = result.stdout.strip()
    
    
    return jsonify({'response': response})
@app.route('/generate-recipe', methods=['POST'])
def generate_recipe():
    data = request.get_json()
    ingredients = data.get('ingredients')
    dietary_restrictions = data.get('dietaryRestrictions')
    
    # Your logic to generate a recipe based on the ingredients and dietary restrictions
    result = subprocess.run(['python', 'ai_recipe_generator.py', ingredients, dietary_restrictions], capture_output=True, text=True)
    # Assuming the script prints the response
    response = result.stdout.strip()
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask, request, jsonify

app = Flask(__name__)

# Helper function to validate input data
def validate_json_input(data):
    if not isinstance(data, list):
        return False, "Input should be a list."
    for item in data:
        if not isinstance(item, str):
            return False, "All items in the list should be strings."
    return True, ""

# POST method to handle incoming JSON data
@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        # Extract data from the request
        data = request.json.get('data', [])
        
        # Validate input
        is_valid, message = validate_json_input(data)
        if not is_valid:
            return jsonify({"is_success": False, "error": message}), 400

        # Separate numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]

        # Find the highest lowercase alphabet
        lower_alphabets = [item for item in alphabets if item.islower()]
        highest_lowercase = max(lower_alphabets) if lower_alphabets else ""

        # Build the response
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with dynamic user data
            "email": "john@xyz.com",         # Replace with dynamic email
            "roll_number": "ABCD123",        # Replace with dynamic roll number
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

# GET method to return the operation code
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)

import functions_framework
import json
from datetime import datetime



@functions_framework.http
def hello_world(request):
    """HTTP Cloud Function that responds with 'Hello, World!'."""
    return 'Hello, World!'

@functions_framework.http
def echo_request(request):
    """HTTP Cloud Function that echoes back the request data."""
    return f"You sent: {request.get_data(as_text=True)}"

@functions_framework.http
def get_current_time(request):
    """HTTP Cloud Function that returns the current timestamp."""
    return {
        'timestamp': datetime.now().isoformat(),
        'message': 'Current server time'
    }

@functions_framework.http
def add_numbers(request):
    """HTTP Cloud Function that adds two numbers from query parameters."""
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = a + b
        return json.dumps({'a': a, 'b': b, 'sum': result})
    except Exception as e:
        return json.dumps({'error': str(e)}), 400

@functions_framework.http
def process_json(request):
    """HTTP Cloud Function that processes JSON request body."""
    try:
        data = request.get_json()
        if not data:
            return json.dumps({'error': 'No JSON data provided'}), 400
        
        # Process: add a computed field
        data['processed_at'] = datetime.now().isoformat()
        data['item_count'] = len(data)
        
        return json.dumps(data)
    except Exception as e:
        return json.dumps({'error': str(e)}), 400

@functions_framework.http
def greet_user(request):
    """HTTP Cloud Function that greets a user by name."""
    name = request.args.get('name', 'Guest')
    greeting = f"Hello, {name}! Welcome to Cloud Functions."
    return {'greeting': greeting, 'name': name}
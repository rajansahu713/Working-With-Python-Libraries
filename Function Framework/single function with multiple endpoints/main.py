import functions_framework
import json
from datetime import datetime


@functions_framework.http
def multi_endpoint_handler(request):
    """
    Cloud Function that handles multiple endpoints in a single function.
    Routes requests based on path and method.
    
    Supported endpoints:
    - GET  /api/hello          -> hello endpoint
    - POST /api/add            -> add two numbers
    - GET  /api/time           -> current time
    - POST /api/greet          -> greet user
    - GET  /api/status         -> status check
    - POST /api/calculate      -> perform calculation
    - GET  /api/users          -> get users list
    """
    try:
        # Get request path and method
        path = request.path
        method = request.method
        
        # Route to appropriate handler
        if path == '/api/hello' and method == 'GET':
            return handle_hello()
        
        elif path == '/api/add' and method == 'POST':
            return handle_add(request)
        
        elif path == '/api/time' and method == 'GET':
            return handle_time()
        
        elif path == '/api/greet' and method == 'POST':
            return handle_greet(request)
        
        elif path == '/api/status' and method == 'GET':
            return handle_status()
        
        elif path == '/api/calculate' and method == 'POST':
            return handle_calculate(request)
        
        elif path == '/api/users' and method == 'GET':
            return handle_users()
        
        elif path == '/api/echo' and method == 'POST':
            return handle_echo(request)
        
        else:
            # Default: show available endpoints
            return handle_not_found(path, method)
    
    except Exception as e:
        return json.dumps({'error': str(e), 'status': 'error'}), 500


# ============ ENDPOINT HANDLERS ============

def handle_hello():
    """GET /api/hello"""
    return json.dumps({
        'message': 'Hello! This is a multi-endpoint cloud function',
        'endpoint': '/api/hello',
        'method': 'GET'
    })


def handle_add(request):
    """POST /api/add - Add two numbers"""
    try:
        data = request.get_json()
        
        if not data or 'a' not in data or 'b' not in data:
            return json.dumps({
                'error': 'Missing parameters: a and b required',
                'expected': {'a': 5, 'b': 3}
            }), 400
        
        a = float(data['a'])
        b = float(data['b'])
        result = a + b
        
        # return json.dumps({
        #     'endpoint': '/api/add',
        #     'a': a,
        #     'b': b,
        #     'result': result,
        #     'status': 'success'
        # })
        return {
            'endpoint': '/api/add',
            'a': a,
            'b': b,
            'result': result,
            'status': 'success'
        }
    except Exception as e:
        return json.dumps({'error': str(e)}), 400


def handle_time():
    """GET /api/time - Get current time"""
    return json.dumps({
        'endpoint': '/api/time',
        'timestamp': datetime.now().isoformat(),
        'unix_time': int(datetime.now().timestamp()),
        'message': 'Current server time'
    })


def handle_greet(request):
    """POST /api/greet - Greet a user"""
    try:
        data = request.get_json() or {}
        name = data.get('name', 'Guest')
        
        return json.dumps({
            'endpoint': '/api/greet',
            'greeting': f'Hello, {name}! Welcome to multi-endpoint cloud function',
            'name': name,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return json.dumps({'error': str(e)}), 400


def handle_status():
    """GET /api/status - Get function status"""
    return json.dumps({
        'endpoint': '/api/status',
        'status': 'running',
        'version': '1.0.0',
        'uptime': 'active',
        'timestamp': datetime.now().isoformat()
    })


def handle_calculate(request):
    """POST /api/calculate - Perform calculation"""
    try:
        data = request.get_json()
        
        if not data or 'operation' not in data:
            return json.dumps({
                'error': 'Missing parameters',
                'expected': {
                    'operation': 'add|subtract|multiply|divide',
                    'a': 10,
                    'b': 5
                }
            }), 400
        
        operation = data.get('operation', '').lower()
        a = float(data.get('a', 0))
        b = float(data.get('b', 0))
        
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'multiply':
            result = a * b
        elif operation == 'divide':
            if b == 0:
                return json.dumps({'error': 'Division by zero'}), 400
            result = a / b
        else:
            return json.dumps({
                'error': f'Unknown operation: {operation}',
                'supported': ['add', 'subtract', 'multiply', 'divide']
            }), 400
        
        return json.dumps({
            'endpoint': '/api/calculate',
            'operation': operation,
            'a': a,
            'b': b,
            'result': result,
            'status': 'success'
        })
    except Exception as e:
        return json.dumps({'error': str(e)}), 400


def handle_users():
    """GET /api/users - Get list of users"""
    users = [
        {'id': 1, 'name': 'Alice', 'role': 'admin'},
        {'id': 2, 'name': 'Bob', 'role': 'user'},
        {'id': 3, 'name': 'Charlie', 'role': 'user'},
        {'id': 4, 'name': 'Diana', 'role': 'moderator'}
    ]
    
    return json.dumps({
        'endpoint': '/api/users',
        'count': len(users),
        'users': users,
        'timestamp': datetime.now().isoformat()
    })


def handle_echo(request):
    """POST /api/echo - Echo back the request data"""
    try:
        data = request.get_json() or request.get_data(as_text=True)
        
        return json.dumps({
            'endpoint': '/api/echo',
            'received': data,
            'type': type(data).__name__,
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return json.dumps({'error': str(e)}), 400


def handle_not_found(path, method):
    """Handle unknown endpoints"""
    available_endpoints = [
        {'method': 'GET', 'path': '/api/hello', 'description': 'Hello endpoint'},
        {'method': 'POST', 'path': '/api/add', 'description': 'Add two numbers', 'params': {'a': 'number', 'b': 'number'}},
        {'method': 'GET', 'path': '/api/time', 'description': 'Get current time'},
        {'method': 'POST', 'path': '/api/greet', 'description': 'Greet a user', 'params': {'name': 'string'}},
        {'method': 'GET', 'path': '/api/status', 'description': 'Get function status'},
        {'method': 'POST', 'path': '/api/calculate', 'description': 'Perform calculation', 'params': {'operation': 'string', 'a': 'number', 'b': 'number'}},
        {'method': 'GET', 'path': '/api/users', 'description': 'Get users list'},
        {'method': 'POST', 'path': '/api/echo', 'description': 'Echo back request'}
    ]
    
    return json.dumps({
        'error': f'Endpoint not found: {method} {path}',
        'status': 404,
        'available_endpoints': available_endpoints
    }), 404

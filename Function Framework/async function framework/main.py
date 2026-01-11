import functions_framework
import json
import asyncio
from datetime import datetime
import aiohttp


@functions_framework.http
async def async_hello_world(request):
    """Async HTTP Cloud Function that responds with 'Hello, World!'."""
    await asyncio.sleep(0.1)  # Simulate async work
    return 'Hello, Async World!'


@functions_framework.http
async def async_echo_request(request):
    """Async HTTP Cloud Function that echoes back the request data."""
    data = request.get_data(as_text=True)
    await asyncio.sleep(0.05)  # Simulate async processing
    return f"You sent (async): {data}"


@functions_framework.http
async def async_get_current_time(request):
    """Async HTTP Cloud Function that returns the current timestamp."""
    await asyncio.sleep(0.1)  # Simulate async operation
    return {
        'timestamp': datetime.now().isoformat(),
        'message': 'Current server time (async)',
        'timezone': 'UTC'
    }


@functions_framework.http
async def async_add_numbers(request):
    """Async HTTP Cloud Function that adds two numbers with delay simulation."""
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        
        # Simulate async computation
        await asyncio.sleep(0.2)
        
        result = a + b
        return json.dumps({
            'a': a,
            'b': b,
            'sum': result,
            'async': True,
            'processed_at': datetime.now().isoformat()
        })
    except Exception as e:
        return json.dumps({'error': str(e)}), 400


@functions_framework.http
async def async_process_json(request):
    """Async HTTP Cloud Function that processes JSON request body concurrently."""
    try:
        data = request.get_json()
        if not data:
            return json.dumps({'error': 'No JSON data provided'}), 400
        
        # Simulate async processing tasks
        async def process_item(item, delay):
            await asyncio.sleep(delay)
            return item.upper() if isinstance(item, str) else item
        
        # Process multiple fields concurrently
        tasks = []
        if isinstance(data, dict):
            for key in data:
                tasks.append(process_item(str(key), 0.1))
        
        if tasks:
            await asyncio.gather(*tasks)
        
        # Add metadata
        data['processed_at'] = datetime.now().isoformat()
        data['item_count'] = len(data) if isinstance(data, dict) else 1
        data['async_processing'] = True
        
        return json.dumps(data)
    except Exception as e:
        return json.dumps({'error': str(e)}), 400


@functions_framework.http
async def async_greet_user(request):
    """Async HTTP Cloud Function that greets a user with simulated delay."""
    name = request.args.get('name', 'Guest')
    
    # Simulate async greeting generation (e.g., fetching user data)
    await asyncio.sleep(0.15)
    
    greeting = f"Hello, {name}! Welcome to Async Cloud Functions."
    return {
        'greeting': greeting,
        'name': name,
        'timestamp': datetime.now().isoformat(),
        'async': True
    }


@functions_framework.http
async def async_fetch_multiple_urls(request):
    """Async HTTP Cloud Function that fetches multiple URLs concurrently."""
    urls = request.args.getlist('url')
    
    if not urls:
        return json.dumps({
            'error': 'No URLs provided',
            'usage': '/async_fetch_multiple_urls?url=http://example.com&url=http://google.com'
        }), 400
    
    async def fetch_url(session, url):
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
                return {
                    'url': url,
                    'status': response.status,
                    'content_length': len(await response.text())
                }
        except Exception as e:
            return {
                'url': url,
                'error': str(e)
            }
    
    try:
        async with aiohttp.ClientSession() as session:
            tasks = [fetch_url(session, url) for url in urls]
            results = await asyncio.gather(*tasks)
        
        return json.dumps({
            'results': results,
            'total_urls': len(urls),
            'fetched_at': datetime.now().isoformat()
        })
    except Exception as e:
        return json.dumps({'error': str(e)}), 400


@functions_framework.http
async def async_concurrent_tasks(request):
    """Async HTTP Cloud Function that runs multiple concurrent tasks."""
    num_tasks = int(request.args.get('tasks', 5))
    
    if num_tasks > 20:
        return json.dumps({'error': 'Maximum 20 concurrent tasks allowed'}), 400
    
    async def simulate_work(task_id, duration=0.2):
        start = datetime.now()
        await asyncio.sleep(duration)
        end = datetime.now()
        return {
            'task_id': task_id,
            'status': 'completed',
            'duration': (end - start).total_seconds()
        }
    
    try:
        # Run multiple tasks concurrently
        tasks = [simulate_work(i) for i in range(num_tasks)]
        results = await asyncio.gather(*tasks)
        
        return json.dumps({
            'total_tasks': num_tasks,
            'results': results,
            'completed_at': datetime.now().isoformat()
        })
    except Exception as e:
        return json.dumps({'error': str(e)}), 400


@functions_framework.http
async def async_delayed_response(request):
    """Async HTTP Cloud Function with progressive delays."""
    delay = float(request.args.get('delay', 1.0))
    
    if delay > 10:
        return json.dumps({'error': 'Delay cannot exceed 10 seconds'}), 400
    
    start_time = datetime.now()
    await asyncio.sleep(delay)
    end_time = datetime.now()
    
    return {
        'requested_delay': delay,
        'actual_delay': (end_time - start_time).total_seconds(),
        'started_at': start_time.isoformat(),
        'completed_at': end_time.isoformat()
    }

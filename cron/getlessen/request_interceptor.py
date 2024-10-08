import gzip
from io import BytesIO

def intercept_last_request(driver, url_contains):
    """Intercepts and returns the last network request that matches the given URL."""
    last_request = None
    for request in driver.requests:
        if request.response and url_contains in request.url:
            last_request = request

    if last_request:
        # Check for gzip encoding in response headers
        if 'gzip' in last_request.response.headers.get('Content-Encoding', ''):
            compressed_data = BytesIO(last_request.response.body)
            with gzip.GzipFile(fileobj=compressed_data) as f:
                decompressed_data = f.read().decode('utf-8')
            return decompressed_data
        else:
            return last_request.response.body.decode('utf-8')
    return None

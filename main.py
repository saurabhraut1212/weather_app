import webbrowser
from http.server import HTTPServer
from src.server import WeatherAppHandler

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, WeatherAppHandler)
    print(f"Server running on port {port}")
    webbrowser.open(f'http://localhost:{port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
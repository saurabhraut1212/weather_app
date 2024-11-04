from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse
from html import escape
import os
from src.services.weather_service import WeatherService
from src.utils.template_engine import TemplateEngine

class WeatherAppHandler(SimpleHTTPRequestHandler):
    def render_template(self, template_name, **context):
        template_path = os.path.join('src/templates', template_name)
        return TemplateEngine.render(template_path, **context)

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            html = self.render_template('home.html')
            self.wfile.write(html.encode())
            
        elif self.path.startswith('/weather'):
            query = urllib.parse.urlparse(self.path).query
            params = urllib.parse.parse_qs(query)
            city = params.get('city', [''])[0]
            
            if city:
                try:
                    weather_service = WeatherService()
                    weather_data = weather_service.get_weather(city)
                    
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    
                    html = self.render_template(
                        'weather.html',
                        city=escape(city),
                        weather=weather_data
                    )
                    self.wfile.write(html.encode())
                    
                except Exception as e:
                    self.send_error(500, f"Error: {str(e)}")
            else:
                self.send_error(400, "City parameter is required")
        else:
            self.send_error(404, "Page not found")
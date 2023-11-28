from flask import Flask
from config import config
from flask_cors import CORS
# import source routes
from routes import User

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}}, supports_credentials=True)

@app.route('/api/users', methods=['OPTIONS'])
def options():
    return {'Allow': 'GET, POST'}, 200

def page_not_found(error):
    return "<h1> Pagina de NOVA no econtrada </h1>",404

if __name__ == '__main__':
    #app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(User.main, url_prefix='/api/users')

    #Error handlers
    #app.register_error_handler(404,page_not_found)
    app.run()
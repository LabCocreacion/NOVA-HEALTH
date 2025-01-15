from flask import Flask, Response
from config import config
from flask_cors import CORS
# import source routes
from routes import User

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}}, supports_credentials=True)

@app.route('/api/users', methods=['OPTIONS'])
def options():
    return Response({'Allow': 'GET, POST'}, status=200, mimetype='application/json; charset=utf-8')

def page_not_found(error):
    return "<h1> Pagina no econtrada </h1>",404

if __name__ == '__main__':
    #app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(User.main, url_prefix='/api/users')

    #Error handlers
    #app.register_error_handler(404,page_not_found)
    app.run(debug=True)
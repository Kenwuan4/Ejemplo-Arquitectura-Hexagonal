from flask import Flask, jsonify, request, Response
import services.UserService as UserService
import services.RickMortyAPI_Service as RickService


app = Flask(__name__)


@app.route('/personas', methods=['POST'])
def create_persona():
    # Receiving Data
    data = request.get_json(force=True)
    result = UserService.graphQuery(data)
    return jsonify(result)


@app.route('/personas/rickapi/<page>', methods=['GET'])
def get_rick(page):
    response = RickService.get_caracter(page)
    return response


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(debug=True, port=3000)

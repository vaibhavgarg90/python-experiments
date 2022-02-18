from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/health', methods=['GET'])
def health():
    response = {
        'status': 'running'
    }
    return jsonify(response), 200


@app.route('/test_get', methods=['GET'])
def test_get():
    response = {
        'success': True
    }
    return jsonify(response), 200


@app.route('/test_get_with_query_param', methods=['GET'])
def test_get_with_query_param():
    query_params = request.args
    response = {
        'success': True,
        'query_params': query_params
    }
    return jsonify(response), 200


@app.route('/test_get_with_path_param/<path_param>', methods=['GET'])
def test_get_with_path_param(path_param):
    response = {
        'success': True,
        'path_param': path_param
    }
    return jsonify(response), 200


@app.route('/test_post', methods=['POST'])
def test_post():
    data = request.get_json()
    response = {
        'success': True,
        'data': data
    }
    return jsonify(response), 200


@app.route('/test_put', methods=['PUT'])
def test_put():
    data = request.get_json()
    response = {
        'success': True,
        'data': data
    }
    return jsonify(response), 200


@app.route('/test_delete', methods=['DELETE'])
def test_delete():
    data = request.get_json()
    response = {
        'success': True,
        'data': data
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)

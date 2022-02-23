import json

from bson import ObjectId
from flask import abort, Flask, jsonify, render_template, request
from time import time
from werkzeug.utils import secure_filename

from service import user_service
from util.file_util import is_file_extension_allowed, save
from util.json_util import JSONEncoder

MESSAGE_TEMPLATE = 'message.html'

app = Flask(__name__)
app.json_encoder = JSONEncoder


@app.errorhandler(400)
def bad_request(error):
    return render_template(MESSAGE_TEMPLATE, message=str(error)), 400


@app.errorhandler(404)
def page_not_found(error):
    return render_template(MESSAGE_TEMPLATE, message=str(error)), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template(MESSAGE_TEMPLATE, message=str(error)), 500


@app.route('/health', methods=['GET'])
def health():
    response = {
        'status': 'running'
    }
    return jsonify(response), 200


@app.route('/user', methods=['POST'])
def insert_user():
    try:
        data = request.get_json()
        if "insert_time" not in data:
            data["insert_time"] = int(time())
        user_id = user_service.insert_user(data)
        user_db_data = user_service.get_user_by_id(user_id)
        return jsonify(user_db_data), 200
    except Exception as e:
        abort(500, str(e))


@app.route('/user/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    user_db_data = user_service.get_user_by_id(user_id)
    if not user_db_data:
        abort(404, f"User with id {user_id} not found")
    return jsonify(user_db_data), 200


@app.route('/users', methods=['GET'])
def list_users():
    query_params = request.args
    query = json.loads(query_params["query"])
    users = list(user_service.list_users(query))
    return jsonify(users), 200


@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    update_query = request.get_json()
    if "update_time" not in update_query:
        update_query["update_time"] = int(time())
    find_query = {"_id": ObjectId(user_id)}
    user_db_data = user_service.get_user_by_id(user_id)
    if not user_db_data:
        abort(404, f"User with id {user_id} not found")
    user_service.update_user(find_query, update_query)
    user_db_data = user_service.get_user_by_id(user_id)
    return jsonify(user_db_data), 200


@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    query = {"_id": ObjectId(user_id)}
    count = user_service.delete_user(query)
    if not count:
        abort(404, f"User with id {user_id} not found")
    return jsonify({"count": count}), 200


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        abort(400, f"File not uploaded")
    file = request.files['file']
    filename = file.filename
    if not filename:
        abort(400, f"File not uploaded")
    if not is_file_extension_allowed(filename):
        abort(400, f"File extension not supported")
    filename = secure_filename(file.filename)
    save(filename, file)
    return jsonify({"status": "success"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)

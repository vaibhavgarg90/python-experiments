import os

from util.env_util import ALLOWED_EXTENSIONS, FILE_UPLOAD_FOLDER


def is_file_extension_allowed(filename):
    return '.' in filename and '.' + filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save(filename, file):
    path = os.path.join(FILE_UPLOAD_FOLDER, filename)
    file.save(path)

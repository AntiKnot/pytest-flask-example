# test mock folder, upload twice, result same.
import os
import uuid

from flask import Blueprint
from flask import jsonify
from flask import request

bp_file = Blueprint('file', __name__, url_prefix='/file')

ALLOWED_EXCEL = ['xls', 'xlsx']
ALLOWED_IMAGES = ['png', 'jpg']
ALLOWED_DATA = ['csv', 'txt']
ALLOWED_EXTENSIONS = ALLOWED_EXCEL + ALLOWED_IMAGES + ALLOWED_DATA


def allowed_file(filename: str):
    file_extension = '.' in filename and filename.rsplit('.', 1)[1]
    return file_extension in ALLOWED_EXTENSIONS


def save_file(file, upload_folder):
    """
    :param file: request.files['file'] "Company.xls"
    :param upload_folder: string like "/tmp/company_info_collection"
    :return: filepath string "/tmp/company_info_collection" and uuid unique filename
    """
    # filename = secure_filename(file.filename)
    unique_filename = "uuid_filename"
    fp = os.path.join(upload_folder, unique_filename)
    file.save(fp)
    return fp, unique_filename


@bp_file.route('/upload', methods=["HEAD", 'POST'])
def upload():
    """
    :return: file path save in server, will replace by token for get basic info
    """
    if request.method == "POST":
        file = request.files["file"]
        if file and allowed_file(file.filename):
            _, unique_filename = save_file(file, upload_folder='tmp')
            return jsonify(fn=unique_filename)
        return jsonify(fn="")

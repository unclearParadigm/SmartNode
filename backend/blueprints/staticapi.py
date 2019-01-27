import os.path

from flask import Blueprint
from flask import render_template
from flask import send_from_directory

from backend.locator import get_frontend_root


staticapi = \
    Blueprint('static_api', __name__, template_folder='templates')


@staticapi.route('/', methods=['GET'])
def serve_frontend():
    return render_template('webui.html',
                           scripts=get_urls_for_frontend_resources(extension='.js'),
                           stylesheets=get_urls_for_frontend_resources(extension='.css'))


@staticapi.route('/static/<string:directory>/<path:filename>', methods=['GET'])
def serve_static_content(directory, filename):
    if directory == 'lib':
        directory = 'node_modules'

    return send_from_directory(os.path.join(get_frontend_root(), directory), filename)


def get_urls_for_frontend_resources(extension: str) -> list:
    for dirpath, dirnames, filenames in os.walk(get_frontend_root()):
        for filename in [f for f in filenames if f.endswith(extension)]:
            url = os.path.join('static', os.path.relpath(os.path.join(dirpath, filename), get_frontend_root()))
            if 'node_modules' not in dirpath:
                yield url

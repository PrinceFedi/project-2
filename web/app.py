"""
Fedi Aniefuna's Flask API.
"""
import configparser
import os

from flask import Flask, send_from_directory, abort

app = Flask(__name__)
docroot = "./pages"


@app.route("/<path:request>")
def hello(request):
    """
        This takes the arg from the flask route function, which is a decorator
        that tells the application which URL should call the associated function. From there we
        test the request to see if it has illegal characters or if it's an invalid or valid file from oru directory.

    Args:
        request: The request of the user

    """
    if '~' in request or '..' in request:
        abort(403)
    elif os.path.exists(f"{docroot}/{request}"):
        return send_from_directory(f"{docroot}", f'{request}'), 200
    else:
        abort(404)


@app.errorhandler(403)
def forbidden(e):
    """
        If a 403 error is triggered, this function will send a request to the 403.html file to report to the client
        that their request has a forbidden error


    """
    return send_from_directory(f'{docroot}', '403.html'), 403


@app.errorhandler(404)
def not_found(e):
    """
    If a 404 error is triggered, this function will send a request to the 404.html file to report to the client
        that the file requested is not found.

    """
    return send_from_directory(f'{docroot}', '404.html'), 404


def parse_config(config_paths):
    """
        This function checks if any  of the files we specify exist, and use the first one that does.

    Args:
        config_paths: A specific file given by our input

    Returns: The specified file

    """
    config_path = None
    for f in config_paths:
        if os.path.isfile(f):
            config_path = f
            break

    if config_path is None:
        raise RuntimeError("Configuration file not found!")

    configuration = configparser.ConfigParser()
    configuration.read(config_path)
    return configuration


my_config = parse_config(["credentials.ini", "default.ini"])
config_port = my_config["SERVER"]["PORT"]
debug_config = my_config["SERVER"]["DEBUG"]

if __name__ == "__main__":
    app.run(debug=bool(debug_config), host='0.0.0.0', port=int(config_port))

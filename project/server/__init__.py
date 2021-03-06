from server.main.views import main_blueprint
from flask import Flask, jsonify

import traceback  # error traceback
from werkzeug.exceptions import default_exceptions  # exception handling
from werkzeug.exceptions import HTTPException  # exception handling


def create_app():
    """
    Creation and initialization of Flask app with exception handling
    :return: app
    """

    # instantiate the app
    app = Flask(__name__, instance_relative_config=False)

    # set config
    app.config.from_object("server.config.Config")

    # register blueprints
    app.register_blueprint(main_blueprint)

    # exception handling
    @app.errorhandler(Exception)
    def handle_error(e):
        """
        Function for better exception handling
        :param e: exception
        :return: error message
        """

        # 400 for https error, 500 for internal error
        if isinstance(e, HTTPException):
            # status_code = e.code
            status_code = 400
        else:
            status_code = 500
        # prepare error message
        message = str(e)
        # stdout error traceback
        print(traceback.format_exc())
        # return response
        return jsonify(message=message, error_traceback=traceback.format_exc()), status_code

    for ex in default_exceptions:
        app.register_error_handler(ex, handle_error)

    return app

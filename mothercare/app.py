import os
import json
import jsonschema


from bottle import Bottle


def endpoints():

    app = Bottle()

    @app.route('/ping', method=['GET'])
    def ping():
        return {
            'service': 'sevasetu-mothercare',
            'description': 'Application for mothercare'
        }

    return app

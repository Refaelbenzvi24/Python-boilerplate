import json

from flask import Response
from flask_restful import Resource
from flask import request


class StatusResource(Resource):
    @staticmethod
    def get():
        response = {
            'status': 'OK'
        }
        return Response(json.dumps(response, default=str), content_type='application/json', status=200)

from flask import Blueprint
from flask_restful import Api

from resources import StatusResource

STATUS_BLUEPRINT = Blueprint("status", __name__)
Api(STATUS_BLUEPRINT).add_resource(StatusResource, '/status')

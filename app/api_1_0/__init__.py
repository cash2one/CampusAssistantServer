__author__ = 'EnvyLan'
from flask import Blueprint

api = Blueprint('api', __name__)

from .authentication import api
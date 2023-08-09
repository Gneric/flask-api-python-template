from flask_restful import Resource
from flask import request

from api.tools.handlers import handle_response
from api.services.userService import getToken
from api.validator.userValidation import validateUserGetToken

class getUser(Resource):
    def get(self):
        try:
            if request.content_type == None:
                return { 'error': 'Content Type error' }, 400

            usr = request.json.get('user', None)
            pwd = request.json.get('password', None)

            validateUser = validateUserGetToken(usr, pwd)
            if validateUser != None: return validateUser
            
            data = getToken(usr, pwd)
            return handle_response(200, 'Usuario Retornado', data)
        except Exception as err:
            return handle_response(400, err)
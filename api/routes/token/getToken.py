from flask_jwt_extended import create_access_token
from flask_restful import Resource
from flask import request

class getToken(Resource):
    def post(self):
        try:
            if request.content_type == None:
                return { 'error': 'Content Type error' }, 400

            usr = request.json.get('user', None)
            pwd = request.json.get('password', None)
            userInfo = request.json.get('userInfo', None)

            identity_token = { 'user': usr, 'user_info': userInfo }
            access_token = create_access_token(identity=str(identity_token))
            
            return { 'result': { 'usr': usr, 'access_token': access_token } }, 200
        except Exception as err:
            print('Error getToken : ', err)
            return { 'error': 'unkown error' }, 400
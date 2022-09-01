from flask import Flask, request
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended.utils import (
    create_refresh_token,
    decode_token
)
from flask_jwt_extended import (
    JWTManager,
    create_access_token
)

from datetime import datetime 
from os.path import exists

from constants import api_config



def createApp(__name__):

    app = Flask(__name__)
    app.config.from_object(api_config)
    jwt = JWTManager(app)
    CORS(app, expose_headers=["filename"], resources={r"*": {"origins": "*"}})

    @app.route("/api/refresh", methods=["POST"])
    def refresh():
        token = request.json.get('refreshToken', '')
        payload = decode_token(token)['sub']
        hasura_token = {}
        hasura_token["hasura_claims"] = decode_token(token)['hasura_claims']
        print(payload)
        if token == '':
            return { 'error': 'token no enviado' }, 401
        access_token = create_access_token(identity=payload, additional_claims=hasura_token)
        refresh_token = create_refresh_token(identity=payload, additional_claims=hasura_token)
        return { "accessToken" : access_token, "refreshToken": refresh_token }

    @jwt.token_verification_failed_loader
    def token_verification_failed_loader_callback(jwt_header, jwt_payload):
        response = { "error" : "token invalido" }, 401
        return response

    @jwt.invalid_token_loader
    def invalid_token_loader_callback(jwt_header):
        response = { "error" : "token invalido" }, 401
        return response

    @jwt.unauthorized_loader
    def unauthorized_loader_callback(jwt_header):
        response = { "error" : "token invalido" }, 401
        return response

    @jwt.expired_token_loader
    def expired_token_loader_callback(jwt_header, two):
        response = { "error" : "token expirado" }, 401
        return response

    @jwt.needs_fresh_token_loader
    def needs_fresh_token_loader(jwt_header):
        response = { "error" : "token invalido" }, 401
        return response

    @app.after_request
    def after_request(response):
        timestamp = str(datetime.now().strftime('[%Y-%b-%d %H:%M]'))
        day = str(datetime.now().strftime('%Y-%b-%d'))

        if not exists(f'./logs/{day}.txt'):
            open(f'./logs/{day}.txt', 'w')

        with open(f'./logs/{day}.txt','a') as f:
            f.write(f'{timestamp}, {request.remote_addr}, {request.method}, {request.scheme}, {request.full_path}, {response.status}' + '\n')

        return response

    @app.errorhandler(Exception)
    def exceptions(e):
        timestamp = str(datetime.now().strftime('[%Y-%b-%d %H:%M]'))
        day = str(datetime.now().strftime('%Y-%b-%d'))

        if not exists(f'./logs/{day}.txt'):
            open(f'./logs/{day}.txt', 'w')

        with open(f'./logs/{day}.txt','a') as f:
            f.write(f'{timestamp}, {request.remote_addr}, {request.method}, {request.scheme}, {request.full_path}, {e.status}' + '\n')

        return e.status_code

    api = Api(app)
    return app, api
    
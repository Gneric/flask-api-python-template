from app.createApp import createApp
from api.router.routes import Routes
from waitress import serve

app, api = createApp(__name__)
router = Routes()

api.add_resource(router._token, '/api/getToken')

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=3010, threads=8) # Solo para produccion
    app.run(host='0.0.0.0', port=3100, debug=True)
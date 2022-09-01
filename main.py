from utils.createApp import createApp
from api.routes.routesInterface import Routes
from waitress import serve

app, api = createApp(__name__)
rts = Routes()

# Login
api.add_resource(rts._token, '/api/getToken')

# Ejemplo
# api.add_resource(rts._alerts, '/api/protected/alerts/getAlerts')

if __name__ == "__main__":
    #serve(app, host="0.0.0.0", port=3010, threads=8) # Solo para produccion
    app.run(host='0.0.0.0', port=3100, debug=True)
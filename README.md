# Template de Python api
> Librerias principales: flask, flask_jwt_extended, flask_restful, flask_cors
## Importante llenar los siguientes datos
api/config
- mySQLConfig
- SQLServerConfig

api/constants
- api_config
## Creando ENV e instalando librerias
- Comando para crear el virtual enviroment
py -m venv env
- Abrir el env
.\env\Scripts\activate
- Instalar las librerias
pip install -r requirements.txt
Configurar los previos archivos
## Para ejecutar
main.py con app.run para **Desarrollo**
main.py con waitress para **Produccion**
from api.tools.handlers import handle_response

def validateUserGetToken(usr, pwd):
    if (usr != 'admin' or pwd != '123456' ):
      return handle_response(400, 'Error en las credenciales del usuario')
    else: return None
from flask_jwt_extended import create_access_token

def getToken(usr, pwd):
    try:
      identity_token = { 'user': usr, 'pwd': pwd }
      access_token = create_access_token(identity=str(identity_token))
      data = { 'user': usr, 'access_token': access_token }
      return data
    except Exception as e:
      print(e)
      return e
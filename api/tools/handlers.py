
def handle_response(status_code, message, data = {}):
  return { 'result': message, 'data': data }, status_code
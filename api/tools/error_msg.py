class ResponseError(Exception):
	def __init__(self, message = '', responseCode = 400):
		self.responseCode = responseCode
		self.error = { "error": message }

		super().__init__(message)
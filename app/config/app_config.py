from datetime import timedelta

# ADD SECRET KEY
SECRET_KEY = "8TT!Ya=jFXq?K[}ft-miExY{P{y!Q<"
JWT_COOKIE_SECURE = False
JWT_TOKEN_LOCATION = ["headers"]
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=48)
PROPAGATE_EXCEPTIONS = True
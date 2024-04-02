from itsdangerous import URLSafeTimedSerializer
from flask import current_app


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    return serializer.dumps(email, salt=current_app.config["SECURITY_PASSWORD_SALT"])

def confirm_token(token, expiration=360000):
    serializer = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
    salt = current_app.config["SECURITY_PASSWORD_SALT"]
    try:
        email = serializer.loads(
            token,
            salt=salt,
            max_age=expiration
        )
    except:
        return False
    return email
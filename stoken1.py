from itsdangerous import URLSafeTimedSerializer
from key import secret_key
def token(data1,salt):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.dumps(data1,salt=salt)
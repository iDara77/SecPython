from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os

dir = os.path.dirname(os.path.realpath(__file__))
priv = rsa.generate_private_key(public_exponent=65537, key_size=2048)
with open(f"{dir}/private.key","wb") as f:
    f.write(priv.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(b'mypassword')
    ))
with open(f"{dir}/public.key","wb") as f:
    f.write(priv.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1,
    ))

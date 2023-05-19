from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os

dir = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir}/public.key", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read()
    )
with open(f"{dir}/test.txt", "rb") as f:
    encrypted = public_key.encrypt(
        f.read(), 
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
with open(f"{dir}/test.txt.enc", "wb") as f:
    f.write(encrypted)
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os

MDP = b"mypassword"
dir = os.path.dirname(os.path.realpath(__file__))

with open(f"{dir}/private.key", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=MDP
    )
with open(f"{dir}/test.txt.enc", "rb") as f:
    decrypted = private_key.decrypt(
        f.read(), 
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

print(decrypted)
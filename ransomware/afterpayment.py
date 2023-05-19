import os, shutil, errno
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

MDP = b"mypassword"

def load_private_key(dir):
    with open(f"{dir}/private.key", "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=MDP
        )
    return private_key

def decrypt_file(file, private_key):
    with open(file, "rb") as f:
        decrypted = private_key.decrypt(
            f.read(), 
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        
    with open(file, "wb") as f:
        f.write(decrypted)
        
def dec_files(dir2,filenames, private_key):
    for filename in filenames:
        decrypt_file(f"{dir2}/{filename}", private_key)
            
def copyall(src, dst):
    try:
        shutil.copytree(src, dst, dirs_exist_ok=True)
    except OSError as exc: # python >2.5
        if exc.errno in (errno.ENOTDIR, errno.EINVAL):
            shutil.copy(src, dst)
        else: raise

def main():

    private_key = load_private_key(dir)
    
    dir = os.path.dirname(os.path.realpath(__file__)) + "/files_to_hack"
    for (dirpath, dirnames, filenames) in os.walk(dir):
        dec_files(dirpath,filenames,private_key)
        
if __name__ == "__main__":
    main()
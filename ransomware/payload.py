import os, shutil, errno
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

def load_public_key(dir):
    with open(f"{dir}/public.key", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read()
        )
    return public_key

def encrypt_file(file, public_key):
    with open(file, "rb") as f:
        encrypted = public_key.encrypt(
            f.read(), 
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    with open(file, "wb") as f:
        f.write(encrypted)
        
def enc_files(dir2,filenames, public_key):
    for filename in filenames:
        encrypt_file(f"{dir2}/{filename}", public_key)
            
def copyall(src, dst):
    try:
        shutil.copytree(src, dst, dirs_exist_ok=True)
    except OSError as exc: # python >2.5
        if exc.errno in (errno.ENOTDIR, errno.EINVAL):
            shutil.copy(src, dst)
        else: raise

def main():
    dir = os.path.dirname(os.path.realpath(__file__))
    public_key = load_public_key(dir)
        
    copyall(f"{dir}/files",f"{dir}/files_to_hack")
    
    dir = os.path.dirname(os.path.realpath(__file__)) + "/files_to_hack"
    for (dirpath, dirnames, filenames) in os.walk(dir):
        enc_files(dirpath,filenames,public_key)
        
if __name__ == "__main__":
    main()
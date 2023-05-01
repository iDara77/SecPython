import crypt
import os

dir = os.path.dirname(os.path.realpath(__file__))

def testPass(passwd):
    salt = passwd[0:2]
    with open(f'{dir}/dict.txt') as f:
        while True:
            p = f.readline().strip("\n")
            if not p:
                break
            c = crypt.crypt(p,salt)
            if c == passwd:
                print (f"[+] Found Password: {p}")
                return
    print ("[-] Password Not Found")

def main():        
    with open(f"{dir}/passwd") as f:
        while True:
            l = f.readline().strip("\n")
            if not l:
                break
            l=l.split(":")
            print (f"[*] Cracking Password For: {l[0]}")
            hp = l[1].strip()
            testPass(hp)
            
if __name__ == "__main__": 
    main()
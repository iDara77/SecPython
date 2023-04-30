import crypt

with open("./passwd/passwd") as f:
    l = f.readline()[:-1]
    hp = l.split(":")[1].strip()
    hx = crypt.crypt("egg","HX")
    if hp == hx:
        print("password is 'egg'")
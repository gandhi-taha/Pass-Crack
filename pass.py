import os
import random as rase
os.system("clear")
os.system("apt-get install figlet")
os.system("clear")
liste = ["A","B","C","Ç","D","E","F","G","Ğ","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z","a","b","c","ç","d","e","f","g","ğ","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z",1,2,3,12,123,1234,12345,123456,1234567,12345678,123456789,123456789987,1234567899876,12345678998765,123456789987654,1234567899876543,12345678998765432,123456789987654321,159753,1,2,3,4,5,6,7,8,9,"+","++","--","-"]
listeusr = ["root","admin","msfadmin","administrator","toor"]
passdude = []
def hesaplamausr():
    asd = 1
    while asd >= 2000:
        e = rase.choice(listeusr)
        e = str(e)
        pass1 = e + f
        pass2 = f + e
        pass3 = g + e + f
        pass4 = f + e + g
        pass5 = e + f + g
        pass6 = b + e
        pass7 = b + e + f
        pass8 = f + e + b
        pass9 = e + f + b
        pass10 = e + b + f
        pass11 = c + b + f
        pass12 = c + f + b + e
        pass13 = c + f + b
        pass14 = f + b + c
        pass15 = b + c + f
        pass16 = b + c + f + g
        pass17 = b + f + c
        pass18 = f + c + e
        pass19 = e + c + f
        pass20 = b + e + f + g
        pass21 = e + e + e
        pass22 = e + e
        pass23 = e
        passdude.append(pass1)
        passdude.append(pass2)
        passdude.append(pass3)
        passdude.append(pass4)
        passdude.append(pass5)
        passdude.append(pass6)
        passdude.append(pass7)
        passdude.append(pass8)
        passdude.append(pass9)
        passdude.append(pass10)
        passdude.append(pass11)
        passdude.append(pass12)
        passdude.append(pass13)
        passdude.append(pass14)
        passdude.append(pass15)
        passdude.append(pass16)
        passdude.append(pass17)
        passdude.append(pass18)
        passdude.append(pass19)
        passdude.append(pass20)
        passdude.append(pass21)
        passdude.append(pass22)
        passdude.append(pass23)
        asd += 1
        if asd == 2000:
            break
        else:
            continue
    return passdude
def hesaplama():
    asd = 1
    while asd < 1000:
        e = rase.choice(liste)
        e = str(e)
        pass1 = e + f
        pass2 = f + e
        pass3 = g + e + f
        pass4 = f + e + g
        pass5 = e + f + g
        pass6 = b + e
        pass7 = b + e + f
        pass8 = f + e + b
        pass9 = e + f + b
        pass10 = e + b + f
        pass11 = c + b + f
        pass12 = c + f + b + e
        pass13 = c + f + b
        pass14 = f + b + c
        pass15 = b + c + f
        pass16 = b + c + f + g
        passdude.append(pass1)
        passdude.append(pass2)
        passdude.append(pass3)
        passdude.append(pass4)
        passdude.append(pass5)
        passdude.append(pass6)
        passdude.append(pass7)
        passdude.append(pass8)
        passdude.append(pass9)
        passdude.append(pass10)
        passdude.append(pass11)
        passdude.append(pass12)
        passdude.append(pass13)
        passdude.append(pass14)
        passdude.append(pass15)
        passdude.append(pass16)
        asd += 1
        if asd == 1000:
            break
        else:
            continue
    return passdude
print("""
  .------------------------------------------.
  |           ~ P A S S A W O R D ~          |
  |             ~ C R E A T O R ~            |
  |                                          |
  |----------------M--E--N--U----------------|
  |                                          |
  |      1.) Create a passaword list         |
  |      2.) Create a username list          |
  |     Press any different key to exit      |
  |           created by; Toxic              |
  |                                          |
  .------------------------------------------.
""")
a = int(input("[*] Please enter choice.: "))
if a == 1:
    os.system("clear")
    os.system("figlet PASSAWORD")
    f = input("[*] Please enter victim name.: ")
    g = input("[*] Please enter victim surname.: ")
    b = input("[*] Please enter victim nickname.: ")
    c = input("[*] Please enter victim born date (ddmmyy).: ")
    hesaplama()
    x = open("pass.txt", "w")
    for xd in passdude:
        x.write("%s\n" % xd)
    x.close()
    os.system("clear")
    os.system("figlet SUCCESS")
    print("""
    [x] %s passaword list is created. 
    """% f)
    ix = input("[*] Did you want check file ? [Y / N].: ")
    if ix == "Y":
        os.system("cat pass.txt")
    else:
        os.system("exit")
elif a == 2:
    os.system("clear")
    os.system("figlet USERNAME")
    f = input("[*] Please enter victim name.: ")
    g = input("[*] Please enter victim surname.: ")
    b = input("[*] Please enter victim nick name.: ")
    c = input("[*] Please enter victim born date (ddmmyy).: ")
    hesaplamausr()
    x = open("username.txt", "w")
    for xd in passdude:
        x.write("%s\n" % xd)
    x.close()
else:
    os.system("exit")
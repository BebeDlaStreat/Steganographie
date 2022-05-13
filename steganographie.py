from PIL import Image               # Import de la classe Image
import math

def lsbCode(A, B):
    if len(A) != 8 or len(B) != 8:
        return
    return B[:5] + A[:3]
def lsbDecode(C):
    if len(C) != 8:
        return
    return (C[5:] + "0"*5, C[:5] + "0"*3)
def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m
def toString(a):
  l=[]
  m=""
  for i in a:
    b=0
    c=0
    if i == 0:
        k = 0
    else:
        k=int(math.log10(i))+1
    for j in range(k):
      b=((i%10)*(2**j))   
      i=i//10
      c=c+b
    l.append(c)
  for x in l:
    m=m+chr(x)
  return m
def tupleString(a):
    b = ""
    for c in a:
        d = str(c)
        if len(d) < 8:
            d = "0" * (8 - len(d)) + d
        b = b + d
    return b

def saveImage(message, fichier, fichier2):
    img = Image.open(fichier)
    phraseBinary = tupleString(toBinary(message))
    phraseBinary += "11111111"

    i = 0
    z = 0
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixel = img.getpixel((x, y))
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            rB = bin(r)[2:]
            gB = bin(g)[2:]
            bB = bin(b)[2:]
            if len(rB) < 8:
                rB = "0" * (8 - len(rB)) + rB
            if len(gB) < 8:
                gB = ("0" * (8 - len(gB))) + gB
            if len(bB) < 8:
                bB = ("0" * (8 - len(bB))) + bB
            size = len(phraseBinary)
            rI = r
            gI = g
            bI = b
            substract = size - i
            if (substract < 8):
                if substract > 0:
                    rI = (int(lsbCode(phraseBinary[i:8+i] + "0"*(8-substract), rB), 2))
                    i += 3
            else:
                rI = (int(lsbCode(phraseBinary[i:8+i], rB), 2))
                i += 3

            substract = size - i
            if (substract < 8):
                if substract > 0:
                    gI = (int(lsbCode(phraseBinary[i:8+i] + "0"*(8-substract), gB), 2))
                    i += 3
            else:
                gI = (int(lsbCode(phraseBinary[i:8+i], gB), 2))
                i += 3

            substract = size - i
            if (substract < 8):
                if substract > 0:
                    bI = (int(lsbCode(phraseBinary[i:8+i] + "0"*(8-substract), bB), 2))
                    i += 3
            else:
                bI = (int(lsbCode(phraseBinary[i:8+i], bB), 2))
                i += 3
            z = z + 1
            if len(pixel) > 3:
                img.putpixel((x,y), (rI, gI, bI, pixel[3]))
            else:
                img.putpixel((x,y), (rI, gI, bI))
    img.save(fichier2, quality=100)

def getMessage(fichier):
    img = Image.open(fichier)
    decode = ""
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixel = img.getpixel((x, y))
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            rB = bin(r)[2:]
            gB = bin(g)[2:]
            bB = bin(b)[2:]
            if len(rB) < 8:
                rB = "0" * (8 - len(rB)) + rB
            if len(gB) < 8:
                gB = ("0" * (8 - len(gB))) + gB
            if len(bB) < 8:
                bB = ("0" * (8 - len(bB))) + bB
            decode += lsbDecode(rB)[0][:3]
            decode += lsbDecode(gB)[0][:3]
            decode += lsbDecode(bB)[0][:3]
    zem = True
    resultat = []
    for j in range(0, len(decode), 8):
        if zem == True:
            
            part = decode[j: j+8]
            if part == "11111111":
                zem = False
            else:
                resultat.append(int(part))
    return toString(resultat)


print("------------------------------")
print("Que souhaitez-vous faire ?")
print("1 pour crypté l'image (Elle doit être dans le dossier sous le nom image1.py)")
print("2 pour décrypté l'image (Elle doit être dans le dossier sous le nom image2.py)")
print("------------------------------")
action = input("Alors ?\n")
if action == "1":
    message = input("Quel message souhaites-tu faire passer ?\n")
    fichier = input("Quel est le nom du fichier ?\n")
    fichier2 = input("Quel est le nom du fichier de sortie ?\n")
    saveImage(message, fichier, fichier2)
    print("L'image a bien été sauvegardé")
if action == "2":
    fichier = input("Quel est le nom du fichier ?\n")
    print("Le message est", getMessage(fichier))

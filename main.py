import modules.function as mf
print("Veuillez saisir le type de chifrrement que vous voulez faire :")
affichage = [
    "1- chiffrement ROT13",
    "2- chiffrement de Cesar",
    "3- chiffrement de atbash",
    "4- chiffrement de Blaise de Vigenere",
    "5- chiffrement par substitution",
]
for i in affichage:
    print(i)
print()
option = input()

if option == "1":
    text = input("Veuillez entrer le texte a chiffrer ou  a dechiffrer : ")
    print(f"Chiffrement : {mf.rot13(text)}")
    print(f"texte original : {text}")
if option == "2":
    text = input("Veuillez entrer le texte a chiffrer ou  a dechiffrer : ")
    cle = input("Veuillez entrer la cle de chiffrement ou  la cle de dechiffrement : ")
    mode  = input("Veuillez entrer le mode si chiffrer ou dechiffrer ")
    print(f"Chiffrement : {mf.chiffrement_cesar(text,cle,mode)}")
    print(f"texte original : {text}")
if option == "3":
    text = input("Veuillez entrer le texte a chiffrer ou  a dechiffrer : ")
    print(f"Chiffrement : {mf.atbash(text)}")
    print(f"texte original : {text}")
if option == "4":
    text = input("Veuillez entrer le texte a chiffrer ou  a dechiffrer : ")
    cle = input("Veuillez entrer la cle de chiffrement ou  la cle de dechiffrement : ")
    mode  = input("Veuillez entrer le mode si chiffrer ou dechiffrer ")
    print(f"Chiffrement : {mf.vigenere_blaise(text,cle,mode)}")
    print(f"texte original : {text}")
if option == "5":
    text = input("Veuillez entrer le texte a chiffrer ou  a dechiffrer : ")
    ma_cle = mf.generer_cle_aleatoire()
    print(f"Clé utilisée : {ma_cle}")
    print(f"Chiffrement : {mf.substitution(text,cle)}")
    print(f"texte original : {text}")

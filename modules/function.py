import random
def rot13(text):
  
    result = ""
    for i in text:
        if i.isalpha() and i.isupper():
            new_code = ((ord(i) - 65 + 13) % 26) + 65
            result += chr(new_code)
        elif i.isalpha() and i.islower():
            new_code = ((ord(i) - 97 + 13) % 26) + 97
            result += chr(new_code)
        else:
            result += "Veuillez saisir des lettres majuscules ou minuscules"
    return result


def chiffrement_cesar(text, cle, mode="Chiffrer"):
    if mode == "dechiffrer":
        cle = -cle
    result = ""
    for i in text:
        if i.isalpha() and (i.isupper() or i.islower()):
            base = ord("A") if i.isupper() else ord("a")
            position = ord(i) - base
            new_position = (position + cle) % 26
            result += chr(new_position + base)
        else:
            result += i
    return result


def atbash(text):
    result = ""
    for i in text:
        if i.isalpha() and i.isupper():
            new_code = 155 - ord(i)
            result += chr(new_code)
        elif i.isalpha() and i.islower():
            new_code = 219 - ord(i)
            result += chr(new_code)
        else:
            result += i
    return result


def vigenere_blaise(texte, cle, mode="chiffrer"):
    result = ""
    cle = cle.lower()
    index_cle = 0

    for i in texte:
        if i.isalpha():

            shift = ord(cle[index_cle % len(cle)]) - ord("a")
            if mode == "dechiffrer":
                shift = -shift

            base = ord("A") if i.isupper() else ord("a")
            new_code = chr((ord(i) - base + shift) % 26 + base)
            result += new_code

            index_cle += 1
        else:

            result += i

    return result


# Test
# msg = "L'ALGORITHME DE VIGENERE"
# key = "PYTHON"
# code = vigenere_blaise(msg, key)
# print(f"Chiffré : {code}")
# print(f"Original: {vigenere_blaise(code, key, 'dechiffrer')}")




def generer_cle_aleatoire():
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random.shuffle(alphabet)
    return "".join(alphabet)

def substitution(texte, cle, mode='chiffrer'):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if mode == 'chiffrer':
        table = str.maketrans(alphabet + alphabet.lower(), cle + cle.lower())
    else:
        table = str.maketrans(cle + cle.lower(), alphabet + alphabet.lower())
        
    return texte.translate(table)

# Test
# ma_cle = generer_cle_aleatoire()
# print(f"Clé utilisée : {ma_cle}")

# message = "Ceci est un secret de substitution"
# code = substitution(message, ma_cle)
# print(f"Chiffré : {code}")
# print(f"Original: {substitution(code, ma_cle, 'dechiffrer')}")
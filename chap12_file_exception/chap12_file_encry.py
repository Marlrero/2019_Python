key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plain):
    result = ''

    for l in plain.lower():
        try:
            i = (key.index(l) + n) % len(key)
            result += key[i]
        except ValueError:
            result += l

    return result.lower()

def decrypt(n, cipher):
    result = ''

    for l in cipher:
        try:
            i = (key.index(l) - n) % len(key)
            result += key[i]
        except ValueError:
            result += l

    return result

text = 'the language of truth is simple'
n = 3
encrypted = encrypt(n, text)
decrypted = decrypt(n, encrypted)

print('평문 > ' + text)
print('암호문 > ' + encrypted)
print('복호문 > ' + decrypted)
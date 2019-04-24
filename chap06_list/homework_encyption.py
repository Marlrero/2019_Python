password = input("password input >> ")

encryption = []
for i in password:
    encryption.append(str(ord(i) + 2)) #ord함수는 문자를 아스키코드로 바꿈

print("encyption =", "".join(encryption))

decryption = []
for i in encryption: #암호 리스트를 하나씩 꺼내서
    decryption.append(str(chr(int(i) - 2))) #int함수를 이용해 원래 값으로 바꾸고, 이를 문자로 바꿈

print("decryption =", "".join(decryption))

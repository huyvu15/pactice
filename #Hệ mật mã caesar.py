#Hệ mật mã caesar
text = input()
k = int(input())
  

for i in range(len(text)):     
    c = ord(text[i])+k
    
    if c >=192-k and c <=250-k:
        print(text[i], end = '')
    else:
        if ord('a') <= ord(text[i]) and ord(text[i])<ord('x'):
            print(chr(c), end = '')
        elif c >= ord('x'):
            c = c - 26
            print(chr(c), end = '')
        
            
        if ord('A') <= ord(text[i]) and ord(text[i])<ord('X'):
            print(chr(c), end = '')
        elif c >=ord('X'):
            c = c - 26
            print(chr(c),end='') 

# def mahoa(plaintext, key):
#     ciphertext = ""
#     for c in plaintext:
#         if c !=' ':
#             number = ord(c)-65
#             number = (number+ key) % 26
#             ciphertext = ciphertext + chr(number+65)
#         else: 
#             ciphertext = ciphertext +c
#     return ciphertext    

# print(mahoa(text, k))        
    
    
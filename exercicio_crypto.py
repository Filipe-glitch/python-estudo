#algoritmo cifra de cesar porém A = E, B = F e segue. Mensagem "mais amor"
from string import ascii_uppercase
from strings import mensagem
a = list(ascii_uppercase)
m = 'mais amor'.upper()
mc = ""
for l in m:
  if l in a:
    i = ord(l) - 65
    mc += a[(i + 4) % 26]
  else:
    mc += l  #mantém espaços
print(f'mensagem criptografada: {mc}')

#algoritmo cifra de cesar porém A = E, B = F e segue. Mensagem criptografada:IRXIRHMQIRXS
b = list(ascii_uppercase)
n = 'IRXIRHMQIRXS'
nc = ''
for k in n:
    if k in b:
        o = ord(k) - 65
        nc += b[(o - 4) % 26]
    else:
        nc += k
print(f'Mensagem original: {nc}')

#criptografia RSA: letras são substituídas por números de dois dígitos. palavra “mensagem”, forma criptografada
import rsa
chavepublica,chaveprivada= rsa.newkeys(512)
r = 'mensagem'
rc = rsa.encrypt(r.encode(), chavepublica)
print('mensagem original:', r)
print('mensagem criptografada: ', rc)
rd = rsa.decrypt(rc,chaveprivada).decode()
print('Mensagem descriptografada: ', rd)
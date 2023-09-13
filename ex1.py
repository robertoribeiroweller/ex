oq = []
sair = ''

while sair != 'S':
    
    # pensei agr nessa solução agr kkk
    sair = input('Qual seu desejo? digite S/s para sair: ').upper()
    oq.append(sair)
    
# lebra do pop? kkk aqui tou usando aqui para remover o primeiro elemento, tou pensando economizar variavel
oq.pop(-1)
for i in oq:
    print('seu(s) desejo(s) são(é)', i)

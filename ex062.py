from time import sleep
print('='*30)
print('{:^55}'.format('\033[2;36mOS 10 TERMOS DE UMA P.A.\033[m'))
primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
c = 0
termos = primeiro
print('Os dez primeiros termos de uma P.A. cujo o primeiro termo é {}.'.format(primeiro))
sleep(0.2)
print('E a razão é {}.'.format(razao))
sleep(0.2)
print('São...')
sleep(0.2)
while c < 10:
    print('{} ->'.format(termos) if c < 9 else '{}'.format(termos), end=' ')
    sleep(0.4)
    c += 1
    termos = primeiro + razao*c
pergunta = str(input('Deseja saber mais termos dessa P.A.?[S/N] ')).strip().upper()
if pergunta == 'S':
    cont = int(input('Quantos termos a mais você quer ver? '))
    termosnovos = primeiro + 10*razao
    print('Os próximos {} termos são: '.format(cont))
    c1 = 1
    while c1 <= cont:
        print('{} ->'.format(termosnovos) if c1 < cont + 1 else '{}'.format(termosnovos), end= ' ')
        sleep(0.4)
        c1 += 1
        termosnovos = primeiro + 9*razao + c1*razao
elif pergunta == 'N':
    print('OK')
    sleep(0.7)
    print('Exercício')
    sleep(0.7)
    print('sendo')
    sleep(0.5)
    print('\033[2;31mENCERRADO\033[m')
    sleep(0.5)
else:
    print('Não entendi sua opção')
print('FIM')


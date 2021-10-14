from time import sleep

print('=-='*20)
print('{:^94}'.format('\033[2;31m>>> Bem vindos ao nosso Quiz sobre prevenção e combate a Covid-19 <<<\033[m'))
print('=-='*20)

acertos = 0
erros = 0
pontos = 0

iniciar = str(input('Você gostaria participar de nosso Quiz? [S/N] ')).strip().upper()
while iniciar != 'S' and iniciar != 'N':
    print('Não entendi sua resposta.', end=' ')
    iniciar = str(input('Gostaria de jogar o Quiz? [S/N] ')).upper().strip()
if iniciar == 'S':
    print('Que ótimo. Vamos começar então...')
    sleep(1)
    print('''Questão 01: Onde foi identificada pela primeira vez um caso de Covid-19?
a) Nova York, EUA.
b) Tóquio, Japão.
c) Roma, Itália.
d) Wuhan, China.
e) Cidade do Cabo, África do sul.''')
    resposta1 = 'D'
    alternativa1 = str(input('Qual é a sua resposta? ')).strip().upper()
    if resposta1 == alternativa1:
        print('Resposta \033[2;31mCERTA\033[m!!!', end=' ')
        print('O primeiro caso da doença foi registrado na provínvia Chinesa de Wuhan, em dezembro de 2019.')
        print('-=-' * 31)
        acertos += 1
        pontos += 10
    elif resposta1 != alternativa1:
        print('Resposta \033[2;31mERRADA\033[m!!!', end=' ')
        print('O primeiro caso da doença foi registrado na provínvia Chinesa de Wuhan, em dezembro de 2019.')
        print('-=-'*31)
    print('''Questão 02: Dentre as muitas variáveis que podem otimizar o sistema imunológico humano, existe a Vitamina D.
Qual das alternativas abaixo é associada a produção de vitamina D pelo corpo humano?
a) Dormir tarde.
b) Diminuir a ingestão de açúcares.
c) Exposição a luz solar.
d) Isolamento social
e) Lavar as mãos com água  e sabão.''')
    resposta2 = 'C'
    alternativa2 = str(input('Qual é a sua resposta? ')).strip().upper()
    if resposta2 == alternativa2:
        print('Resposta \033[2;31mCERTA\033[m!!!', end=' ')
        print('A principal fonte de vitamina D é a sua produção na pele a partir da exposição aos raios solares.')
        print('-=-' * 31)
        acertos += 1
        pontos += 10
    elif resposta2 != alternativa2:
        print('Resposta \033[2;31mERRADA\033[m!!!', end=' ')
        print('A principal fonte de vitamina D é a sua produção na pele a partir da exposição aos raios solares.')
        print('-=-' * 31)

    print('''Questão 03: Segundo a mais recente atualização protocolar da Anvisa, pessoas infectadas com a Covid-19, 
que forem assintomáticos ou apresentarem sintomas leves. Devem praticar isolamento de quantos dias?
a) 10 dias de isolamento.
b) 15 dias de isolamento.
c) 20 dias de isolamento.
d) 30 dias de isolamento.
e) 60 dias de isolamento.''')

    resposta3 = 'A'
    alternativa3 = str(input('Qual é a sua resposta? ')).strip().upper()

    if resposta3 == alternativa3:
        print('Resposta \033[2;31mCERTA\033[m!!!', end=' ')
        print('A Anvisa determinou que pacientes assintomáticos ou com quadro leve de Covid-19 devem ser isolados por 10 dias.')
        print('-=-' * 31)
        acertos += 1
        pontos += 10

    elif resposta3 != alternativa3:
        erros += 1
        print('Resposta \033[2;31mERRADA\033[m!!!', end=' ')
        print('A Anvisa determinou que pacientes assintomáticos ou com quadro leve de Covid-19 devem ser isolados por 10 dias.')
        print('-=-' * 31)

elif iniciar == 'N':
    print('Que pena, mas se quiser reconsiderar e jogar é só \033[2;31mRENICIAR\033[m o jogo.')

print('Você acertou {} perguntas e errou {}. Por isso sua pontuação final foi de {} pontos.'.format(acertos, erros, pontos))



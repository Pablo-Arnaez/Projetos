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
    sleep(1)
    resposta1 = 'D'
    alternativa1 = str(input('Qual é a sua resposta? ')).strip().upper()
    if resposta1 == alternativa1:
        print('Resposta \033[2;31mCERTA\033[m!!!', end=' ')
        sleep(1)
        print('O primeiro caso da doença foi registrado na provínvia Chinesa de Wuhan, em dezembro de 2019.')
        sleep(3)
        print('-=-' * 31)
        acertos += 1
        pontos += 10
    elif resposta1 != alternativa1:
        erros += 1
        print('Resposta \033[2;31mERRADA\033[m!!!', end=' ')
        sleep(1)
        print('O primeiro caso da doença foi registrado na provínvia Chinesa de Wuhan, em dezembro de 2019.')
        sleep(3)
        print('-=-'*31)

    print('''Questão 02: Dentre as muitas variáveis que podem otimizar o sistema imunológico humano, existe a Vitamina D.
Qual das alternativas abaixo é associada a produção de vitamina D pelo corpo humano?
a) Dormir tarde.
b) Diminuir a ingestão de açúcares.
c) Exposição a luz solar.
d) Isolamento social
e) Lavar as mãos com água  e sabão.''')
    sleep(1)
    resposta2 = 'C'
    alternativa2 = str(input('Qual é a sua resposta? ')).strip().upper()
    if resposta2 == alternativa2:
        print('Resposta \033[2;31mCERTA\033[m!!!', end=' ')
        sleep(1)
        print('A principal fonte de vitamina D é a sua produção na pele a partir da exposição aos raios solares.')
        sleep(3)
        print('-=-' * 31)
        acertos += 1
        pontos += 10
    elif resposta2 != alternativa2:
        erros +=1
        print('Resposta \033[2;31mERRADA\033[m!!!', end=' ')
        sleep(1)
        print('A principal fonte de vitamina D é a sua produção na pele a partir da exposição aos raios solares.')
        sleep(3)
        print('-=-' * 31)

    print('''Questão 03: Segundo a mais recente atualização protocolar da Anvisa, pessoas infectadas com a Covid-19, 
que forem assintomáticos ou apresentarem sintomas leves. Devem praticar isolamento de quantos dias?
a) 10 dias de isolamento.
b) 15 dias de isolamento.
c) 20 dias de isolamento.
d) 30 dias de isolamento.
e) 60 dias de isolamento.''')
    sleep(1)

    resposta3 = 'A'
    alternativa3 = str(input('Qual é a sua resposta? ')).strip().upper()

    if resposta3 == alternativa3:
        print('Resposta \033[2;31mCERTA\033[m!!!', end=' ')
        sleep(1)
        print('A Anvisa determinou que pacientes assintomáticos ou com quadro leve de Covid-19 devem ser isolados por 10 dias.')
        sleep(3)
        print('-=-' * 31)
        acertos += 1
        pontos += 10

    elif resposta3 != alternativa3:
        erros += 1
        print('Resposta \033[2;31mERRADA\033[m!!!', end=' ')
        sleep(1)
        print('A Anvisa determinou que pacientes assintomáticos ou com quadro leve de Covid-19 devem ser isolados por 10 dias.')
        sleep(3)
        print('-=-' * 31)

    print('''Questão 04: Quais exames são usados para o diagnóstico do coronavírus?
a) Teste de reflexos e PCR.
b) Contagem de plaquetas e teste de temperatura.
c) Teste de temperatura e teste de reflexos.
d) Teste sorológico e contagem de plaquetas.
e) PCR e testes sorológicos.''')
    sleep(1)

    resposta4 = 'E'
    alternativa4 = str(input('Qual é a sua resposta? ')).strip().upper()

    if resposta4 == alternativa4:
        print('Resposta \033[2;31mCERTA\033[m!!!', end=' ')
        sleep(1)
        print('O protocolo oficial OMS determina que o PCR (Reação em cadeia da Polimerase) e os testes sorológicos (anticorpos presente no sangue) são as metodolgiais a serem usadas para esse fim.')
        sleep(3)
        print('-=-' * 31)
        acertos += 1
        pontos += 10

    elif resposta4 != alternativa4:
        erros += 1
        print('Resposta \033[2;31mERRADA\033[m!!!', end=' ')
        sleep(1)
        print('O protocolo oficial OMS determina que o PCR (Reação em cadeia da Polimerase) e os testes sorológicos (anticorpos presente no sangue) são as metodolgiais a serem usadas para esse fim.')
        sleep(3)
        print('-=-' * 31)

    print('''Questão 05: Qual foi a primeira vacina aprovada pela ANVISA?
a) CoronaVac.
b) AstraZeneca.
c) Pfizer.
d) Sputnik V.
e) Janssen.''')
    sleep(1)

    resposta5 = 'C'
    alternativa5 = str(input('Qual é a sua resposta? ')).strip().upper()

    if resposta5 == alternativa5:
        print('Resposta \033[2;31mCERTA\033[m!!!', end=' ')
        sleep(1)
        print('O primeiro registro definitivo concedido pela ANVISA a uma vacina contra a Covid 19, foi concedido a empresa farmacêutica Norte-americana Pfizer.')
        sleep(3)
        print('-=-' * 31)
        acertos += 1
        pontos += 10

    elif resposta5 != alternativa5:
        erros += 1
        print('Resposta \033[2;31mERRADA\033[m!!!', end=' ')
        sleep(1)
        print('O primeiro registro definitivo concedido pela ANVISA a uma vacina contra a Covid 19, foi concedido a empresa farmacêutica Norte-americana Pfizer.')
        sleep(3)
        print('-=-' * 31)

    print('''Questão 06: Em qual período iniciou-se a vacinação contra a covid-19 no Brasil?
a) Janeiro de 2021.
b) Maio de 2020.
c) Outubro de 2021.
d) Janeiro de 2020.
e) Dezembro de 2019.''')
    sleep(1)

    resposta6 = 'A'
    alternativa6 = str(input('Qual é a sua resposta? ')).strip().upper()

    if resposta6 == alternativa6:
        print('Resposta \033[2;31mCERTA\033[m!!!', end=' ')
        sleep(1)
        print('A data oficial do início da vacinação contra a Covid-19 foi dia 17 de janeiro de 2021.')
        sleep(3)
        print('-=-' * 31)
        acertos += 1
        pontos += 10

    elif resposta6 != alternativa6:
        erros += 1
        print('Resposta \033[2;31mERRADA\033[m!!!', end=' ')
        sleep(1)
        print('A data oficial do início da vacinação contra a Covid-19 foi dia 17 de janeiro de 2021.')
        sleep(3)
        print('-=-' * 31)

    print('''Questão 07: Quais das alternativas abaixo não representa um meio de transmissão do Corona Vírus:
a) Tosse.
b) Toque do aperto de mãos contaminadas.
c) Espirro.
d) Uso de máscara.
e) Contato com objetos ou superfícies contamidas.''')
    sleep(1)

    resposta7 = 'D'
    alternativa7 = str(input('Qual é a sua resposta? ')).strip().upper()

    if resposta7 == alternativa7:
        print('Resposta \033[2;31mCERTA\033[m!!!', end=' ')
        sleep(1)
        print('Todas as opções acima representam formas da Covid-19 propagar-se, exceto o uso de máscara, que é muito importante no combate a propagação do mesmo.')
        sleep(3)
        print('-=-' * 31)
        acertos += 1
        pontos += 10

    elif resposta7 != alternativa7:
        erros += 1
        print('Resposta \033[2;31mERRADA\033[m!!!', end=' ')
        sleep(1)
        print('Todas as opções acima representam formas da Covid-19 propagar-se, exceto o uso de máscara, que é muito importante no combate a propagação do mesmo.')
        sleep(3)
        print('-=-' * 31)

    print('''Questão 08: Quais das alternativas abaixo não representam possíveis sintomas da presença do Corona Vírus no organismo:
a) Tosse e febre.
b) Perda de memória e cegueira parcial.
c) Coriza e dor de garganta.
d) Dispnéia e dificuldade de respirar.
e) Perda do olfato e alteração do paladar.''')
    sleep(1)

    resposta8 = 'B'
    alternativa8 = str(input('Qual é a sua resposta? ')).strip().upper()

    if resposta8 == alternativa8:
        print('Resposta \033[2;31mCERTA\033[m!!!', end=' ')
        sleep(1)
        print('A perda de memória e cegueira parcial, ao contrário das demais alternativas, não constituem o quadro de possíveis sintomas da Covid-19')
        sleep(3)
        print('-=-' * 31)
        acertos += 1
        pontos += 10

    elif resposta8 != alternativa8:
        erros += 1
        print('Resposta \033[2;31mERRADA\033[m!!!', end=' ')
        sleep(1)
        print('A perda de memória e cegueira parcial, ao contrário das demais alternativas, não constituem o quadro de possíveis sintomas da Covid-19')
        sleep(3)
        print('-=-' * 31)

    print('''Questão 09: Quais das alternativas abaixo não representa uma medida oficial de combate a propagação da Covid-19?
a) Auxílio emergencial.
b) Uso de máscara.
c) Vacinação imunizante.
d) Isolamento social.
e) Restrinção das atividades não essenciais.''')
    sleep(1)

    resposta9 = 'A'
    alternativa9 = str(input('Qual é a sua resposta? ')).strip().upper()

    if resposta9 == alternativa9:
        print('Resposta \033[2;31mCERTA\033[m!!!', end=' ')
        sleep(1)
        print('Todas as alternativas representam medidas de combate a propagação da Covid-19, exceto a opção A.')
        sleep(3)
        print('-=-' * 31)
        acertos += 1
        pontos += 10

    elif resposta9 != alternativa9:
        erros += 1
        print('Resposta \033[2;31mERRADA\033[m!!!', end=' ')
        sleep(1)
        print('Todas as alternativas representam medidas de combate a propagação da Covid-19, exceto a opção A.')
        sleep(3)
        print('-=-' * 31)

    print('''Questão 10: Sabemos que uma Epidemia é a manifestação coletiva de uma doença que rapidamente se espalha, por contágio direto ou indireto, até atingir um grande número de pessoas em um determinado território.\nAssinale a alternativa abaixo necessária para uma epidemia tornar-se uma Pandemia:
a) A existência de 2 ou mais vírus durante a infecção epidêmica.
b) O nível alto de letalidade do vírus.
c) A falta de vacinação e ou tratamento.
d) A não imunização de rebanho.
e) A propagação da doença atingir uma grande região geográfica.''')
    sleep(1)

    resposta10 = 'E'
    alternativa10 = str(input('Qual é a sua resposta? ')).strip().upper()

    if resposta10 == alternativa10:
        print('Resposta \033[2;31mCERTA\033[m!!!', end=' ')
        sleep(1)
        print('O critério principal de classificação de uma Pandemia é a dissiminação da doença em uma grande região geográfica, como por exemplo todo o planeta Terra.')
        sleep(3)
        print('-=-' * 31)
        acertos += 1
        pontos += 10

    elif resposta10 != alternativa10:
        erros += 1
        print('Resposta \033[2;31mERRADA\033[m!!!', end=' ')
        sleep(1)
        print('O critério principal de classificação de uma Pandemia é a dissiminação da doença em uma grande região geográfica, como por exemplo todo o planeta Terra.')
        sleep(3)
        print('-=-' * 31)

    print('Você acertou {} perguntas e errou {}. Por isso sua pontuação final foi de {} pontos.'.format(acertos, erros, pontos))
    sleep(1/2)
    print('Isso representa um total de {}% de aproveitamento.'.format(acertos * 10))
    sleep(1/2)
    if acertos >= 9:
        print(
            'Parabéns, {}% é um ótimo rendimento e você pode ser considerado um \033[2;31mEXPERT\033[m no assunto.'.format(acertos * 10))

    elif acertos < 9 and acertos >= 7:
        print('Parabéns, {}% é um bom rendimento, mas se você quiser melhorar pode simplesmente reiniciar o jogo.'.format(acertos * 10))

    else:
        print('Você pode melhorar melhorar seus conhecimentos sobre o assunto.\nQue tal \033[2;31mRENICIAR\033[m o jogo?')

elif iniciar == 'N':
    print('Que pena, mas se quiser reconsiderar e jogar é só \033[2;31mRENICIAR\033[m o jogo.')



from random import randint
r = r1 =''
soma = 0
print('-' * 25)
print('Vamos jogar par ou ímpar?')
print('-' * 25)
while True:
    n1 = int (input('Diga um número de 1 a 10:'))
    if n1 > 10:
       n1 = int(input('Você só tem dez dedos engraçadinho:'))
    r1 = str(input('Par ou ímpar?')).strip().upper()[0]

    n = randint(0,10)
    soma = n1 + n
    print(f'ok, eu escolho {n} e {n1} + {n} = {soma}')
    if soma % 2 == 0:
        print('deu par!')
    else:
        print('deu ímpar!')
    if soma %2 ==0 and r1 == 'P'or soma % 2 != 0 and r1 == 'I':
        print('Você ganhou! :(')
    else:
        print('Que pena, eu ganhei :)')
    print('-' * 25)
    r = str(input('Quer jogar de novo?')).strip().upper()[0]

    if r == 'N':
        print('Obrigada por jogar comigo! até mais :)')
        break

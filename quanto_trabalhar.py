#Quantas horas preciso trabalhar para comprar isso?
valor_prod = None
while valor_prod  == None :
    try:
        valor_prod = float(input('Quanto custa o que você quer comprar? '))
    except ValueError:
        print('Digite somente números nessa etapa.')

sala_total = None
while sala_total == None :
    try:
        sala_total = float(input('Quanto você recebe por mês? '))
    except ValueError:
        print('Digite somente números nessa etapa.')

dia_trab = None
while dia_trab == None :
    try :
        dia_trab = int(input('Quantos dias no mês você trabalha? '))
        if dia_trab > 31 or dia_trab < 0:
            print('Digite um valor menor ou igual a 31.')
            dia_trab = None
    except ValueError:
        print('Digite somente números inteiros nessa etapa.')
    

hora_trab = None
while hora_trab == None:
    try :  
        hora_trab = float(input('Quantas horas por dia você trabalha?'))
        if hora_trab > 24 or hora_trab <0:
            print('Digite um valor menor ou igual a 24')
            dia_trab = None
    except ValueError:
        print('Digite somente números nessa etapa.')


sala_dia = sala_total / dia_trab
sala_hora = sala_dia / hora_trab
hora_neces = valor_prod // sala_hora
print('Voce precisa trabalhar:{}'.format(hora_neces))


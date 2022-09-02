#Quantas horas preciso trabalhar para comprar isso?
valor_prod=int(input('Quanto custa o que você quer comprar?'))
sala_total=int(input('Quanto você recebe por mês?'))
dia_trab=int(input('Quantos dias no mês você trabalha?'))
hora_trab=int(input('Quantas horas por dia você trabalha?'))
sala_dia=sala_total/dia_trab
sala_hora=sala_dia/hora_trab
hora_neces=valor_prod/sala_hora
print('Voce precisa trabalhar: ',hora_neces,' horas.')

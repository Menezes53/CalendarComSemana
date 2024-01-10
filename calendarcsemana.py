import calendar 

ano = 2024
mes = 1
dia = 9

dia_semana = calendar.weekday(ano, mes, dia)

if dia_semana == 0 :
    print('Segunda-Feira')
elif dia_semana == 1 :
    print('Terça-Feira-Meu Niver')
elif dia_semana == 2 :
    print('Quarta-Feira')
elif dia_semana == 3 :
    print('Quinta-Feira')
elif dia_semana == 4 :
    print('Sexta-Feira')
elif dia_semana == 5 :
    print('Sábado')

else :
    print('Domingo')
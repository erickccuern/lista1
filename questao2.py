lista = [1,3,5,7,234,754,-213,656,12,435,56,4,9,6,4578,-65,-890,45,999,4567,233,565,987,-24,0]
print(lista)
menor = lista[0]
maior = 0
soma = 0
variancia = 0
posMenor = 0
posMaior = 0
for i in range(25):
    if lista[i] < menor:
        menor = lista[i]
        posMenor = i
    if lista[i] > maior:
        maior = lista[i]
        posMaior = i
    soma+=lista[i]

media = soma/25
for i in range(25):
    variancia+=(lista[i]-media)**2
variancia/=25
desvioPadrao = sqrt(variancia)
print('Menor Valor: ',menor)
print('Maior Valor: ',maior)
print('Posição do Menor Valor: ',posMenor)
print('Posição do Maior Valor: ',posMaior)
print('Média: ',media)
print('Desvio Padrão: ',desvioPadrao)
    

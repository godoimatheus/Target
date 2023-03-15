import json

f = open("dados.json")

data = json.load(f)

faturamento_total = 0
num_dias = 0
maior_faturamento = float('-inf')
menor_faturamento = float('inf')

for dia in data:
    faturamento = dia['valor']
    if faturamento == 0:
        continue
    faturamento_total += faturamento
    num_dias += 1
    if faturamento < menor_faturamento:
        menor_faturamento = faturamento
    if faturamento > maior_faturamento:
        maior_faturamento = faturamento

media_faturamento = faturamento_total / num_dias

dias_acima_media = 0
for dia in data:
    if dia['valor'] > media_faturamento:
        dias_acima_media += 1

print('Menor faturamento por dia:', menor_faturamento)
print('Maior faturamento por dia:', maior_faturamento)
print('Número de dias com faturamento acima da média:', dias_acima_media)

f.close()

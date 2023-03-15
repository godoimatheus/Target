billing = {
    'SP': 67826.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}
total = 0
for v in billing.values():
    total += v
print('Representação percentual:')
for k, v in billing.items():
    percent = v * 100 / total
    print(f'{k} = {percent:.2f}%')

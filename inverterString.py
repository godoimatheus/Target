word = str(input('Informe uma palavra para ver sua inversão: '))
reverseWord = word[::-1]
print(f'A palavra {word} invertida fica {reverseWord}')
if word == reverseWord:
    print('É um palíndromo')

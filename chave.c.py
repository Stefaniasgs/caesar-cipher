import string

alfabeto = string.ascii_uppercase + string.digits + string.punctuation + ' '
texto = input('Digite a mensagem: ').upper()
chave_palavra = input('Digite a chave:').upper()
mensagem_cifrada = ''
chave_numeros = []
for letra in chave_palavra:
    chave_numeros.append(alfabeto.index(letra))
for i, letra in enumerate(texto):
    indice = alfabeto.index(letra)
    posicao = chave_numeros[i % len(chave_numeros)]
    novo_indice = (indice + posicao) % len (alfabeto)
    nova_letra = alfabeto[novo_indice]
    mensagem_cifrada += nova_letra
    print(nova_letra)
with open ('mensagem_cifrada.txt', 'w') as arquivo:
    arquivo.write(mensagem_cifrada)















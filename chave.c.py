import string

alfabeto = string.ascii_uppercase + string.digits + string.punctuation + ' '
texto = input('Digite a mensagem: ').upper()
chave = 5
mensagem_cifrada = ''
for letra in texto:
    indice = alfabeto.index(letra)
    novo_indice = (indice+chave) % 26
    nova_letra = alfabeto[ novo_indice ]
    mensagem_cifrada += nova_letra
    print(nova_letra)
with open ('mensagem_cifrada.txt', 'w') as arquivo:
    arquivo.write(mensagem_cifrada)











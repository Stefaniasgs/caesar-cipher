import string

alfabeto = string.ascii_uppercase + string.digits + string.punctuation + ' '

def criptografar(texto, chave_palavra):
    chave_numeros = []
    mensagem_cifrada = ''
    for letra in chave_palavra:
        chave_numeros.append(alfabeto.index(letra))
    for i, letra in enumerate(texto):
        indice = alfabeto.index(letra)
        posicao = chave_numeros[i % len(chave_numeros)]
        novo_indice = (indice + posicao) % len(alfabeto)
        nova_letra = alfabeto[novo_indice]
        mensagem_cifrada += nova_letra
    return mensagem_cifrada

def descriptografar(texto, chave_palavra):
    chave_numeros = []
    mensagem_cifrada = ''
    for letra in chave_palavra:
        chave_numeros.append(alfabeto.index(letra))
    for i, letra in enumerate(texto):
        indice = alfabeto.index(letra)
        posicao = chave_numeros[i % len(chave_numeros)]
        novo_indice = (indice - posicao) % len(alfabeto)
        nova_letra = alfabeto[novo_indice]
        mensagem_cifrada += nova_letra
    return mensagem_cifrada

while True:
    print('\n================================')
    print('   CIFRA DE CESAR ')
    print('================================')
    print('1. Criptografar')
    print('2. Descriptografar')
    print('3. Sair')

    alternativa = input('Escolha uma opção: ')

    if alternativa == '3':
        break

    texto = input('Digite a mensagem: ').upper()
    chave_palavra = input('Digite a chave: ').upper()

    if alternativa == '1':
        resultado = criptografar(texto, chave_palavra)
    elif alternativa == '2':
        resultado = descriptografar(texto, chave_palavra)

    print('Resultado:', resultado)

    with open('mensagem_cifrada.txt', 'w') as arquivo:
          arquivo.write(resultado)
